# Copyright (C) 2024 Yousef A. (Vyoxa).
# Licensed under the GPL-3.0 License.
# Created for KiraYume: https://github.com/Vyoxa/KiraYume

import os
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices, QIcon
from PyQt6.QtWidgets import QWidget, QCheckBox, QGridLayout, QFileDialog
from configparser import ConfigParser

from src.core.Constants import TESSERACT_CONNECTED_STYLE_SHEET, TESSERACT_DISCONNECTED_STYLE_SHEET
from src.pyui.TesseractSettingsWidget import Ui_Form

class TesseractSettingsWidget(QWidget):
    def __init__(self, parent=None):
        super(TesseractSettingsWidget, self).__init__(parent)
        self.main_instance = parent
        try:
            self.ui = Ui_Form()
            self.ui.setupUi(self)
            self.show()
            QGridLayout(self.ui.traineddata_box)
            self.config = ConfigParser()
            self.config_file_path = parent.config_file_path
            self.config.read(self.config_file_path)
            self.exe_path = None
            self.tessdata_folder = None
            self.ui.edit_exe_path_button.setIcon(QIcon(self.main_instance.resource_path('assets', 'TesseractSettings512.png')))
            # self.check_exe_path()
            self.ui.download_here.linkActivated.connect(self.open_link)
            self.ui.open_tessdata_button.clicked.connect(self.open_tessdata_button_clicked)
            self.ui.edit_exe_path_button.clicked.connect(self.edit_exe_path_button_clicked)
            self.ui.reload_button.clicked.connect(self.reload_button_clicked)
            self.ui.close_button.clicked.connect(self.exit_button_clicked)
            self.hide()
        except Exception as e:
            print(e)

    def open_link(self, url):
        QDesktopServices.openUrl(QUrl(url))

    def check_exe_path(self):
        try:
            self.config.read(self.config_file_path)
            if self.config.has_option('General', 'Tesseract exe location'):
                exe_path = self.config['General']['Tesseract exe location']
                self.exe_path = exe_path
                self.tessdata_folder = os.path.join(os.path.dirname(exe_path), 'tessdata')
                self.ui.executable_path.setText(self.exe_path)
            else:
                self.exe_path = None
                self.tessdata_folder = None
            self.reload_button_clicked()
        except Exception as e:
            print(e)

    def edit_exe_path_button_clicked(self):
        try:
            self.exe_path = QFileDialog.getOpenFileName(self, 'Select Tesseract executable', '',
                                                        'Tesseract Executable (tesseract.exe)')[0]
            if not self.exe_path:
                return
            if os.path.basename(self.exe_path) != 'tesseract.exe':
                self.exe_path = None
                self.tessdata_folder = None
                self.main_instance.ui.tess_activity.setStyleSheet(TESSERACT_DISCONNECTED_STYLE_SHEET)
                self.main_instance.ui.tess_activity.setToolTip('Tesseract-OCR Disconnected.')
            else:
                self.tessdata_folder = os.path.join(os.path.dirname(self.exe_path), 'tessdata')
                self.ui.executable_path.setText(self.exe_path)
                self.config['General']['Tesseract exe location'] = self.exe_path
                self.main_instance.ui.tess_activity.setStyleSheet(TESSERACT_CONNECTED_STYLE_SHEET)
                self.main_instance.ui.tess_activity.setToolTip('Tesseract-OCR Connected.')
                self.reload_button_clicked()
        except Exception as e:
            print(e)

    def change_occured(self, state):
        try:
            self.config.read(self.config_file_path)
            if state == 2:
                self.config['TrainedData'][self.sender().text()] = 'True'
            else:
                self.config['TrainedData'][self.sender().text()] = 'False'
            with open(self.config_file_path, 'w') as configfile:
                self.config.write(configfile)
        except Exception as e:
            print(e)

    def exit_button_clicked(self):
        try:
            if self.tessdata_folder:
                self.config.read(self.config_file_path)
                text = ''
                tessdata_files = os.listdir(self.tessdata_folder)
                for checkbox in self.config['TrainedData']:
                    checkbox_filename = checkbox + '.traineddata'
                    if checkbox_filename not in tessdata_files:
                        self.config['TrainedData'].pop(checkbox)
                    elif self.config['TrainedData'][checkbox] == 'True':
                        text += checkbox + '+'
                text = text[:-1] if text and text[-1] == '+' else text
                self.main_instance.tesstraineddata = text
                with open(self.config_file_path, 'w') as configfile:
                    self.config.write(configfile)
            self.hide()
        except Exception as e:
            print(e)

    def reload_button_clicked(self):
        try:
            if self.tessdata_folder:
                self.config.read(self.config_file_path)
                layout = self.ui.traineddata_box.layout()

                while layout.count():
                    child = layout.takeAt(0)
                    if child.widget():
                        child.widget().deleteLater()

                row, col, max, n = 1, 0, False, 0
                max_columns = 5
                for file in os.listdir(self.tessdata_folder):
                    if file.endswith(".traineddata") and not file.startswith('osd'):
                        n += 1
                        checkbox = QCheckBox(file[:-12], self.ui.traineddata_box)
                        checkbox_config = self.config['TrainedData'][file[:-12]] if file[:-12] in self.config['TrainedData'] else None
                        if checkbox_config == 'True':
                            checkbox.setChecked(True)
                        elif checkbox_config == 'False':
                            checkbox.setChecked(False)
                        else:
                            self.config['TrainedData'][file[:-12]] = 'False'
                        checkbox.stateChanged.connect(self.change_occured)
                        with open(self.config_file_path, 'w') as configfile:
                            self.config.write(configfile)
                        layout.addWidget(checkbox, row, col)
                        col += 1
                        if col >= max_columns:
                            row += 1
                            col = 0
                            max = True
                if max:
                    self.setGeo(row, max_columns)
                else:
                    self.setGeo(row, col)
                match n:
                    case 0:
                        self.ui.traineddata_box.setTitle('tessdata\\*.traineddata (No files found)')
                    case 1:
                        self.ui.traineddata_box.setTitle('tessdata\\*.traineddata (1 file found)')
                    case _:
                        self.ui.traineddata_box.setTitle(f'tessdata\\*.traineddata ({n} files found)')
            else:
                self.ui.traineddata_box.setTitle("Can't find tessdata folder.")
                self.setGeo(1, 1)
        except Exception as e:
            print(e)

    def open_tessdata_button_clicked(self):
        if self.tessdata_folder:
            os.startfile(self.tessdata_folder)

    def setGeo(self, row, columns):
        parentGeometry = self.main_instance.geometry()
        item_height = 20
        item_width = 80
        window_width = columns * item_width + 370
        window_height = (row + 1) * item_height + 280
        self.setGeometry(
            (parentGeometry.width() - window_width) // 2,
            (parentGeometry.height() - window_height) // 2,
            window_width,
            window_height
        )
