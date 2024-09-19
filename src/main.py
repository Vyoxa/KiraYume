# Copyright (C) 2024 Yousef A. (Vyoxa).
# Licensed under the GPL-3.0 License.
# Created for KiraYume: https://github.com/Vyoxa/KiraYume

import os
import shutil
import socket
import sys
import configparser
import appdirs

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt6.QtWidgets import *

from core.TranslationWorker import TranslationWorker
from core.SettingsWidget import SettingsWidget
from core.TesseractSettingsWidget import TesseractSettingsWidget
from core.FileViewerDelegate import FileViewerDelegate
from core.KiraYumeCreditsWidget import KiraYumeCreditsWidget
from pyui.MainWindow import Ui_MainWindow

from core.Constants import (PROGRAM_VERSION, LANGUAGES_FROM, LANGUAGES_TO,
                            ITEM_PATH_ROLE, TRANSLATED_ITEM_PATH_ROLE,
                            COLOR_FOLDER, COLOR_INFO, COLOR_SUCCESS, COLOR_ERROR, COLOR_DEFAULT_TEXT,
                            SCANNER_BUTTON_OFF_STYLE_SHEET, SCANNER_BUTTON_ON_STYLE_SHEET,
                            ERASER_BUTTON_ON_STYLE_SHEET, ERASER_BUTTON_OFF_STYLE_SHEET,
                            TESSERACT_CONNECTED_STYLE_SHEET, TESSERACT_DISCONNECTED_STYLE_SHEET)

# TODO: Improve tesseract's scanning capabilities somehow, currently subpar at detecting manga and is ok at manhwa
# TODO: Create a console log that shows the user what the program is doing behind the scenes
# TODO: Add a reload button next to folders in item tree to reload files, so users don't have to re-import it to update its contents
# TODO: Add hints to each setting in SettingsWidget UI to explain what they do in detail.
# TODO: It is probably for the best to put the text font options under the main window options instead of Settings for quicker easier access, not sure.
# TODO: How about an actual API for DeepL?
# TODO: Work on Dump translation into .txt file option in settings
# TODO: Better error handling for translation worker for sudden error interruptions
# TODO: Add more languages to translate from/to
# TODO: Make a README.md

# Known Problems:
#
# when language_from is Japanese, it outs entire page's read sentences as one line, thus counting as one bubble, meaning only Area Scanner works with it right now
#
# When Thai is passed to wrap_text, sometimes breaks and repeats the same line over and over
#
# Some languages are by default too small (Arabic, Korean so far) and thus have +15px added to compensate, Not sure why or how to fix, something about different width to height ratios maybe?

# DeepL can't translate when languagefrom and languageto are the same languages, it simply doesn't accept them and changes translate_to, This is from DeepL's side and probably can't be fixed, Google's works as intended

# Program automatically overwrites when the image name is the same, Could make a safety mechanism that asks the user if they wish to edit name or continue anyway

# OCR Quite often reads ! as /, I'm guessing because AnimeAce (most common) font's ! looks like a /


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(self.resource_path('assets', 'AppIcon128.png')))
        self.setWindowTitle("KiraYume")
        self.setInfo(f"Welcome to KiraYume v{PROGRAM_VERSION}")
        self.setGeometry(0, 0, 1100, 700)
        self.centerWindow()


        self.translation_worker = None
        self.scrollbar_position = None
        self.tesstraineddata = None
        self.currently_selected_item = (None, None)  # (itempath, translated_itempath) Updated when user selects an item from file tree
        self.scanner_mode = False
        self.eraser_mode = False

        self.connect_UI()

        self.init_config()
        self.KiraYumeCredits_widget = KiraYumeCreditsWidget(self)
        self.settings_widget = SettingsWidget(self)
        self.tesseract_widget = TesseractSettingsWidget(self)
        self.init_data()

    def resizeEvent(self, event):
        try:
            super(Main, self).resizeEvent(event)
            if self.ui.ImageViewerORIGINAL.sceneRect():
                self.ui.ImageViewerORIGINAL.ratio_mode(self.current_ratio_mode)
            if self.ui.ImageViewerTRANSLATED.sceneRect():
                self.ui.ImageViewerTRANSLATED.ratio_mode(self.current_ratio_mode)
        except Exception as e:
            print(e)

    def centerWindow(self) -> None:
        # Fetch screen dimensions
        screen = QApplication.primaryScreen().geometry()
        # Calculate the center position
        x = (screen.width() - self.width()) / 2
        y = (screen.height() - self.height()) / 2 - 50
        # Move the window to the center
        self.move(int(x), int(y))

    def resource_path(self, resource_folder, resource_name):
        """Get the absolute path to the resource in the bundled app."""
        if getattr(sys, 'frozen', False):
            # If the application is running in a bundle
            base_path = sys._MEIPASS
        else:
            # If running normally, fetch from the source code location
            base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        return os.path.join(base_path, resource_folder, resource_name)

    def connect_UI(self) -> None:
        self.ui.KiraYumeCredits_button.setIcon(QIcon(self.resource_path("assets", "AppIcon128.png")))
        self.ui.settings_button.setIcon(QIcon(self.resource_path("assets", "Settings125.png")))
        self.ui.tess_settings_button.setIcon(QIcon(self.resource_path("assets", "TesseractSettings128.png")))

        self.model = QStandardItemModel()
        self.ui.selection_tree_UI.setModel(self.model)
        self.ui.selection_tree_UI.setItemDelegate(FileViewerDelegate(self.ui.selection_tree_UI, self))
        self.ui.selection_tree_UI.clicked.connect(self.on_item_selection_changed)

        self.ui.KiraYumeCredits_button.clicked.connect(self.KiraYumeCredits_button_clicked)

        self.ui.import_file_button.clicked.connect(self.import_file_button_clicked)

        self.ui.import_image_button.clicked.connect(self.ImportImage)

        self.ui.import_folder_button.clicked.connect(self.ImportFolder)

        self.ui.settings_button.clicked.connect(self.settings_button_clicked)

        self.ui.translate_button.clicked.connect(self.scan_everything)

        self.ui.scanner_button.clicked.connect(self.scanner_button_clicked)

        self.ui.eraser_button.clicked.connect(self.eraser_button_clicked)

        self.ui.language_to_combobox.currentTextChanged.connect(self.languageto_changed)
        self.ui.language_from_combobox.currentTextChanged.connect(self.languagefrom_changed)

        self.ui.deepl_radio_button.toggled.connect(self.translator_changed)

        self.ui.tess_settings_button.clicked.connect(self.tess_settings_button_clicked)

    def init_config(self):
        config_dir = appdirs.user_config_dir("KiraYume", False)
        os.makedirs(config_dir, exist_ok=True)
        self.config_file_path = os.path.join(config_dir, 'settings.ini')
        self.config = configparser.ConfigParser()
        self.cwd = os.getcwd()

        self.fonts_dir = os.path.join(config_dir, 'fonts')
        os.makedirs(self.fonts_dir, exist_ok=True)

        default_fonts = ['NotoSans-Bold.ttf', 'NotoSansJP-Bold.ttf', 'NotoSansKR-Bold.ttf', 'NotoNaskhArabic-Bold.ttf', 'NotoSansThai-Bold.ttf']

        for font in default_fonts:
            font_source = self.resource_path('fonts', font)
            font_dest = os.path.join(self.fonts_dir, font)

            if not os.path.exists(font_dest):
                shutil.copyfile(font_source, font_dest)

        if not os.path.isfile(self.config_file_path):
            self.config['General'] = {
                'Save location': self.cwd,
                'Save as': '{original_name}_{language_to}{extension_suffix}',
                'Ratio mode': 'Maintain Aspect Ratio, Expand to Fit',
                # 'Auto sync scroller': 'True',
                # 'Auto dump translations': 'False',
                'Auto import current directory': 'False',
                'Last used language from': 'Auto',
                'Last used language to': 'English',
                'Last used translator': 'Google'
            }
            self.config['Settings'] = {
                'Text color': '000, 000, 000',
                'Background color': '255, 255, 255',
                'Auto text color': 'True',
                'Auto background color': 'True'
            }
            self.config['TrainedData'] = {
                'eng': 'True'
            }
            self.config['Fonts'] = {
                'NotoSans-Bold.ttf': 'True',
                'NotoSansJP-Bold.ttf': 'False',
                'NotoSansKR-Bold.ttf': 'False',
                'NotoNaskhArabic-Bold.ttf': 'False',
                'NotoSansThai-Bold.ttf': 'False'

            }
            with open(self.config_file_path, 'w') as configfile:
                self.config.write(configfile)
        self.config.read(self.config_file_path)

        if not self.config.has_option('General', 'Tesseract exe location'):
            self.check_default_exe_path()
        else:
            path = os.path.join(self.config['General']['Tesseract exe location'])  # Check if it has been moved/removed, if so, remove wrong location
            if not os.path.exists(path) or os.path.basename(path) != 'tesseract.exe':
                self.config['General'].pop('Tesseract exe location')
                self.check_default_exe_path()
        self.update_tess_activity()
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)


    def check_default_exe_path(self):
        default_exe_path = os.path.join(self.cwd, 'Tesseract-OCR', 'tesseract.exe')  # Check default location, aka in the same folder as the program
        if os.path.exists(default_exe_path):
            self.config['General']['Tesseract exe location'] = default_exe_path

    def update_tess_activity(self):
        if self.config.has_option('General', 'Tesseract exe location'):
            self.ui.tess_activity.setStyleSheet(TESSERACT_CONNECTED_STYLE_SHEET)
            self.ui.tess_activity.setToolTip('Tesseract-OCR Connected.')
        else:
            self.ui.tess_activity.setStyleSheet(TESSERACT_DISCONNECTED_STYLE_SHEET)
            self.ui.tess_activity.setToolTip('Tesseract-OCR Disconnected')


    def init_data(self) -> None:
        self.current_ratio_mode = self.config.get('General', 'Ratio mode',
                                                  fallback="Maintain Aspect Ratio, Expand to Fit")

        self.ui.ImageViewerORIGINAL.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.ImageViewerTRANSLATED.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.ImageViewerORIGINAL.setVerticalScrollBar(self.ui.SyncSB)
        self.ui.ImageViewerTRANSLATED.setVerticalScrollBar(self.ui.SyncSB)
        self.ui.ImageViewerORIGINAL.main = self

        if self.config['General']['Auto import current directory'] == 'True':
            self.ImportFolder(self.cwd)
        self.ui.import_folder_button.hide()
        self.ui.import_image_button.hide()
        last_used_languagefrom = self.config.get('General', 'Last used language from', fallback='Auto')
        languagesfrom = LANGUAGES_FROM
        languagesfrom.remove(last_used_languagefrom)
        self.ui.language_from_combobox.addItems([last_used_languagefrom] + languagesfrom)

        last_used_languageto = self.config.get('General', 'Last used language to', fallback='English')
        languagesto = LANGUAGES_TO
        languagesto.remove(last_used_languageto)
        self.ui.language_to_combobox.addItems([last_used_languageto] + languagesto)

        self.ui.google_radio_button.setChecked(True) if self.config.get('General', 'Last used translator', fallback='Google') == 'Google' else self.ui.deepl_radio_button.setChecked(True)

        if 'TrainedData' not in self.config.sections():
            self.config['TrainedData'] = {}
            with open(self.config_file_path, 'w') as configfile:
                self.config.write(configfile)

        self.tesseract_widget.check_exe_path()
        self.tesseract_widget.exit_button_clicked()

    def languagefrom_changed(self, text) -> None:
        self.config.read(self.config_file_path)
        self.config['General']['Last used language from'] = text
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)

    def languageto_changed(self, text) -> None:
        self.config.read(self.config_file_path)
        self.config['General']['Last used Language to'] = text
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)

    def KiraYumeCredits_button_clicked(self) -> None:
        if self.KiraYumeCredits_widget.isVisible():
            self.KiraYumeCredits_widget.hide()
        else:
            self.KiraYumeCredits_widget.show()

    def settings_button_clicked(self) -> None:
        if self.settings_widget.isVisible():
            self.settings_widget.hide()
        else:
            self.settings_widget.show()

    def import_file_button_clicked(self) -> None:
        if self.ui.import_folder_button.isVisible():
            self.ui.import_folder_button.hide()
            self.ui.import_image_button.hide()
        else:
            self.ui.import_folder_button.show()
            self.ui.import_image_button.show()

    def tess_settings_button_clicked(self) -> None:
        if self.tesseract_widget.isVisible():
            self.tesseract_widget.hide()
        else:
            self.tesseract_widget.show()

    def scanner_button_clicked(self):
        try:
            if not self.check_internet_connection():
                self.setInfo("No internet connection, Can not translate text, Only Text Eraser can work in offline mode.",  COLOR_ERROR)
                return
            self.scanner_mode = not self.scanner_mode
            if self.scanner_mode:
                self.eraser_mode = False
                self.ui.eraser_button.setStyleSheet(ERASER_BUTTON_OFF_STYLE_SHEET)

                self.ui.scanner_button.setStyleSheet(SCANNER_BUTTON_ON_STYLE_SHEET)
                self.ui.ImageViewerORIGINAL.selector_mode = True
                self.ui.ImageViewerORIGINAL.viewport().setCursor(Qt.CursorShape.CrossCursor)
                self.setInfo("Select an Area on the original Image to be re-scanned")
            else:
                self.ui.scanner_button.setStyleSheet(SCANNER_BUTTON_OFF_STYLE_SHEET)
                self.ui.ImageViewerORIGINAL.selector_mode = False
                self.ui.ImageViewerORIGINAL.viewport().setCursor(Qt.CursorShape.ArrowCursor)
                self.setInfo("")
        except Exception as e:
            print(f"Error in toggle_scanner_mode: {e}")

    def eraser_button_clicked(self):
        try:
            self.eraser_mode = not self.eraser_mode
            if self.eraser_mode:
                self.scanner_mode = False
                self.ui.scanner_button.setStyleSheet(SCANNER_BUTTON_OFF_STYLE_SHEET)

                self.ui.eraser_button.setStyleSheet(ERASER_BUTTON_ON_STYLE_SHEET)
                self.ui.ImageViewerORIGINAL.selector_mode = True
                self.ui.ImageViewerORIGINAL.viewport().setCursor(Qt.CursorShape.CrossCursor)
                self.setInfo("Select an Area on the original Image to have its text erased")
            else:
                self.ui.eraser_button.setStyleSheet(ERASER_BUTTON_OFF_STYLE_SHEET)
                self.ui.ImageViewerORIGINAL.selector_mode = False
                self.ui.ImageViewerORIGINAL.viewport().setCursor(Qt.CursorShape.ArrowCursor)
                self.setInfo("")
        except Exception as e:
            print(f"Error in toggle_eraser_mode: {e}")

    def translator_changed(self) -> None:
        try:
            self.config.read(self.config_file_path)
            items = ['Croatian', 'Filipino', 'Hebrew', 'Hindi', 'Thai']
            if self.ui.deepl_radio_button.isChecked():
                self.config.set('General', 'Last used translator', 'DeepL')
                for item in items:
                    index = self.ui.language_from_combobox.findText(item)
                    if index != -1:
                        self.ui.language_from_combobox.removeItem(index)
                    index = self.ui.language_to_combobox.findText(item)
                    if index != -1:
                        self.ui.language_to_combobox.removeItem(index)
            else:
                self.config.set('General', 'Last used translator', 'Google')
                self.ui.language_from_combobox.addItems(items)
                self.ui.language_to_combobox.addItems(items)
            with open(self.config_file_path, 'w') as configfile:
                self.config.write(configfile)
        except Exception as e:
            print(e)

    def setInfo(self, text, color=COLOR_DEFAULT_TEXT) -> None:
        self.ui.information.setText(text)
        self.ui.information.setStyleSheet(
            'QLabel { font-weight: bold; color: #' + color + '; background-color: none;  border: 1px solid #101f32; padding: 5px;  font-size: 15px; border-radius: 15px; }')
        QApplication.processEvents()

    def ImportFolder(self, folderpath=None) -> None:
        try:
            if not folderpath:
                folderpath = os.path.normpath(QFileDialog.getExistingDirectory(QFileDialog(self), "Select a folder."))
                if folderpath in ['.', None]:  # user canceled operation
                    return
            folderpath_model_item = self.find_item_by_path(folderpath)

            folderpath_parent = os.path.dirname(folderpath)
            folderpath_parent_model_item = self.find_item_by_path(folderpath_parent)

            # Check if any children of the new folder already exist in the model, to prevent duplicates
            for child_path in self.get_child_paths(folderpath):
                existing_child = self.find_item_by_path(child_path)

                if existing_child and not existing_child.parent():  # Does not have a parent aka Only top-level children
                    # Remove the existing child from the model, they'll be re-added anyway below
                    self.model.removeRow(existing_child.index().row())

            if not folderpath_model_item:  # Folder item does not exist in the model, create & process it
                folderpath_model_item = self.create_model_item(folderpath)
                self.process_directory(folderpath_model_item, folderpath)
                if folderpath_parent_model_item:  # Folder's parent already exists in model, surrender the child
                    folderpath_parent_model_item.appendRow(folderpath_model_item)
                else:  # Child does not have a father, poor child
                    self.model.appendRow(folderpath_model_item)
            else:  # Folder already exists? Store its index, Check if it has a father or not
                folderpath_index = folderpath_model_item.index()

                if folderpath_parent_model_item:
                    folderpath_parent_model_item.removeRow(folderpath_index.row())  # Delete Child
                    folderpath_model_item = self.create_model_item(folderpath)  # Create Child
                    self.process_directory(folderpath_model_item, folderpath)  # Feed Child
                    folderpath_parent_model_item.insertRow(folderpath_index.row(), folderpath_model_item)  # Return Child to its father, along with an apology letter
                else:  # Child: Look at me, I am the father now
                    self.model.removeRow(folderpath_index.row())
                    folderpath_model_item = self.create_model_item(folderpath)
                    self.process_directory(folderpath_model_item, folderpath)
                    self.model.insertRow(folderpath_index.row(), folderpath_model_item)

            self.ui.selection_tree_UI.expand(folderpath_model_item.index())  # Domain Expansion: Malevolent Model Item
            self.remove_empty_folders(self.model.invisibleRootItem())  # Recursively remove any leftover empty folders

            self.import_file_button_clicked()
        except Exception as e:
            print(f"Error in openFolderDialog: {e}")

    def ImportImage(self) -> None:
        try:
            filepaths, _ = QFileDialog.getOpenFileNames(QFileDialog(self), "Select images", "",
                                                        "Images (*.png *.jpeg *.jpg)")
            if not filepaths:  # user canceled operation
                return

            for i in range(self.model.rowCount()):
                item = self.model.item(i)
            filepaths_parent = os.path.normpath(os.path.dirname(filepaths[0]))  # It's guaranteed they all have the same parent anyway
            filepaths_parent_model_item = self.find_item_by_path(filepaths_parent)  # Returns none if no parent item with this path was found in the model
            if not filepaths_parent_model_item:  # Create a parent for the children if they don't have one
                filepaths_parent_model_item = self.create_model_item(filepaths_parent)
                self.model.appendRow(filepaths_parent_model_item)
                for filepath in filepaths:
                    model_file_item = self.create_model_item(filepath)
                    filepaths_parent_model_item.appendRow(model_file_item)
            else:  # if they already have a parent, check whether or not any of the filepaths already exist in that parent, if so, skip them
                existing_filepaths_in_model = {child.data(ITEM_PATH_ROLE) for child in
                                               self.iterate_model_items(filepaths_parent_model_item)}  # to check whether any of the filepaths already exist in our model
                print(existing_filepaths_in_model)
                for filepath in filepaths:
                    if os.path.normpath(filepath) in existing_filepaths_in_model:
                        continue
                    model_file_item = self.create_model_item(filepath)
                    filepaths_parent_model_item.appendRow(model_file_item)

            self.ui.selection_tree_UI.expand(filepaths_parent_model_item.index())
            self.import_file_button_clicked()
        except Exception as e:
            print(f"Error in openimagedialog: {e}")

    def find_item_by_path(self, path):
        """Find the QStandardItem by the given path."""
        for item in self.iterate_model_items():
            if item.data(ITEM_PATH_ROLE) == path:
                return item
        return None

    def iterate_model_items(self, root_item=None):
        """Iterate through the model and return all QStandardItems."""
        if not root_item:
            root_item = self.model.invisibleRootItem()

        for row in range(root_item.rowCount()):
            child = root_item.child(row)
            yield child
            yield from self.iterate_model_items(child)

    def get_child_paths(self, folder_path):
        """Returns a list of paths to all subfolders within a given folder. It does not include files or sub-subfolders."""
        child_paths = []
        for child in os.listdir(folder_path):
            child_path = os.path.join(folder_path, child)
            if os.path.isdir(child_path):
                child_paths.append(child_path)
        return child_paths

    def create_model_item(self, path):
        """Create a new QStandardItem for the given path and return it."""
        model_item = QStandardItem(os.path.basename(path))
        model_item.setData(os.path.normpath(path), ITEM_PATH_ROLE)  # Took me longer than I'd like to admit to figure out why nothing works as intended if you don't normalize your path
        model_item.setData(None, TRANSLATED_ITEM_PATH_ROLE)
        return model_item

    def process_directory(self, parent_item, parent_path):
        try:
            for entry in os.scandir(parent_path):
                if entry.is_file():
                    if not any(entry.path.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.webp']):
                        continue
                    image_child_item = self.create_model_item(entry.path)
                    parent_item.appendRow(image_child_item)
                elif entry.is_dir():
                    folder_child_item = self.create_model_item(entry.path)
                    parent_item.appendRow(folder_child_item)
                    self.process_directory(folder_child_item, entry.path)  # Recursively process subdirectories
        except Exception as e:
            print(f"Error processing directory {parent_path}: {e}")

    def remove_empty_folders(self, parent):
        try:
            for i in range(parent.rowCount() - 1, -1, -1):
                child = parent.child(i)
                if os.path.isdir(child.data(ITEM_PATH_ROLE)):
                    self.remove_empty_folders(child)
                    if child.rowCount() == 0:
                        parent.removeRow(i)
        except Exception as e:
            print(f"Error in remove_empty_folders: {e}")

    # def bogo_sort_best_sort(self, items):
    #     import random
    #     while not all(items[i] <= items[i + 1] for i in range(len(items) - 1)):
    #         random.shuffle(items)
    #     return items

    def on_item_selection_changed(self, selected_item):
        try:
            if selected_item:
                item_path = selected_item.data(ITEM_PATH_ROLE)
                translated_item_path = selected_item.data(TRANSLATED_ITEM_PATH_ROLE)
                item_name = os.path.basename(item_path)
                if os.path.isdir(item_path):
                    self.reset_buttons(False)
                    self.currently_selected_item = (item_path, None)
                    self.setInfo(f'[{item_name}] Folder contains ....... images', COLOR_FOLDER)
                    image_count = sum(1 for root, dirs, files in os.walk(item_path) for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')))  # Takes around 0.1s for ~8k images, I quite like this functionality so unless it becomes a performance issue I'll leave it be
                    self.setInfo(f'[{item_name}] Folder contains {image_count} images', COLOR_FOLDER)
                    self.update_graphics_contents(None, None)
                else:
                    if any(item_path.lower().endswith(ext) for ext in
                           ['.png', '.jpg', '.jpeg', '.webp']):
                        self.reset_buttons(True)
                        if not translated_item_path:
                            self.setInfo(f'[{item_name}]                         |                         [AWAITING SCAN]', COLOR_INFO)
                            self.currently_selected_item = (item_path, None)
                            self.update_graphics_contents(item_path, None)
                        else:
                            self.setInfo(f'[{item_name}]                         |                         [{os.path.basename(translated_item_path)}]', COLOR_SUCCESS)
                            self.currently_selected_item = (item_path, translated_item_path)
                            self.update_graphics_contents(item_path, translated_item_path)
                    else:  # Should never be the case, As only images can be imported, but you never know...
                        self.currently_selected_item = (item_path, None)
                        self.setInfo(f'[CAN NOT DISPLAY] [{item_name}] [NOT AN IMAGE]', COLOR_ERROR)
                        self.update_graphics_contents(None, None)
        except Exception as e:
            print(f"Error in on_item_selection_changed: {e}")

    def reset_buttons(self, active):
        self.ui.ImageViewerORIGINAL.viewport().setCursor(Qt.CursorShape.ArrowCursor)
        self.ui.scanner_button.setStyleSheet(SCANNER_BUTTON_OFF_STYLE_SHEET)
        self.ui.eraser_button.setStyleSheet(ERASER_BUTTON_OFF_STYLE_SHEET)
        self.scanner_mode = False
        self.eraser_mode = False
        self.ui.translate_button.setEnabled(active)
        self.ui.scanner_button.setEnabled(active)
        self.ui.eraser_button.setEnabled(active)

    def update_graphics_contents(self, displayable_original_image_path, displayable_translated_image_path):
        self.ui.ImageViewerTRANSLATED.displayImageOnScene(displayable_translated_image_path)
        self.ui.ImageViewerORIGINAL.displayImageOnScene(displayable_original_image_path)
        if displayable_translated_image_path:
            self.ui.ImageViewerTRANSLATED.ratio_mode(self.current_ratio_mode)
        if displayable_original_image_path:
            self.ui.ImageViewerORIGINAL.ratio_mode(self.current_ratio_mode)

    def handle_translation_end(self, translation_mode, translated_path):
        try:
            og_image_path = self.currently_selected_item[0]
            currently_selected_index = self.find_item_by_path(og_image_path).index()
            self.model.setData(currently_selected_index, translated_path, TRANSLATED_ITEM_PATH_ROLE)
            self.scrollbar_position = self.ui.ImageViewerORIGINAL.verticalScrollBar().value()
            self.update_graphics_contents(og_image_path, translated_path)
            self.currently_selected_item = (og_image_path, translated_path)
            self.ui.ImageViewerORIGINAL.verticalScrollBar().setValue(self.scrollbar_position)
            self.ui.ImageViewerTRANSLATED.verticalScrollBar().setValue(self.scrollbar_position)

            match translation_mode:
                case 0:
                    pass
                case 1 | 2:
                    self.ui.ImageViewerORIGINAL.viewport().setCursor(Qt.CursorShape.CrossCursor)
            self.ui.translate_button.setEnabled(True)
        except Exception as e:
            print(f"Error in handle_translated_path: {e}")

    def check_internet_connection(self):
        try:
            socket.create_connection(("1.1.1.1", 53), 0.5)  # Ping Google's DNS
            return True
        except OSError:
            return False

    def scan_everything(self):
        self.start_translation_worker((0, None, None, None, None))

    def start_translation_worker(self, translation_mode):
        try:
            if not self.currently_selected_item[0]:
                self.setInfo("Nothing selected, please Import/Select an image to begin translation.", COLOR_ERROR)
                return
            if not self.tesstraineddata:
                self.setInfo("No OCR trained data selected, open Tesseract OCR (bottom left) to select one.", COLOR_ERROR)
                return
            if not self.check_internet_connection() and translation_mode[0] != 2:
                self.setInfo("No internet connection, Can not translate text, Only Text Eraser can work in offline mode.", COLOR_ERROR)
                return

            self.translation_worker = TranslationWorker(self, self.currently_selected_item, translation_mode)
            self.translation_worker.finish_signal.connect(self.handle_translation_end)
            self.translation_worker.setInfo.connect(self.setInfo)
            self.translation_worker.start()
            self.ui.ImageViewerORIGINAL.viewport().setCursor(Qt.CursorShape.ArrowCursor)
            self.ui.translate_button.setEnabled(False)
        except Exception as e:
            print(f"Error in start_translation_worker: {e}")

def main():
    try:
        app = QApplication(sys.argv)
        MainWindow = Main()
        MainWindow.show()
        app.exec()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
