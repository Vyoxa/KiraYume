# Copyright (C) 2024 Yousef A. (Vyoxa).
# Licensed under the GPL-3.0 License.
# Created for KiraYume: https://github.com/Vyoxa/KiraYume

import os
from configparser import ConfigParser
from functools import lru_cache

from PyQt6.QtCore import QThread, pyqtSignal
from PIL import Image, ImageDraw, ImageFont, ImageOps

import pytesseract
import arabic_reshaper
from bidi.algorithm import get_display
from deep_translator import GoogleTranslator

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from .Constants import (COLOR_INFO, COLOR_SUCCESS,
                        LANGUAGE_CODES, DEEPL_LANGUAGES, COLOR_ERROR)


class TranslationWorker(QThread):
    finish_signal = pyqtSignal(int, str)
    setInfo = pyqtSignal(str, str)

    def __init__(self, parent=None, image_paths: tuple = (None, None), translation_mode: tuple = (None, None, None, None, None)):

        super().__init__(parent)
        self.og_image_path = None
        self.og_image_name = None
        self.extension_suffix = None
        self.original_name = None
        self.save_location = None
        self.save_as_name = None
        self.dump_translation = None
        self.language_from = None
        self.language_to = None
        self.text_color = None
        self.background_color = None
        self.OCR_languages = None
        self.font_name = None
        self.font_path = None

        self.main = parent
        # Modes are: 0, 1, 2; Normal Translation, Scanner Mode, Eraser Mode.
        # self.x0, self.y0, self.x1, self.y1 are only used in Scanner & Eraser mode in which the starting location of the cropped area is needed in order to paste it back in
        self.translation_mode, self.x0, self.y0, self.x1, self.y1 = translation_mode
        self.og_image_path, self.translated_image_path = image_paths  # Original location of the image path and the location of its translated variant if one exists

    def run(self):
        try:
            self.setInfo.emit(f"Loading data from config file...", COLOR_INFO)
            self.load_data()
            self.setInfo.emit(f"[{self.og_image_name}] Reading image using ({self.OCR_languages}) from TesseractOCR...", COLOR_INFO)
            original_pil_image = Image.open(self.og_image_path).convert("RGB")
            match self.translation_mode:
                case 0:  # 0: Normal Translation: Takes Full Original Image, scans, translates, edits, and saves entire image.
                    bubbles = self.read_image(original_pil_image)

                    self.setInfo.emit(f"[{self.og_image_name}] Translating sentences from {self.language_from} to {self.language_to} using {self.translator}...", COLOR_INFO)
                    original_sentences, translated_sentences = self.translate_text(bubbles)

                    self.setInfo.emit(f'[{self.og_image_name}] Clearing original text and replacing with translated text using font "{self.font_name}"...', COLOR_INFO)
                    edited_pil_image = self.edit_image(original_pil_image, bubbles, original_sentences, translated_sentences)  # TODO: JAPANESE DOESN'T WORK, list out of index error

                    self.setInfo.emit(f'[{self.og_image_name}] Saving image...', COLOR_INFO)
                    self.translated_image_path = self.prep_image_path(extension_suffix=self.extension_suffix, original_name=self.original_name, language_from=self.language_from, language_to=self.language_to, translator=self.translator)
                    edited_pil_image.save(self.translated_image_path)

                    self.setInfo.emit('Image Translated & Saved, Notice any mistakes? Rescan an area using the Area Scanner.', COLOR_SUCCESS)
                    self.finish_signal.emit(self.translation_mode, self.translated_image_path)

                case 1:  # 1: Scanner Mode, Takes in Selected Cropped Original Image, scans selected area, translates, edits, and saves area onto image. (if it already exists, paste it in, if not, create and paste it in)
                    cropped_pil_image = original_pil_image.crop((self.x0, self.y0, self.x1, self.y1))
                    bubbles = self.read_image(cropped_pil_image)

                    self.setInfo.emit(f"[{self.og_image_name}] Translating sentences from {self.language_from} to {self.language_to} using {self.translator}...", COLOR_INFO)
                    original_sentences, translated_sentences = self.translate_text(bubbles)

                    self.setInfo.emit(f'[{self.og_image_name}] Clearing original text and replacing with translated text using font "{self.font_name}"...', COLOR_INFO)
                    edited_cropped_pil_image = self.edit_image(cropped_pil_image, bubbles, original_sentences, translated_sentences)

                    self.setInfo.emit(f'[{self.og_image_name}] Saving changes...', COLOR_INFO)
                    if not self.translated_image_path:
                        self.translated_image_path = self.prep_image_path(extension_suffix=self.extension_suffix, original_name=self.original_name, language_from=self.language_from, language_to=self.language_to, translator=self.translator)
                        original_pil_image.save(self.translated_image_path)
                    translated_pil_image = Image.open(self.translated_image_path)
                    translated_pil_image.paste(edited_cropped_pil_image, (self.x0, self.y0))
                    translated_pil_image.save(self.translated_image_path)

                    self.setInfo.emit('Selected Area Translated & Saved.', COLOR_SUCCESS)
                    self.finish_signal.emit(self.translation_mode, self.translated_image_path)

                case 2:  # 2: Eraser Mode, Same as above, but instead of translating text, it removes them.
                    cropped_pil_image = original_pil_image.crop((self.x0, self.y0, self.x1, self.y1))
                    bubbles = self.read_image(cropped_pil_image)

                    self.setInfo.emit(f'[{self.og_image_name}] Gathering text to remove...', COLOR_INFO)
                    original_sentences, empty_sentences = self.gather_text(bubbles)

                    self.setInfo.emit(f'[{self.og_image_name}] Removing found text...', COLOR_INFO)
                    edited_cropped_pil_image = self.edit_image(cropped_pil_image, bubbles, original_sentences, empty_sentences)

                    self.setInfo.emit(f'[{self.og_image_name}] Saving changes...', COLOR_INFO)
                    if not self.translated_image_path:
                        self.translated_image_path = self.prep_image_path(extension_suffix=self.extension_suffix, original_name=self.original_name, language_from=self.language_from, language_to=self.language_to, translator=self.translator)
                        original_pil_image.save(self.translated_image_path)
                    translated_pil_image = Image.open(self.translated_image_path)
                    translated_pil_image.paste(edited_cropped_pil_image, (self.x0, self.y0))
                    translated_pil_image.save(self.translated_image_path)

                    self.setInfo.emit("Selected Area's Text Removed.", COLOR_SUCCESS)
                    self.finish_signal.emit(self.translation_mode, self.translated_image_path)

        except Exception as e:
            print(f"Error in run: {e}")
            self.setInfo.emit(f"[ERROR]: ({e}), please try again or use 'Area Scanner'", COLOR_ERROR)
            self.finish_signal.emit(self.translation_mode, None)

    def load_data(self):
        self.config = ConfigParser()
        self.config.read(self.main.config_file_path)

        self.og_image_name = os.path.basename(self.og_image_path)

        self.extension_suffix = os.path.splitext(self.og_image_path)[1]
        self.original_name = os.path.basename(self.og_image_path).split(self.extension_suffix)[0]

        self.translator = 'Google' if self.main.ui.google_radio_button.isChecked() else 'DeepL'

        self.save_location = self.config.get('General', 'Save location', fallback=os.getcwd())
        self.save_as_name = self.config.get('General', 'Save as', fallback=None)
        self.dump_translation = self.config.getboolean('General', 'Auto dump translations', fallback=False)
        self.language_from = self.config.get('General', 'Last used language from', fallback='Auto')
        self.language_to = self.config.get('General', 'Last used Language to', fallback='English')

        if not self.config.getboolean('Settings', 'Auto text color', fallback=True):
            self.text_color = tuple(
                map(int, self.config.get('Settings', 'Text color', fallback='(0, 0, 0)').strip('()').split(',')))

        if not self.config.getboolean('Settings', 'Auto background color', fallback=True):
            self.background_color = tuple(map(int, self.config.get('Settings', 'Background color',
                                                                   fallback='(255, 255, 255)').strip('()').split(',')))

        self.OCR_languages = self.main.tesstraineddata
        fonts_folder = self.main.fonts_dir

        for font in self.config['Fonts']:
            if self.config.getboolean('Fonts', font, fallback=False):
                self.font_name = font
                break

        for file in os.listdir(fonts_folder):
            file = file.lower()
            if file.startswith(self.font_name) and (file.endswith('.ttf') or file.endswith('.otf')):
                self.font_path = os.path.join(fonts_folder, file)
                break

    def read_image(self, pil_image):
        image_data = self.tesseract_read_image(pil_image)
        bubbles = self.group_text_by_bubbles(image_data)
        self.print_detailed_image_data(image_data)  # FOR DEBUGGING PURPOSES
        return bubbles

    def edit_image(self, pil_image, bubbles, original_sentences, translated_sentences):
        self.drawing = ImageDraw.Draw(pil_image)
        self.width, self.height = pil_image.size
        self._dummy_image = Image.new('RGB', (1, 1), (255, 255, 255))  # To use for textsize width/height calculations
        self._dummy_draw = ImageDraw.Draw(self._dummy_image)

        for nth_bubble, bubble in enumerate(bubbles):
            block_num = bubble['block_num']
            current_translated_sentence = translated_sentences[nth_bubble]
            spacing = bubble['lines'][1]['bbox'][1] - bubble['lines'][0]['bbox'][
                3] if len(bubble['lines']) > 1 else 10
            ordered_colors = []

            line_start_positions = [line['bbox'][0] for line in bubble['lines']]
            line_end_positions = [line['bbox'][2] for line in bubble['lines']]
            line_y_start_positions = [line['bbox'][1] for line in bubble['lines']]
            line_y_end_positions = [line['bbox'][3] for line in bubble['lines']]
            current_original_sentence = original_sentences[nth_bubble]
            for nth_line, line in enumerate(bubble['lines']):  # Iterate through each line in the bubble
                bbox = line['bbox']  # Bounding box for the line
                text = line['text']  # Text content of the line

                try:
                    first_word_bbox = line['words'][0]['bbox']
                    space_bbox = (first_word_bbox[0] - 5, first_word_bbox[1], first_word_bbox[0], first_word_bbox[3])  # Small space behind the first word
                    background_color, text_color = self.get_bg_and_text_color(pil_image, bbox, space_bbox)  # Extracts color from space_bbox, which is background color, subtracts the space_bbox colors from bbox colors, whatever's left is text_color
                    print(
                        f"\nBlock | Line Number: {block_num} | {nth_line + 1} \nFull untranslated bubble: {current_original_sentence} \n"
                        f"Full translated bubble: {current_translated_sentence} \nCurrent line {text}")
                    if self.background_color:
                        background_color = self.background_color
                    if self.text_color:
                        text_color = self.text_color
                    self.draw_background_on_line(bbox, spacing, background_color)  # Overwrite bbox line with background color
                    ordered_colors.append(text_color)  # Save the text_color to use later when drawing the text
                except Exception as e:
                    print("Error in drawing background: ", e)
                    continue
            for nth_line, line in enumerate(bubble['lines']):
                try:
                    lines_count = len(bubble['lines'])
                    bbox = line['bbox']
                    current_line_width = (line_end_positions[nth_line] - line_start_positions[nth_line])
                    # current_line_height = (line_y_end_positions[nth_line] - line_y_start_positions[nth_line])
                    center_width_point = (line_start_positions[nth_line] + (current_line_width / 2))
                    line_height_average = (sum(line_y_end_positions) - sum(line_y_start_positions)) // len(line_y_start_positions)
                    font_size = self.calculate_max_font_size(current_original_sentence, line_height_average)  # Maximum possible allowed font size, determined by average line height

                    total_lines = len(bubble['lines'])
                    is_first_line = (nth_line == 0)
                    is_last_line = (nth_line == total_lines - 1)
                    # Now wrap the full bubble translated sentence text in line, Draw words that fit, and save words that don't fit for the next line iteration loop
                    current_translated_sentence, next_iteration_text = self.wrap_text(current_translated_sentence, font_size, is_last_line, is_first_line, current_line_width)
                    current_line_text_width = self.textsize(current_translated_sentence, font_size)[0]

                    if self.language_to == 'Arabic':
                        current_translated_sentence = get_display(arabic_reshaper.reshape(current_translated_sentence))  # Correct & reshape for RTL arabic
                        text_x = center_width_point - (current_line_text_width // 2) + 25  # I still don't know why arabic (and only arabic) needs this extra 25, without it, text looks misplaced
                        text_y = bbox[1] - (line_height_average // 2)
                    else:
                        text_x = center_width_point - (current_line_text_width // 2)
                        text_y = bbox[1]

                    font = ImageFont.truetype(self.font_path, font_size)
                    text_color = ordered_colors[nth_line]
                    print(f"Text: {current_translated_sentence}, Font size: {font_size}, Color: {text_color}")
                    self.drawing.text((text_x, text_y), current_translated_sentence, fill=text_color, font=font)
                    current_translated_sentence = next_iteration_text if next_iteration_text else None
                    if next_iteration_text and lines_count == nth_line + 1:  # Case where the translated text is longer than original and thus there are leftover text after lines are done
                        next_line_width = self.textsize(next_iteration_text, font_size)[0]
                        if self.language_to == 'Arabic':
                            next_iteration_text = get_display(arabic_reshaper.reshape(next_iteration_text))
                            next_nth_line_x = center_width_point - (next_line_width // 2) + 25
                            next_nth_line_y = bbox[3] - (line_height_average // 2)
                        else:
                            next_nth_line_x = center_width_point - (next_line_width // 2)
                            next_nth_line_y = bbox[3]
                        next_nth_line_y += spacing
                        self.drawing.text((next_nth_line_x, next_nth_line_y), next_iteration_text, font=font, fill=text_color)
                    elif not next_iteration_text and lines_count > nth_line + 1:  # Case where there's no more translated text but lines are leftover
                        break
                except Exception as e:
                    print("Error in line", e)
                    continue
        return pil_image

    def prep_image_path(self, **kwargs):
        if self.save_as_name:
            image_name = self.save_as_name.format(**kwargs)  # What could possibly go wrong?
        else:
            image_name = f"{self.original_name}_{self.language_to}{self.extension_suffix}"
        image_path = os.path.join(self.save_location, image_name)
        return image_path

    def print_detailed_image_data(self, image_data):
        for i in range(len(image_data['text'])):
            if image_data['text'][i]:
                details = {key: image_data[key][i] for key in image_data}
                print(details)

    def tesseract_read_image(self, pil_image):
        try:
            tesseract_exe_path = self.config.get('General', 'Tesseract exe location')
            tessdata_path = os.path.join(os.path.dirname(tesseract_exe_path), 'tessdata')
            pytesseract.pytesseract.tesseract_cmd = tesseract_exe_path
            os.environ['TESSDATA_PREFIX'] = tessdata_path

            gray_image = pil_image.convert("L")
            enhanced_image = ImageOps.autocontrast(gray_image)

            image_data = pytesseract.image_to_data(enhanced_image, lang=self.OCR_languages,
                                                   output_type=pytesseract.Output.DICT)
            return image_data
        except Exception as e:
            print(f"Error in tesseract_read_image: \n{e}")

    def draw_background_on_line(self, bbox, spacing, background_color):
        try:
            offset = int(spacing // 2)
            # offsets, so we do not go outside image boundaries
            left_offset = min(offset, bbox[0])
            top_offset = min(offset, bbox[1])
            right_offset = min(offset, self.width - bbox[2] - 1)
            bottom_offset = min(offset, self.height - bbox[3] - 1)
            bigger_bubble_box = (
                max(bbox[0] - left_offset, 0),  # Left edge
                max(bbox[1] - top_offset, 0),  # Top edge
                min(bbox[2] + right_offset, self.width),  # Right edge
                min(bbox[3] + bottom_offset, self.height)  # Bottom edge
            )
            self.drawing.rectangle(bigger_bubble_box, fill=background_color)
        except Exception as e:
            print(f"Error in draw_background_on_line: \n{e}")

    @lru_cache()
    def get_font(self, font_size):
        """Load and cache the font to avoid reloading this specific font_size every time it is needed."""
        return ImageFont.truetype(self.font_path, font_size)

    def textsize(self, text, font_size):
        """Calculate text size dynamically based on text and font size."""
        font = ImageFont.truetype(self.font_path, font_size)
        _, _, width, height = self._dummy_draw.textbbox((0, 0), text=text, font=font)
        return width, height

    def calculate_max_font_size(self, text, max_height, max_font_size=50):
        font_size = max_font_size
        text_width, text_height = self.textsize(text, font_size)
        while text_height >= max_height:
            font_size -= 1
            if font_size < 1:
                font_size = 2
                break
            text_width, text_height = self.textsize(text, font_size)
        if self.language_to in ['Arabic', 'Korean']:  # Workaround
            font_size += 15
        elif self.language_to in ['Japanese']:
            font_size += 5
        return font_size

    def wrap_text(self, text, font_size, is_last_line, is_first_line, max_width):
        try:
            if self.language_to in ['Japanese', 'Thai']:
                words = list(text)  # Character-based splitting, For languages like Japanese & Chinese
            else:
                words = text.split()  # Word-based splitting, for languages like English & Arabic
            current_line = ""
            base_multiplier = 2.5
            slope = 0.005
            min_multiplier = 1.1
            overflow_threshold = int(max_width * max(base_multiplier - (slope * max_width), min_multiplier))

            for word in words:
                if self.language_to in ['Japanese', 'Thai']:
                    test_line = f"{current_line}{word}".strip()
                else:
                    test_line = f"{current_line} {word}".strip() if current_line else word
                if self.textsize(test_line, font_size)[0] <= max_width:
                    current_line = test_line
                else:
                    if self.textsize(test_line, font_size)[0] <= overflow_threshold:
                        current_line = test_line
                    elif current_line == "":
                        if is_last_line or is_first_line:
                            current_line = test_line
                    next_iteration_text = text.replace(current_line, "", 1)
                    return current_line, next_iteration_text
            return current_line, ""
        except Exception as e:
            print(f"Error in wrap_text: {e}")

    def get_bg_and_text_color(self, pil_image, bbox, space_bbox, similarity_threshold=30):
        pil_image = pil_image.convert('RGB')
        image = pil_image.crop(space_bbox)
        pixels = list(image.getdata())

        # Get the most common background color
        color_counts = {}
        for color in pixels:
            color_counts[color] = color_counts.get(color, 0) + 1

        background_color = max(color_counts, key=color_counts.get)

        # Now look for the text color in the bbox (entire area)
        image = pil_image.crop(bbox)
        pixels = list(image.getdata())

        # Filter out colors similar to the background color
        def color_distance(c1, c2):
            return sum(abs(a - b) for a, b in zip(c1, c2))

        filtered_colors = [color for color in pixels if color_distance(color, background_color) > similarity_threshold]

        # Count remaining colors and pick the most frequent as the text color
        color_counts = {}
        for color in filtered_colors:
            color_counts[color] = color_counts.get(color, 0) + 1

        if color_counts:
            text_color = max(color_counts, key=color_counts.get)
        else:
            # Fallback if no color is found (unlikely but safe)
            text_color = (0, 0, 0)  # Default to black

        return background_color, text_color

    def average_color(self, colors):
        """ Calculate the average color of a list of colors """
        return tuple(sum(c) // len(colors) for c in zip(*colors))

    def is_similar(self, colors, threshold):
        """ Check if a list of colors is similar to the average color of a list of colors """
        avg_color = tuple(sum(c) // len(colors) for c in zip(*colors))
        return all(self.color_similarity(avg_color, color) < threshold for color in colors)

    def color_similarity(self, color1, color2):
        """ Calculate the euclidean distance between two colors """
        return sum((a - b) ** 2 for a, b in zip(color1, color2)) ** 0.5

    def translate_text(self, bubbles):
        try:
            sentences_to_translate = [' '.join([line['text'] for line in self.sort_lines_by_position(bubble)['lines']])
                                      for bubble in bubbles]

            translated_sentences = []
            langfrom = LANGUAGE_CODES.get(self.language_from.lower(), 'auto')
            langto = LANGUAGE_CODES.get(self.language_to.lower())
            if self.translator == 'Google':
                for sentence in sentences_to_translate:
                        translated_sentence = self.google_translate(sentence, langfrom, langto)
                        translated_sentences.append(translated_sentence)
            else:
                translated_sentences = self.deepl_translate(sentences_to_translate, langfrom, langto)

            return sentences_to_translate, translated_sentences
        except Exception as e:
            print(f"Error in translate_text: {e}")
            return [], []

    def gather_text(self, bubbles):
        try:
            sentences = [' '.join([line['text'] for line in self.sort_lines_by_position(bubble)['lines']]) for bubble in
                         bubbles]

            # Create an empty string for each sentence (for the eraser tool)
            empty_sentences = ['' for _ in sentences]

            return sentences, empty_sentences
        except Exception as e:
            print(f"Error gathering text: {e}")
            return [], []

    def google_translate(self, text_to_translate, source_language='auto', target_language='en'):
        try:
            translated_sentence = GoogleTranslator(source=source_language, target=target_language).translate(
                text_to_translate)
            return translated_sentence
        except Exception as e:
            print(f"Error google translating sentence: {e}")
            return ''

    def deepl_translate(self, sentences, source_language='auto', target_language='en', driver_type='Chrome'):  # we have DeepL at home! DeepL at home:
        try:
            if source_language not in DEEPL_LANGUAGES or target_language not in DEEPL_LANGUAGES:
                return "Invalid language, please retry"

            if driver_type == 'Chrome':
                options = webdriver.ChromeOptions()
                options.add_argument('--headless')
                driver = webdriver.Chrome(options=options)
            else:
                options = webdriver.FirefoxOptions()
                options.add_argument('--headless')
                driver = webdriver.Firefox(options=options)

            translated_sentences = []

            for sentence in sentences:
                if len(sentence) > 1500:
                    print(f"Text exceeds 1500 characters, skipping: {sentence[:50]}...")
                    translated_sentences.append('')
                    continue

                text_to_translate_url = sentence.replace(" ", "%20").replace("\n", "%0A")
                website = f"https://www.deepl.com/translator#{source_language}/{target_language}/{text_to_translate_url}"

                driver.get(website)

                try:
                    translated_sentence = WebDriverWait(driver, 20).until(
                        lambda driver: driver.find_element(By.XPATH,
                                                           f'//*[@id="textareasContainer"]/div[3]/section/div[1]/d-textarea/div/p/span[1]')).text
                    print(f'{sentence} -> {translated_sentence}')
                    translated_sentences.append(translated_sentence)
                except Exception as e:
                    print(f"Error fetching translation for '{sentence}': {e}")
                    translated_sentences.append('')
            driver.quit()
            return translated_sentences

        except Exception as e:
            print(f"Error in deepl_translate: {e}")
            return ['' for _ in sentences]

    def sort_lines_by_position(self, bubble):
        """ Sort lines in each bubble based on the top y-coordinate of their bounding box """
        bubble['lines'].sort(key=lambda line: line['bbox'][1])
        return bubble

    # def prepare_sentences(self, sentences):
    #     formatted_sentences = []
    #     for sentence in sentences:
    #         if sentence and not sentence[0].isupper():
    #             sentence = sentence.capitalize()
    #
    #         if not sentence.endswith(('.', "!", "?", ";", "'", '"')):
    #             sentence += '.'
    #
    #         formatted_sentences.append(sentence)
    #     return formatted_sentences

    def group_text_by_bubbles(self, data):  # ¯\_(ツ)_/¯
        # Organize data by lines, accounting for character-based languages
        lines = {}  # {(block_num, par_num, line_num): {'bbox': [left, top, right, bottom], 'text': [], 'words': []}}
        for i, text in enumerate(data['text']):
            if float(data['conf'][i]) >= 50 and text.strip():
                block_num = data['block_num'][i]
                par_num = data['par_num'][i]
                line_num = data['line_num'][i]

                left, top, width, height = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
                right, bottom = left + width, top + height

                word_bbox = [left, top, right, bottom]  # Bounding box for the individual word/character

                key = (block_num, par_num, line_num)
                if key not in lines:
                    lines[key] = {'bbox': [left, top, right, bottom], 'text': [text],
                                  'words': [{'text': text, 'bbox': word_bbox}]}
                else:
                    line = lines[key]
                    line['bbox'] = [
                        min(line['bbox'][0], left),
                        min(line['bbox'][1], top),
                        max(line['bbox'][2], right),
                        max(line['bbox'][3], bottom),
                    ]
                    line['text'].append(text)
                    line['words'].append({'text': text, 'bbox': word_bbox})  # Add individual word

        # Group lines into bubbles based on block_num
        bubbles = {}
        for key, line in lines.items():
            block_num = key[0]
            if block_num not in bubbles:
                bubbles[block_num] = {'block_num': block_num, 'lines': []}
            bubbles[block_num]['lines'].append((key[1], key[2], line))  # Include par_num and line_num for sorting

        # Sort lines within each bubble by par_num, then line_num
        for bubble in bubbles.values():
            bubble['lines'].sort(key=lambda x: (x[0], x[1]))  # Sort by par_num then line_num
            bubble['lines'] = [line[2] for line in bubble['lines']]  # Remove the sorting keys

        bubbles_list = list(bubbles.values())

        for bubble in bubbles_list:
            for line in bubble['lines']:
                if self.language_from in ['Japanese', 'Chinese']:
                    line['text'] = ''.join([word['text'] for word in line['words']])  # Join characters for character-based languages
                else:
                    line['text'] = ' '.join([word['text'] for word in line['words']])  # Join words with spaces for word-based languages

        return bubbles_list

