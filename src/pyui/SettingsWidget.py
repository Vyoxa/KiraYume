# Form implementation generated from reading ui file '.\SettingsWidget.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

# Copyright (C) 2024 Yousef A. (Vyoxa).
# Licensed under the GPL-3.0 License.
# Created for KiraYume: https://github.com/Vyoxa/KiraYume

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(891, 500)
        self.gridLayout = QtWidgets.QGridLayout(Settings)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=Settings)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.reset_button = QtWidgets.QPushButton(parent=self.frame)
        self.reset_button.setStyleSheet("QPushButton {\n"
"    background-color: #101f32;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 8px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    border-radius: 15px;\n"
"    border-width: 3px;\n"
"    min-width: 1em;\n"
"    min-height: 1em;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #293547;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #414c5b;\n"
"}\n"
"")
        self.reset_button.setObjectName("reset_button")
        self.gridLayout_3.addWidget(self.reset_button, 4, 0, 1, 1)
        self.exit_button = QtWidgets.QPushButton(parent=self.frame)
        self.exit_button.setStyleSheet("QPushButton {\n"
"    background-color: #101f32;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 8px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    border-radius: 15px;\n"
"    border-width: 3px;\n"
"    min-width: 1em;\n"
"    min-height: 1em;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #293547;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #414c5b;\n"
"}\n"
"")
        self.exit_button.setObjectName("exit_button")
        self.gridLayout_3.addWidget(self.exit_button, 4, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.edit_saveas = QtWidgets.QPushButton(parent=self.frame)
        self.edit_saveas.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.edit_saveas.setStyleSheet("QPushButton {\n"
"    background-color: none;\n"
"    border: none;\n"
"}\n"
"")
        self.edit_saveas.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../assets/edit128.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.edit_saveas.setIcon(icon)
        self.edit_saveas.setIconSize(QtCore.QSize(30, 35))
        self.edit_saveas.setObjectName("edit_saveas")
        self.gridLayout_2.addWidget(self.edit_saveas, 4, 7, 1, 1)
        self.ratio_mode = QtWidgets.QComboBox(parent=self.frame)
        self.ratio_mode.setStyleSheet("QComboBox {\n"
"    border: 1px solid #009688;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    background: #333;\n"
"    color: #fff;\n"
"    outline: none;\n"
"    padding: 8px\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #666;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border-color: #009688;\n"
"}\n"
"\n"
"QComboBox:drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #444;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    background: #333;\n"
"}\n"
"\n"
"QComboBox:down-arrow {\n"
"    image: url(assets/edit.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #444;\n"
"    background-color: #333;\n"
"    selection-background-color: #003c45;\n"
"    selection-color: #fff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    color: #fff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background: #003c45;\n"
"    color: #fff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #444;\n"
"    background: #222;\n"
"    width: 15px;\n"
"    margin: 22px 0 22px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #555;\n"
"    min-height: 20px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 1px solid #444;\n"
"    background: #222;\n"
"    height: 20px;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background: #333;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    border: 1px solid #444;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: #555;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.ratio_mode.setObjectName("ratio_mode")
        self.ratio_mode.addItem("")
        self.ratio_mode.addItem("")
        self.ratio_mode.addItem("")
        self.gridLayout_2.addWidget(self.ratio_mode, 7, 1, 1, 6)
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setEnabled(True)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: #148fa3; \n"
"    border: 1px solid #101f32; \n"
"    border-radius: 10px; \n"
"    border-width: 1px;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 10, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.frame)
        self.label_9.setStyleSheet("QLabel {\n"
"    border: 1px solid #eabe42;\n"
"    border-radius: 6px;\n"
"    border-width: 1px;\n"
"}")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setEnabled(True)
        self.label.setStyleSheet("QLabel {\n"
"    border: 1px solid #17cc85;\n"
"    border-radius: 6px;\n"
"    border-width: 1px;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.edit_savelocation = QtWidgets.QPushButton(parent=self.frame)
        self.edit_savelocation.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.edit_savelocation.setToolTip("")
        self.edit_savelocation.setStyleSheet("QPushButton {\n"
"    background-color: none;\n"
"    border: none;\n"
"}\n"
"")
        self.edit_savelocation.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../assets/folderIcon128.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.edit_savelocation.setIcon(icon1)
        self.edit_savelocation.setIconSize(QtCore.QSize(30, 35))
        self.edit_savelocation.setObjectName("edit_savelocation")
        self.gridLayout_2.addWidget(self.edit_savelocation, 1, 7, 1, 1)
        self.RGBbgColorInput = QtWidgets.QLineEdit(parent=self.frame)
        self.RGBbgColorInput.setStyleSheet("QLineEdit { \n"
"    border: 1px solid #148fa3; \n"
"    height: 35px; \n"
"    border-radius: 2px;\n"
"    border-width: 1px;\n"
"}")
        self.RGBbgColorInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.RGBbgColorInput.setObjectName("RGBbgColorInput")
        self.gridLayout_2.addWidget(self.RGBbgColorInput, 11, 1, 1, 6)
        self.SETTING_TODO2 = QtWidgets.QCheckBox(parent=self.frame)
        self.SETTING_TODO2.setEnabled(False)
        self.SETTING_TODO2.setStyleSheet("QCheckBox {\n"
"    color: #fff;\n"
"    background-color: #2d2d2d;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 3px;\n"
"    border: 2px solid #444;\n"
"    background: #222;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #009688;\n"
"    background: #003c45;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #666;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 2px solid #33a89f;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    outline: none;\n"
"}")
        self.SETTING_TODO2.setText("")
        self.SETTING_TODO2.setObjectName("SETTING_TODO2")
        self.gridLayout_2.addWidget(self.SETTING_TODO2, 7, 8, 1, 1)
        self.RGBColorInput = QtWidgets.QLineEdit(parent=self.frame)
        self.RGBColorInput.setStyleSheet("QLineEdit { \n"
"    border: 1px solid #148fa3; \n"
"    height: 35px; \n"
"    border-radius: 2px;\n"
"    border-width: 1px;\n"
"}")
        self.RGBColorInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.RGBColorInput.setReadOnly(False)
        self.RGBColorInput.setClearButtonEnabled(False)
        self.RGBColorInput.setObjectName("RGBColorInput")
        self.gridLayout_2.addWidget(self.RGBColorInput, 10, 1, 1, 6)
        self.SETTING_TODO1 = QtWidgets.QCheckBox(parent=self.frame)
        self.SETTING_TODO1.setEnabled(False)
        self.SETTING_TODO1.setStyleSheet("QCheckBox {\n"
"    color: #fff;\n"
"    background-color: #2d2d2d;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 3px;\n"
"    border: 2px solid #444;\n"
"    background: #222;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #009688;\n"
"    background: #003c45;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #666;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 2px solid #33a89f;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    outline: none;\n"
"}")
        self.SETTING_TODO1.setText("")
        self.SETTING_TODO1.setChecked(False)
        self.SETTING_TODO1.setObjectName("SETTING_TODO1")
        self.gridLayout_2.addWidget(self.SETTING_TODO1, 4, 8, 1, 1)
        self.edit_font = QtWidgets.QPushButton(parent=self.frame)
        self.edit_font.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.edit_font.setStyleSheet("QPushButton {\n"
"    background-color: none;\n"
"    border: none;\n"
"}\n"
"")
        self.edit_font.setText("")
        self.edit_font.setIcon(icon)
        self.edit_font.setIconSize(QtCore.QSize(30, 35))
        self.edit_font.setObjectName("edit_font")
        self.gridLayout_2.addWidget(self.edit_font, 13, 7, 1, 1)
        self.auto_import_cd = QtWidgets.QCheckBox(parent=self.frame)
        self.auto_import_cd.setStatusTip("")
        self.auto_import_cd.setWhatsThis("")
        self.auto_import_cd.setStyleSheet("QCheckBox {\n"
"    color: #148fa3;\n"
"    background-color: #2d2d2d;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 3px;\n"
"    border: 2px solid #444;\n"
"    background: #222;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #009688;\n"
"    background: #003c45;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #666;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 2px solid #33a89f;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    outline: none;\n"
"}")
        self.auto_import_cd.setCheckable(True)
        self.auto_import_cd.setChecked(False)
        self.auto_import_cd.setObjectName("auto_import_cd")
        self.gridLayout_2.addWidget(self.auto_import_cd, 1, 8, 1, 1)
        self.SaveLocationName = QtWidgets.QLabel(parent=self.frame)
        self.SaveLocationName.setStyleSheet("QLabel {\n"
"    border: 1px solid #eabe42;\n"
"    border-radius: 2px;\n"
"    border-width: 1px;\n"
"}")
        self.SaveLocationName.setText("")
        self.SaveLocationName.setObjectName("SaveLocationName")
        self.gridLayout_2.addWidget(self.SaveLocationName, 1, 1, 1, 6)
        self.auto_background_color = QtWidgets.QCheckBox(parent=self.frame)
        self.auto_background_color.setStyleSheet("QCheckBox {\n"
"    color: #148fa3;\n"
"    background-color: #2d2d2d;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 3px;\n"
"    border: 2px solid #444;\n"
"    background: #222;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #009688;\n"
"    background: #003c45;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #666;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 2px solid #33a89f;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    outline: none;\n"
"}")
        self.auto_background_color.setChecked(False)
        self.auto_background_color.setObjectName("auto_background_color")
        self.gridLayout_2.addWidget(self.auto_background_color, 11, 8, 1, 1)
        self.RGBLabelBackground = QtWidgets.QLabel(parent=self.frame)
        self.RGBLabelBackground.setStyleSheet("QLabel { \n"
"    color: #148fa3; \n"
"    font-weight: bold;\n"
"}")
        self.RGBLabelBackground.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.RGBLabelBackground.setObjectName("RGBLabelBackground")
        self.gridLayout_2.addWidget(self.RGBLabelBackground, 11, 7, 1, 1)
        self.auto_text_color = QtWidgets.QCheckBox(parent=self.frame)
        self.auto_text_color.setStyleSheet("QCheckBox {\n"
"    color: #148fa3;\n"
"    background-color: #2d2d2d;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 3px;\n"
"    border: 2px solid #444;\n"
"    background: #222;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #009688;\n"
"    background: #003c45;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #666;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 2px solid #33a89f;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    outline: none;\n"
"}")
        self.auto_text_color.setChecked(False)
        self.auto_text_color.setObjectName("auto_text_color")
        self.gridLayout_2.addWidget(self.auto_text_color, 10, 8, 1, 1)
        self.RGBLabelText = QtWidgets.QLabel(parent=self.frame)
        self.RGBLabelText.setStyleSheet("QLabel { \n"
"    color: #148fa3; \n"
"    font-weight: bold;\n"
"}")
        self.RGBLabelText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.RGBLabelText.setObjectName("RGBLabelText")
        self.gridLayout_2.addWidget(self.RGBLabelText, 10, 7, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.frame)
        self.label_8.setStyleSheet("QLabel {\n"
"    color: #148fa3; \n"
"    border: 1px solid #101f32; \n"
"    border-radius: 10px; \n"
"    border-width: 1px;\n"
"}")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 11, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setEnabled(True)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: #148fa3; \n"
"    border: 1px solid #101f32; \n"
"    border-radius: 10px; \n"
"    border-width: 1px;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 13, 0, 1, 1)
        self.SaveAsName = QtWidgets.QLabel(parent=self.frame)
        self.SaveAsName.setStyleSheet("QLabel {\n"
"    border: 1px solid #17cc85;\n"
"    border-radius: 2px;\n"
"    border-width: 1px;\n"
"}")
        self.SaveAsName.setText("")
        self.SaveAsName.setObjectName("SaveAsName")
        self.gridLayout_2.addWidget(self.SaveAsName, 4, 1, 1, 6)
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setStyleSheet("QLabel {\n"
"    border: 1px solid #009688;\n"
"    border-radius: 6px;\n"
"    border-width: 1px;\n"
"    padding: 8px\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 7, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setStyleSheet("QLabel {\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.2 #148fa3, stop:1 #0d404e); \n"
"    font: 15px;\n"
"    font-weight: bold;\n"
"}")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 9, 0, 1, 9)
        self.label_16 = QtWidgets.QLabel(parent=self.frame)
        self.label_16.setStyleSheet("QLabel {\n"
"    color: #101f32;\n"
"    font: 15px;\n"
"    font-weight: bold;\n"
"}")
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 0, 0, 1, 9)
        self.example_sentence = QtWidgets.QLabel(parent=self.frame)
        self.example_sentence.setStyleSheet("QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255); \n"
"    font-size: 15px; \n"
"    border: 4px solid #000000;\n"
"    border-radius: 18px; \n"
"}")
        self.example_sentence.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.example_sentence.setObjectName("example_sentence")
        self.gridLayout_2.addWidget(self.example_sentence, 12, 1, 1, 8)
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setStyleSheet("QLabel {\n"
"    color: #148fa3; \n"
"    border: 1px solid #101f32; \n"
"    border-radius: 10px; \n"
"    border-width: 1px;\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 12, 0, 1, 1)
        self.text_font = QtWidgets.QLabel(parent=self.frame)
        self.text_font.setStyleSheet("QLabel {\n"
"    border: 1px solid #101f32;\n"
"    border-radius: 2px;\n"
"    border-width: 1px;\n"
"}")
        self.text_font.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.text_font.setObjectName("text_font")
        self.gridLayout_2.addWidget(self.text_font, 13, 1, 1, 6)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Form"))
        self.reset_button.setText(_translate("Settings", "Reset defaults"))
        self.exit_button.setText(_translate("Settings", "Exit"))
        self.ratio_mode.setItemText(0, _translate("Settings", "Maintain Aspect Ratio, Expand to Fit"))
        self.ratio_mode.setItemText(1, _translate("Settings", "Maintain Aspect Ratio"))
        self.ratio_mode.setItemText(2, _translate("Settings", "Ignore Aspect Ratio, Resize to Fit"))
        self.label_2.setText(_translate("Settings", "Text Color"))
        self.label_9.setText(_translate("Settings", " Save Location "))
        self.label.setText(_translate("Settings", "Save as"))
        self.RGBbgColorInput.setInputMask(_translate("Settings", "000, 000, 000"))
        self.RGBColorInput.setInputMask(_translate("Settings", "000, 000, 000"))
        self.RGBColorInput.setText(_translate("Settings", ", , "))
        self.auto_import_cd.setToolTip(_translate("Settings", "If possible, add the folder that the program exe is in on launch."))
        self.auto_import_cd.setText(_translate("Settings", "On startup: Import current directory"))
        self.auto_background_color.setText(_translate("Settings", "Auto detect background color"))
        self.RGBLabelBackground.setText(_translate("Settings", "RGB"))
        self.auto_text_color.setText(_translate("Settings", "Auto detect text color"))
        self.RGBLabelText.setText(_translate("Settings", "RGB"))
        self.label_8.setText(_translate("Settings", "Background Color"))
        self.label_3.setText(_translate("Settings", "Text Font"))
        self.label_4.setText(_translate("Settings", "Image Ratio Mode"))
        self.label_7.setText(_translate("Settings", "「 TRANSLATION SETTINGS 」"))
        self.label_16.setText(_translate("Settings", "「 GENERAL SETTINGS 」"))
        self.example_sentence.setToolTip(_translate("Settings", "~Inspired by the training routine from One Punch Man."))
        self.example_sentence.setText(_translate("Settings", "100 push-ups, 100 sit-ups, and 100 squats daily, followed by a 10-kilometer run—every day, no excuses!"))
        self.label_5.setText(_translate("Settings", "Example Colors"))
        self.text_font.setText(_translate("Settings", "notosans-bold"))
