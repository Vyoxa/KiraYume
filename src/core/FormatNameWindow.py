# Copyright (C) 2024 Yousef A. (Vyoxa).
# Licensed under the GPL-3.0 License.
# Created for KiraYume: https://github.com/Vyoxa/KiraYume

from PyQt6.QtWidgets import QDialog
from configparser import ConfigParser

from src.pyui.FormatNameWindow import Ui_Form

class FormatNameWindow(QDialog):
    def __init__(self, parent=None):
        super(FormatNameWindow, self).__init__(parent)
        try:
            self.ui = Ui_Form()
            self.ui.setupUi(self)
            self.parent = parent
            self.setWindowTitle("Save translated images as")
            self.ui.name_format.textChanged.connect(self.name_format_changed)
            self.ui.save_button.clicked.connect(self.save_as_clicked)
            self.ui.reset_button.clicked.connect(self.reset_clicked)
            self.current_text = self.ui.name_format.text()
            self.ui.reset_button.setEnabled(not self.isDefault())
            self.ui.save_button.setEnabled(False)

            self.config = ConfigParser()
            self.config_file_path = parent.config_file_path
            self.config.read(self.config_file_path)
            self.ui.name_format.setText(self.config['General']['Save as'])

            self.show()
        except Exception as e:
            print(e)
    def name_format_changed(self, text):
        self.current_text = text
        self.ui.save_button.setEnabled(self.isValidInput(text))
        self.ui.reset_button.setEnabled(not self.isDefault())
    def save_as_clicked(self):
        try:
             self.ui.save_button.setEnabled(False)
             self.parent.SaveAsName.setText(self.current_text)
             self.config['General']['Save as'] = self.current_text
             with open(self.config_file_path, 'w') as configfile:
                 self.config.write(configfile)
             self.setFocus()
        except Exception as e:
            print(e)
    def reset_clicked(self):
        Default_name = '{original_name}_{language_to}{extension_suffix}'
        self.ui.name_format.setText(Default_name)
        self.name_format_changed(Default_name)
        self.config['General']['Save as'] = Default_name
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)
        self.setFocus()
    def isDefault(self):
        return self.ui.name_format.text() == '{original_name}_{language_to}{extension_suffix}'

    def isValidInput(self, text):
        # List of valid image file extensions
        valid_extensions = ['.jpg', '.jpeg', '.png', '.webp']  # TODO: ADD MORE EXTENSIONS
        # Invalid characters in file names
        invalid_chars = '\\/:*?"<>|'

        # Check for invalid characters
        if any(char in text for char in invalid_chars):
            return False

        # Check if text ends with '{extension_suffix}' or any valid image extension
        if text.endswith('{extension_suffix}') or any(text.endswith(ext) for ext in valid_extensions):
            return True

        return False
