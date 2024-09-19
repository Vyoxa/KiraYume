# Copyright (C) 2024 Yousef A. (Vyoxa).
# Licensed under the GPL-3.0 License.
# Created for KiraYume: https://github.com/Vyoxa/KiraYume

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QFileDialog
from configparser import ConfigParser

from .ChangeFontWindow import ChangeFontWindow
from .FormatNameWindow import FormatNameWindow
from src.pyui.SettingsWidget import Ui_Settings

class SettingsWidget(QWidget):
    def __init__(self, parent=None):
        super(SettingsWidget, self).__init__(parent)
        try:
            self.ui = Ui_Settings()
            self.ui.setupUi(self)
            self.show()
            self.main_instance = parent
            self.config_file_path = parent.config_file_path
            self.fonts_dir = parent.fonts_dir
            self.ui.edit_savelocation.setIcon(QIcon(self.main_instance.resource_path('assets', 'folderIcon128.png')))
            self.ui.edit_saveas.setIcon(QIcon(self.main_instance.resource_path('assets', 'edit128.png')))
            self.ui.edit_font.setIcon(QIcon(self.main_instance.resource_path('assets', 'edit128.png')))
            self.init_config_settings()

            self.setGeometry(
                (self.main_instance.width() - self.width()) // 2,
                (self.main_instance.height() - self.height()) // 2,
                900, 500)

            self.ui.edit_saveas.clicked.connect(self.save_as_clicked)
            self.ui.edit_savelocation.clicked.connect(self.save_location_clicked)
            self.NameSaveAsWidget = None
            self.SelectFontWidget = None

            self.ui.ratio_mode.currentIndexChanged.connect(self.toggle_ratio_mode)

            self.ui.auto_import_cd.toggled.connect(self.toggle_auto_import_cd)

            self.ui.auto_text_color.toggled.connect(self.toggle_text_color)
            self.ui.auto_background_color.toggled.connect(self.toggle_background_color)

            self.ui.edit_font.clicked.connect(self.changefont_clicked)


            self.ui.RGBColorInput.textChanged.connect(self.update_example)
            self.ui.RGBbgColorInput.textChanged.connect(self.update_example)

            self.ui.exit_button.clicked.connect(self.hide)
            self.ui.reset_button.clicked.connect(self.reset_defaults)


            self.toggle_text_color()
            self.toggle_background_color()
            self.update_example()
            self.hide()

        except Exception as e:
            print('Error in SettingsWidget: ', e)

    def check_settings_existence(self):
        defaults = {
            'General': {
                'Save as': '{original_name}_{language_to}{extension_suffix}',
                'Save Location': self.main_instance.cwd,
                'Ratio mode': 'Maintain Aspect Ratio, Expand to Fit',
                'Auto save upon translation': 'False',
                'Auto import current directory': 'False',
                'Auto dump translations': 'False',
                'Last used language from': 'Auto',
                'Last used language to': 'English',
                'Last used translator': 'Google'
            },
            'Settings': {
                'Auto text color': 'True',
                'Auto background color': 'True',
                'Background color': '255, 255, 255',
                'Text color': '000, 000, 000'
            },
            'Fonts': {
                'NotoSans-Bold': 'True'
            }
        }

        for section, options in defaults.items():
            if not self.config.has_section(section):
                self.config.add_section(section)
            for option, default_value in options.items():
                if not self.config.has_option(section, option):
                    self.config.set(section, option, default_value)

        # Save updated config back to file
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)

    def init_config_settings(self):
        try:
            self.config = ConfigParser()
            self.config.read(self.config_file_path)

            self.check_settings_existence()

            save_as_name = self.config.get('General', 'Save as')
            self.ui.SaveAsName.setText(save_as_name)

            save_location_name = self.config.get('General', 'Save Location')
            self.ui.SaveLocationName.setText(save_location_name)

            ratio_mode = self.config.get('General', 'Ratio mode')
            self.ui.ratio_mode.setCurrentText(ratio_mode)

            auto_import_current_directory = self.config.getboolean('General', 'Auto import current directory')
            self.ui.auto_import_cd.setChecked(auto_import_current_directory)

            # auto_dump_translation = self.config.getboolean('General', 'Auto dump translations')
            # self.auto_dump_translation.setChecked(auto_dump_translation)

            auto_text_color = self.config.getboolean('Settings', 'Auto text color')
            self.ui.auto_text_color.setChecked(auto_text_color)

            auto_background_color = self.config.getboolean('Settings', 'Auto background color')
            self.ui.auto_background_color.setChecked(auto_background_color)

            rgb_bg_color = self.config.get('Settings', 'Background color')
            self.ui.RGBbgColorInput.setText(rgb_bg_color)

            rgb_text_color = self.config.get('Settings', 'Text color')
            self.ui.RGBColorInput.setText(rgb_text_color)

            selected_font = next((font for font in self.config.options('Fonts') if
                                  self.config.getboolean('Fonts', font, fallback=False)), 'NotoSans-Bold')
            self.ui.text_font.setText(selected_font)
            self.config.set('Fonts', selected_font, 'True')

        except Exception as e:
            print(e)

    def toggle_ratio_mode(self):
        try:
            self.config.read(self.config_file_path)
            current_ratio_mode = self.ui.ratio_mode.currentText()
            self.config['General']['Ratio mode'] = current_ratio_mode
            self.main_instance.current_ratio_mode = current_ratio_mode
            self.main_instance.ui.ImageViewerORIGINAL.ratio_mode(current_ratio_mode)
            self.main_instance.ui.ImageViewerTRANSLATED.ratio_mode(current_ratio_mode)
            with open(self.config_file_path, 'w') as configfile:
                self.config.write(configfile)
        except Exception as e:
            print(e)

    def toggle_auto_import_cd(self):
        self.config.read(self.config_file_path)
        if self.ui.auto_import_cd.isChecked():
            self.config['General']['Auto import current directory'] = 'True'
        else:
            self.config['General']['Auto import current directory'] = 'False'
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)

    # def toggle_auto_dump_translation(self):
    #     if self.ui.auto_dump_translation.isChecked():
    #         self.config['General']['Auto dump translations'] = 'True'
    #     else:
    #         self.config['General']['Auto dump translations'] = 'False'
    #     with open(self.config_file_path, 'w') as configfile:
    #         self.config.write(configfile)

    def toggle_text_color(self):
        self.config.read(self.config_file_path)
        if self.ui.auto_text_color.isChecked():
            self.ui.RGBColorInput.setEnabled(False)
            self.ui.RGBLabelText.setEnabled(False)
            self.config['Settings']['Auto text color'] = 'True'
        else:
            self.ui.RGBColorInput.setEnabled(True)
            self.ui.RGBLabelText.setEnabled(True)
            self.config['Settings']['Auto text color'] = 'False'
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)

    def toggle_background_color(self):
        self.config.read(self.config_file_path)
        if self.ui.auto_background_color.isChecked():
            self.ui.RGBbgColorInput.setEnabled(False)
            self.ui.RGBLabelBackground.setEnabled(False)
            self.config['Settings']['Auto background color'] = 'True'
        else:
            self.ui.RGBbgColorInput.setEnabled(True)
            self.ui.RGBLabelBackground.setEnabled(True)
            self.config['Settings']['Auto background color'] = 'False'
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)

    def update_example(self):
        try:
            text_color = self.parseRGB(self.ui.RGBColorInput.text())
            cursor_position = self.ui.RGBColorInput.cursorPosition()
            self.ui.RGBColorInput.setText(text_color)
            self.ui.RGBColorInput.setCursorPosition(cursor_position)


            bg_color = self.parseRGB(self.ui.RGBbgColorInput.text())
            cursor_position = self.ui.RGBbgColorInput.cursorPosition()
            self.ui.RGBbgColorInput.setText(bg_color)
            self.ui.RGBbgColorInput.setCursorPosition(cursor_position)

            self.config['Settings']['Text color'] = text_color
            self.config['Settings']['Background color'] = bg_color
            self.ui.example_sentence.setStyleSheet(f"color: rgb({text_color}); background-color: rgb({bg_color}); font-size: 15px; border: 4px solid #000000; border-radius: 18px; ")

            with open(self.config_file_path, 'w') as configfile:
                self.config.write(configfile)
        except Exception as e:
            print(e)

    def parseRGB(self, color):
        rgb_values = color.split(',')

        corrected_rgb_values = []
        for value in rgb_values:
            try:
                n = int(value)
                n = max(0, min(n, 255))  # Clamp the value between 0 and 255
                corrected_rgb_values.append(f'{n:03}')  # Format as zero-padded 3 digits
            except ValueError:
                corrected_rgb_values.append('000')  # Default to '000' if conversion fails

        # If there are less than 3 values, pad the remaining values with '000'
        while len(corrected_rgb_values) < 3:
            corrected_rgb_values.append('000')

        return ', '.join(corrected_rgb_values)

    def changefont_clicked(self):
        self.SelectFontWidget = ChangeFontWindow(self)

    def save_as_clicked(self):
        self.NameSaveAsWidget = FormatNameWindow(self)

    def save_location_clicked(self):
        try:
            self.config.read(self.config_file_path)
            folder_path = QFileDialog.getExistingDirectory(QFileDialog(self), "Select a folder as a save location.")
            if folder_path:
                self.ui.SaveLocationName.setText(folder_path)
                self.config['General']['Save Location'] = folder_path
                with open(self.config_file_path, 'w') as configfile:
                    self.config.write(configfile)
        except Exception as e:
            print(e)

    def reset_defaults(self):
        try:
            self.config.read(self.config_file_path)
            self.config.set('General', 'Save location', self.main_instance.cwd)
            self.config.set('General', 'Save as', '{original_name}_{language_to}{extension_suffix}')
            self.config.set('General', 'Ratio mode', 'Maintain Aspect Ratio, Expand to Fit')
            # self.config.set('General', 'Auto sync scroller', 'True')
            self.config.set('General', 'Auto import current directory', 'False')
            # self.config.set('General', 'Auto dump translations', 'False')

            self.config.set('Settings', 'Text color', '000, 000, 000')
            self.config.set('Settings', 'Background color', '255, 255, 255')
            self.config.set('Settings', 'Auto text color', 'True')
            self.config.set('Settings', 'Auto background color', 'True')

            self.config.set('Fonts', 'NotoSans-Bold', 'True')

            with open(self.config_file_path, 'w') as configfile:
                self.config.write(configfile)

            self.init_config_settings()

            self.ui.text_font.setText('NotoSans-Bold')
        except Exception as e:
            print(e)


