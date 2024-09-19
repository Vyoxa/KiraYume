# Copyright (C) 2024 Yousef A. (Vyoxa).
# Licensed under the GPL-3.0 License.
# Created for KiraYume: https://github.com/Vyoxa/KiraYume

import os
import shutil

from PyQt6.QtWidgets import QDialog, QRadioButton, QGridLayout, QFileDialog
from configparser import ConfigParser

from src.pyui.ChangeFontWindow import Ui_Fonts

class ChangeFontWindow(QDialog):
    def __init__(self, parent=None):
        super(ChangeFontWindow, self).__init__(parent)
        self.main_instance = parent
        try:
            self.ui = Ui_Fonts()
            self.ui.setupUi(self)
            self.setWindowTitle("Change translated text's font")
            QGridLayout(self.ui.fonts_box)
            self.config = ConfigParser()
            self.config_file_path = parent.config_file_path
            self.fonts_dir = parent.fonts_dir
            self.config.read(self.config_file_path)
            self.reload_button_clicked()
            self.ui.reload_button.clicked.connect(self.reload_button_clicked)
            self.ui.add_font_button.clicked.connect(self.add_font_button_clicked)
            self.ui.open_folder_button.clicked.connect(self.open_folder_button_clicked)
            self.show()
        except Exception as e:
            print(e)

    def change_occured(self):
        try:
            font_name = self.sender().text()
            for font in self.config['Fonts']:
                self.config['Fonts'][font] = 'False'
            self.config['Fonts'][font_name] = 'True'
            self.main_instance.ui.text_font.setText(font_name)
            with open(self.config_file_path, 'w') as configfile:
                self.config.write(configfile)
            self.setFocus()
        except Exception as e:
            print(e)

    def add_font_button_clicked(self):
        try:
            filepaths, _ = QFileDialog.getOpenFileNames(QFileDialog(self), "Select a font file", "",
                                                        "Font files (*.ttf *.otf)")
            if not filepaths:
                return

            for filepath in filepaths:
                shutil.copy(filepath, self.fonts_dir)

            self.reload_button_clicked()
        except Exception as e:
            print(e)

    def open_folder_button_clicked(self):
        try:
            os.startfile(self.fonts_dir)
        except Exception as e:
            print(e)

    def reload_button_clicked(self):
        try:
            layout = self.ui.fonts_box.layout()

            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

            row, col, max = 1, 0, False
            max_columns = 3
            n = 0
            for file in os.listdir(self.fonts_dir):
                if file.endswith('.ttf') or file.endswith('.otf'):
                    n += 1
                    radioButton = QRadioButton(file[:-4],
                                               self.ui.fonts_box)  # Create a radio button without the .ttf extension
                    radioButton_config = self.config['Fonts'][file[:-4]] if file[:-4] in self.config['Fonts'] else None

                    if radioButton_config == 'True':
                        radioButton.setChecked(True)
                    else:
                        self.config['Fonts'][file[:-4]] = 'False'

                    radioButton.toggled.connect(
                        self.change_occured)
                    layout.addWidget(radioButton, row, col)

                    with open(self.config_file_path, 'w') as configfile:
                        self.config.write(configfile)
                    col += 1
                    if col >= max_columns:
                        row += 1
                        col = 0
                        max = True
            if max:
                self.setGeo(row, max_columns)
            else:
                self.setGeo(row, col)
            self.ui.fonts_box.setTitle(f'fonts/*.(ttf/otf)  ({n} Fonts found)')
        except Exception as e:
            print(e)
    def setGeo(self, row, columns):
        item_height = 20
        item_width = 80
        window_width = columns * item_width + 180
        window_height = (row + 1) * item_height + 80
        self.setBaseSize(window_width, window_height)
