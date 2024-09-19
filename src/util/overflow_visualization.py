# Copyright (C) 2024 Yousef A. (Vyoxa).
# Licensed under the GPL-3.0 License.
# Created for KiraYume: https://github.com/Vyoxa/KiraYume

from PIL import Image, ImageDraw, ImageFont

def create_visualization():
    base_multiplier = 2.5
    slope = 0.005
    min_multiplier = 1.1

    # Image size and properties
    width, height = 960, 2080
    bar_height = 15
    vertical_margin = 5
    horizontal_margin = 2
    patch_margin = 30

    sample_text = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"

    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)

    font_path = "arial.ttf"
    font_size = 12

    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    # Helper function to calculate text size
    def textsize(text, font_path, font_size):
        im = Image.new('RGB', (0, 0), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(font_path, font_size)
        _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
        im.close()
        return width, height

    y = vertical_margin

    # Add the legend at the top-right corner
    def add_legend():
        # Right-top corner positioning
        legend_start_x = width - 500
        legend_start_y = vertical_margin

        legend_items = [
            ("Black (Normal line width):", 'black', "This is how many words fit in the line without overflow."),
            ("Red (Overfilled line):", 'red', "Showcases what happens when you try to add an extra word that doesn’t fit."),
            (
            "Blue (With overflow allowance):", 'blue', "This is how many words fit in the line with overflow.")
        ]

        rect_size = 15
        text_offset = rect_size + 10

        for label, color, description in legend_items:
            draw.rectangle([legend_start_x, legend_start_y, legend_start_x + rect_size, legend_start_y + rect_size],
                           fill=color)
            draw.text((legend_start_x + text_offset, legend_start_y), label, fill='black', font=font)
            draw.text((legend_start_x + text_offset, legend_start_y + rect_size), description, fill='black', font=font)

            # Move y down for the next legend item
            legend_start_y += rect_size + vertical_margin * 4
    add_legend()

    # Helper function to check if a word fits in the line
    def does_word_fit(current_line, word, max_width):
        test_line = current_line + " " + word if current_line else word
        text_width, _ = textsize(test_line, font_path, font_size)
        return text_width <= max_width

    # Helper function to draw text in the center
    def draw_centered_text(text, font, x_start, x_end, y_start, y_end):
        text_width, text_height = textsize(text, font_path, font_size)
        x_center = (x_end + x_start - text_width) / 2
        y_center = (y_end + y_start - text_height) / 2
        draw.text((x_center, y_center), text, fill='black', font=font)

    # Loop through different max_width values
    for max_width in range(20, 401, 20):
        multiplier = max(base_multiplier - (slope * max_width), min_multiplier)
        allowance = max_width * multiplier - max_width

        print(f"max_width: {max_width}, Multiplier: {multiplier:.2f}, Allowance: {allowance:.2f}")

        words = sample_text.split()

        ## FIRST LINE: Black rectangle with max_width
        # Draw the black rectangle (max_width)
        draw.rectangle([horizontal_margin, y, horizontal_margin + max_width, y + bar_height], outline='black', fill=None)

        # Draw text for the max_width only (black rectangle)
        current_line = ""
        for word in words:
            if does_word_fit(current_line, word, max_width):
                current_line += " " + word if current_line else word
            else:
                break

        needed_width, _ = textsize(current_line, font_path, font_size)
        draw_centered_text(current_line, font, horizontal_margin, horizontal_margin + max_width, y, y + bar_height)
        draw.text((horizontal_margin + max_width + 100, y), f"Needed Width: {needed_width} | Available Width: {max_width}", fill='black', font=font)

        y += bar_height + vertical_margin  # Move y for the next line

        ## SECOND LINE: Red rectangle with extra word that doesn't fit (max_width)
        # Draw the red rectangle (same max_width as the black one)
        draw.rectangle([horizontal_margin, y, horizontal_margin + max_width, y + bar_height], outline='red', fill=None)

        # Draw text for the max_width with one extra word (red rectangle)
        current_line_with_extra = ""
        for word in words:
            if does_word_fit(current_line_with_extra, word, max_width):
                current_line_with_extra += " " + word if current_line_with_extra else word
            else:
                # Add one extra word that doesn't fit and then break
                current_line_with_extra += " " + word
                break

        needed_width, _ = textsize(current_line_with_extra, font_path, font_size)
        draw.text((horizontal_margin, y), current_line_with_extra, fill='black', font=font)
        draw.text((horizontal_margin + max_width + 100, y), f"Needed Width: {needed_width} | Available Width: {max_width}", fill='black', font=font)

        y += bar_height + vertical_margin  # Move y for the next line

        ## THIRD LINE: Blue rectangle with overflow allowance (max_width + allowance)
        # Draw the filled blue rectangle only for the overflow portion (max_width to max_width + allowance)
        draw.rectangle([horizontal_margin + max_width, y, horizontal_margin + max_width + allowance, y + bar_height], outline='blue', fill='blue')

        # Draw the outline for the entire (max_width + allowance) rectangle
        draw.rectangle([horizontal_margin, y, horizontal_margin + max_width + allowance, y + bar_height], outline='blue', fill=None)

        # Draw text for the max_width + allowance (blue rectangle)
        current_line_with_overflow = ""
        for word in words:
            if does_word_fit(current_line_with_overflow, word, max_width + allowance):
                current_line_with_overflow += " " + word if current_line_with_overflow else word
            else:
                break

        needed_width, _ = textsize(current_line_with_overflow, font_path, font_size)
        draw_centered_text(current_line_with_overflow, font, horizontal_margin, horizontal_margin + max_width + allowance, y, y + bar_height)
        draw.text((horizontal_margin + max_width + 100, y), f"Needed Width: {needed_width} | Available Width: {int(max_width + allowance)}", fill='black', font=font)

        # Update the y position for the next set of rectangles and text
        y += bar_height + patch_margin  # Extra space after the patch of three lines

    img.show()
    # img.save('visualization.png')


create_visualization()