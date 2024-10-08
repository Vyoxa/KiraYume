# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.resize(1073, 768)
        MainWindow.setStyleSheet("QMainWindow {\n"
"\n"
"    background-color: #2b2b2b;\n"
"\n"
"    color: #e0e0e0;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar {\n"
"\n"
"    background-color: #3b3b3b;\n"
"\n"
"    color: #e0e0e0;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item {\n"
"\n"
"    spacing: 3px;\n"
"\n"
"    padding: 2px 10px;\n"
"\n"
"    background-color: #3b3b3b;\n"
"\n"
"    color: #e0e0e0;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected {\n"
"\n"
"    background-color: #4b4b4b;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu {\n"
"\n"
"    background-color: #3b3b3b;\n"
"\n"
"    color: #e0e0e0;\n"
"\n"
"    border: 1px solid #4b4b4b;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item {\n"
"\n"
"    background-color: #3b3b3b;\n"
"\n"
"    color: #e0e0e0;\n"
"\n"
"    padding: 5px 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected {\n"
"\n"
"    background-color: #4b4b4b;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"\n"
"    background-color: #3b3b3b;\n"
"\n"
"    color: #e0e0e0;\n"
"\n"
"    border: 1px solid #4b4b4b;\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView {\n"
"\n"
"    background-color: #3b3b3b;\n"
"\n"
"    color: #e0e0e0;\n"
"\n"
"    alternate-background-color: #4b4b4b;\n"
"\n"
"    gridline-color: #4b4b4b;\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::item {\n"
"\n"
"    background-color: transparent;\n"
"\n"
"    color: #e0e0e0;\n"
"\n"
"    selection-background-color: #4b4b4b;\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::item:selected {\n"
"\n"
"    background-color: #4b4b4b;\n"
"\n"
"    color: #e0e0e0;\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::item:hover {\n"
"\n"
"    background-color: #4b4b4b;\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::item:selected:hover {\n"
"\n"
"    background-color: #5b5b5b;\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::item:pressed {\n"
"\n"
"    background-color: #5b5b5b;\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::section {\n"
"\n"
"    background-color: #3b3b3b;\n"
"\n"
"    color: #e0e0e0;\n"
"\n"
"    border-top: 1px solid #4b4b4b;\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::section:selected {\n"
"\n"
"    background-color: #4b4b4b;\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::section:selected:hover {\n"
"\n"
"    background-color: #5b5b5b;\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::section:selected:pressed {\n"
"\n"
"    background-color: #5b5b5b;\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::indicator {\n"
"\n"
"    width: 16px;\n"
"\n"
"    height: 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::indicator:unchecked {\n"
"\n"
"    image: url(:/images/checkbox-unchecked.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::indicator:checked {\n"
"\n"
"    image: url(:/images/checkbox-checked.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::indicator:indeterminate {\n"
"\n"
"    image: url(:/images/checkbox-indeterminate.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::indicator:hover {\n"
"\n"
"    image: url(:/images/checkbox-unchecked-hover.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::indicator:checked:hover {\n"
"\n"
"    image: url(:/images/checkbox-checked-hover.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::indicator:indeterminate:hover {\n"
"\n"
"    image: url(:/images/checkbox-indeterminate-hover.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::indicator:pressed {\n"
"\n"
"    image: url(:/images/checkbox-unchecked-pressed.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::indicator:checked:pressed {\n"
"\n"
"    image: url(:/images/checkbox-checked-pressed.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::indicator:indeterminate:pressed {\n"
"\n"
"    image: url(:/images/checkbox-indeterminate-pressed.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::sub")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    background-color: #2b2b2b;\n"
"    color: #e0e0e0;\n"
"}\n"
"\n"
"\n"
"QWidget:disabled {\n"
"    color: #808080;\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(8, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 3, 1)
        spacerItem1 = QtWidgets.QSpacerItem(8, 2, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 6, 4, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.KiraYumeCredits_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.KiraYumeCredits_button.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #101f32, stop:0.7 rgba(43, 43, 43, 0)); \n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #101f32, stop:0.85 rgba(43, 43, 43, 0)); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #101f32, stop:0.7 rgba(22, 43, 70, 10)); \n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../assets/AppIcon128.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.KiraYumeCredits_button.setIcon(icon)
        self.KiraYumeCredits_button.setIconSize(QtCore.QSize(45, 45))
        self.KiraYumeCredits_button.setObjectName("KiraYumeCredits_button")
        self.gridLayout.addWidget(self.KiraYumeCredits_button, 1, 1, 1, 2)
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet("QFrame {\n"
"    border: none;\n"
"    padding: 0px;\n"
"    margin: 0px; \n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_4.setStyleSheet("QLabel {\n"
"    color: #d7d7d7;\n"
"    font-weight: bold;\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_5.setStyleSheet("QLabel {\n"
"    color: #d7d7d7;\n"
"    font-weight: bold;\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.frame_3)
        self.label.setStyleSheet("QLabel {\n"
"    color: #d7d7d7;\n"
"    font-weight: bold;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 4, 0, 1, 1)
        self.language_from_combobox = QtWidgets.QComboBox(parent=self.frame_3)
        self.language_from_combobox.setStyleSheet("QComboBox {\n"
"    color: #d7d7d7;\n"
"    font-weight: bold;\n"
"    border: 1px solid #444;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    background: #333;\n"
"    color: #fff;\n"
"    outline: none;\n"
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
"QScrollBar {\n"
"  background: #2b2b2b;  \n"
"  border-radius: 5px;  \n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"  background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(16, 31, 50, 100), stop:1 rgba(20, 143, 163, 100));  \n"
"  border-radius: 4px;\n"
"  opacity: 0.8;\n"
"  width: 8px;  \n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"  width: 0px;\n"
"  height: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"  background: #2b2b2b;\n"
"}")
        self.language_from_combobox.setObjectName("language_from_combobox")
        self.gridLayout_3.addWidget(self.language_from_combobox, 2, 1, 1, 2)
        self.deepl_radio_button = QtWidgets.QRadioButton(parent=self.frame_3)
        self.deepl_radio_button.setStyleSheet("QRadioButton {\n"
"    color: #d7d7d7;\n"
"    background-color: #333;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 7px;\n"
"    border: 2px solid #444;\n"
"    background: #222;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border: 2px solid #009688;\n"
"    background: #003c45;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border: 2px solid #666;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    border: 2px solid #33a89f;\n"
"}\n"
"\n"
"QRadioButton:focus {\n"
"    outline: none;\n"
"}")
        self.deepl_radio_button.setObjectName("deepl_radio_button")
        self.gridLayout_3.addWidget(self.deepl_radio_button, 4, 2, 1, 1)
        self.google_radio_button = QtWidgets.QRadioButton(parent=self.frame_3)
        self.google_radio_button.setStyleSheet("QRadioButton {\n"
"    color: #E5E5E5;\n"
"    background-color: #333;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 7px;\n"
"    border: 2px solid #444;\n"
"    background: #222;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border: 2px solid #009688;\n"
"    background: #003c45;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border: 2px solid #666;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    border: 2px solid #33a89f;\n"
"}\n"
"\n"
"QRadioButton:focus {\n"
"    outline: none;\n"
"}")
        self.google_radio_button.setChecked(True)
        self.google_radio_button.setObjectName("google_radio_button")
        self.gridLayout_3.addWidget(self.google_radio_button, 4, 1, 1, 1)
        self.language_to_combobox = QtWidgets.QComboBox(parent=self.frame_3)
        self.language_to_combobox.setStyleSheet("QComboBox {\n"
"    color: #d7d7d7;\n"
"    font-weight: bold;\n"
"    border: 1px solid #444;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    background: #333;\n"
"    color: #fff;\n"
"    outline: none;\n"
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
"QScrollBar {\n"
"  background: #2b2b2b;  \n"
"  border-radius: 5px;  \n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"  background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(16, 31, 50, 100), stop:1 rgba(20, 143, 163, 100));  \n"
"  border-radius: 4px;\n"
"  opacity: 0.8;\n"
"  width: 8px;  \n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"  width: 0px;\n"
"  height: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"  background: #2b2b2b;\n"
"}")
        self.language_to_combobox.setObjectName("language_to_combobox")
        self.gridLayout_3.addWidget(self.language_to_combobox, 3, 1, 1, 2)
        self.tess_activity = QtWidgets.QLabel(parent=self.frame_3)
        self.tess_activity.setMaximumSize(QtCore.QSize(50, 50))
        self.tess_activity.setStyleSheet("QLabel {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.149254 rgba(16, 31, 50, 206), stop:0.328358 rgba(16, 31, 50, 80), stop:0.442786 rgba(16, 31, 50, 80), stop:0.572139 rgba(20, 132, 132, 80), stop:0.686567 rgba(20, 132, 132, 250), stop:1 rgba(255, 255, 255, 0));\n"
"    border-radius: 20px;\n"
"    margin-top: 10px;\n"
"    margin-right: 10px;\n"
"}")
        self.tess_activity.setText("")
        self.tess_activity.setObjectName("tess_activity")
        self.gridLayout_3.addWidget(self.tess_activity, 5, 2, 1, 1)
        self.tess_settings_button = QtWidgets.QPushButton(parent=self.frame_3)
        self.tess_settings_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tess_settings_button.sizePolicy().hasHeightForWidth())
        self.tess_settings_button.setSizePolicy(sizePolicy)
        self.tess_settings_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tess_settings_button.setStatusTip("")
        self.tess_settings_button.setWhatsThis("")
        self.tess_settings_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tess_settings_button.setStyleSheet("QPushButton {\n"
"    color: #148fa3;\n"
"    background-color: none;\n"
"    border: none;\n"
"    margin-top: 10px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../assets/TesseractSettings128.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tess_settings_button.setIcon(icon1)
        self.tess_settings_button.setIconSize(QtCore.QSize(40, 40))
        self.tess_settings_button.setCheckable(False)
        self.tess_settings_button.setChecked(False)
        self.tess_settings_button.setObjectName("tess_settings_button")
        self.gridLayout_3.addWidget(self.tess_settings_button, 5, 0, 1, 2)
        self.gridLayout_4.addWidget(self.frame_3, 8, 0, 1, 6)
        self.settings_button = QtWidgets.QPushButton(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)
        self.settings_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.settings_button.setStyleSheet("QPushButton {\n"
"    background-color: none;\n"
"    border: none;\n"
"}\n"
"")
        self.settings_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../assets/settings125.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.settings_button.setIcon(icon2)
        self.settings_button.setIconSize(QtCore.QSize(45, 40))
        self.settings_button.setCheckable(False)
        self.settings_button.setObjectName("settings_button")
        self.gridLayout_4.addWidget(self.settings_button, 0, 0, 1, 1)
        self.eraser_button = QtWidgets.QPushButton(parent=self.frame_4)
        self.eraser_button.setEnabled(False)
        self.eraser_button.setStyleSheet("QPushButton {\n"
"    color: #d7d7d7;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.466, x2:1, y2:0.801136, stop:0 #b0454b, stop:0.8 #101f32);\n"
"    border: 1px solid rgba(0, 0, 0, 0);\n"
"    padding: 6px 2px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    border-radius: 14px;\n"
"    border-width: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.466, x2:1, y2:0.801136, stop:0 #b0454b, stop:1 #101f32);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #b0454b;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #c38e91;\n"
"}\n"
"")
        self.eraser_button.setObjectName("eraser_button")
        self.gridLayout_4.addWidget(self.eraser_button, 7, 0, 1, 2)
        self.import_file_button = QtWidgets.QPushButton(parent=self.frame_4)
        self.import_file_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_file_button.sizePolicy().hasHeightForWidth())
        self.import_file_button.setSizePolicy(sizePolicy)
        self.import_file_button.setStyleSheet("QPushButton {\n"
"    background-color: #101f32;\n"
"    border: none;\n"
"    color: #d7d7d7;\n"
"    padding: 8px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    border-radius: 5px;\n"
"    border-width: 3px;\n"
"    min-width: 1em;\n"
"    min-height: 1em;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #172e4a;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0d1929;\n"
"}\n"
"")
        self.import_file_button.setFlat(False)
        self.import_file_button.setObjectName("import_file_button")
        self.gridLayout_4.addWidget(self.import_file_button, 0, 1, 1, 1)
        self.translate_button = QtWidgets.QPushButton(parent=self.frame_4)
        self.translate_button.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.translate_button.setFont(font)
        self.translate_button.setAutoFillBackground(False)
        self.translate_button.setStyleSheet("QPushButton {\n"
"    color: #d7d7d7;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.2 #148fa3, stop:1 #0d404e); \n"
"    border: none;\n"
"    padding: 8px 2px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border-radius: 10px;\n"
"    border-width: 2px;\n"
"    min-width: 8em;\n"
"    margin-top: 5px;  \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    color: #b7b7b7;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.2 #107282, stop:1 #0a333e); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #898989;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.2 #0d5b68, stop:1 #082932); \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #71adc1;\n"
"}\n"
"")
        self.translate_button.setCheckable(False)
        self.translate_button.setChecked(False)
        self.translate_button.setAutoDefault(False)
        self.translate_button.setDefault(False)
        self.translate_button.setFlat(False)
        self.translate_button.setObjectName("translate_button")
        self.gridLayout_4.addWidget(self.translate_button, 6, 0, 1, 6)
        self.selection_tree_UI = QtWidgets.QTreeView(parent=self.frame_4)
        self.selection_tree_UI.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.selection_tree_UI.setStyleSheet("QTreeView {\n"
"            border: 2px solid #101f32;\n"
"            border-radius: 5px; \n"
"            background-color: #2b2b2b;\n"
"            padding: 6px 6px;\n"
"            margin-top: 0px;\n"
"        }\n"
"\n"
"        QTreeView::item:hover {\n"
"            background-color: #4d4d4d;  \n"
"        }\n"
"\n"
"        QTreeView::item:selected {\n"
"            background-color: #13a29a;\n"
"            border-radius: 4px;\n"
"        }\n"
"\n"
"\n"
"        QTreeView::branch:has-siblings:!adjoins-item {\n"
"            border-image: url(/assets/stylesheet-vline.png) 0;\n"
"        }\n"
"\n"
"        QTreeView::branch:has-siblings:adjoins-item {\n"
"            border-image: url(assets/stylesheet-branch-more.png) 0;\n"
"        }\n"
"\n"
"        QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"            border-image: url(assets/stylesheet-branch-end.png) 0;\n"
"        }\n"
"\n"
"        QTreeView::branch:has-children:!has-siblings:closed,\n"
"        QTreeView::branch:closed:has-children:has-siblings {\n"
"            border-image: none;\n"
"            image: url(assets/stylesheet-branch-closed.png);\n"
"        }\n"
"\n"
"        QTreeView::branch:open:has-children:!has-siblings,\n"
"        QTreeView::branch:open:has-children:has-siblings  {\n"
"            border-image: none;\n"
"            image: url(assets/stylesheet-branch-open.png);\n"
"        }\n"
"\n"
"        QScrollBar {\n"
"          background: #2b2b2b;  \n"
"          border-radius: 5px;  \n"
"        }\n"
"\n"
"        QScrollBar::handle {\n"
"          background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(16, 31, 50, 100), stop:1 rgba(20, 143, 163, 100));  \n"
"          border-radius: 4px;\n"
"          opacity: 0.8;\n"
"          width: 5px;  \n"
"        }\n"
"\n"
"        QScrollBar::add-line, QScrollBar::sub-line {\n"
"          width: 0px;\n"
"          height: 0px;\n"
"          margin: 0px;\n"
"        }\n"
"\n"
"        QScrollBar::sub-page, QScrollBar::add-page {\n"
"          background: #2b2b2b;\n"
"        }")
        self.selection_tree_UI.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.selection_tree_UI.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.selection_tree_UI.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.selection_tree_UI.setDragEnabled(False)
        self.selection_tree_UI.setAlternatingRowColors(False)
        self.selection_tree_UI.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.selection_tree_UI.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.selection_tree_UI.setAutoExpandDelay(-1)
        self.selection_tree_UI.setIndentation(15)
        self.selection_tree_UI.setUniformRowHeights(False)
        self.selection_tree_UI.setAnimated(True)
        self.selection_tree_UI.setWordWrap(True)
        self.selection_tree_UI.setExpandsOnDoubleClick(True)
        self.selection_tree_UI.setObjectName("selection_tree_UI")
        self.selection_tree_UI.header().setVisible(False)
        self.selection_tree_UI.header().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.selection_tree_UI, 5, 0, 1, 6)
        self.scanner_button = QtWidgets.QPushButton(parent=self.frame_4)
        self.scanner_button.setEnabled(False)
        self.scanner_button.setStyleSheet("QPushButton {\n"
"    color: #d7d7d7;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.420318, x2:0.955224, y2:0.966, stop:0.25 #101f32, stop:1 #148fa3);\n"
"    border: 1px solid rgba(0, 0, 0, 0);\n"
"    padding: 6px 2px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    border-radius: 14px;\n"
"    border-width: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {    \n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.420318, x2:0.955224, y2:0.966, stop:0.1 #101f32, stop:1 #148fa3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #148fa3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #91abb9;\n"
"}\n"
"")
        self.scanner_button.setObjectName("scanner_button")
        self.gridLayout_4.addWidget(self.scanner_button, 7, 2, 1, 4)
        self.import_folder_button = QtWidgets.QPushButton(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_folder_button.sizePolicy().hasHeightForWidth())
        self.import_folder_button.setSizePolicy(sizePolicy)
        self.import_folder_button.setToolTip("")
        self.import_folder_button.setStyleSheet("QPushButton {\n"
"    color: #fcfcfc;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #1b95cb, stop:1 #13a29a); \n"
"    padding: 8px;\n"
"    border-radius: 4px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #0d6e69, stop:1 #146f97); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #063b38, stop:1 #0d4964); \n"
"}")
        self.import_folder_button.setObjectName("import_folder_button")
        self.gridLayout_4.addWidget(self.import_folder_button, 0, 3, 1, 1)
        self.import_image_button = QtWidgets.QPushButton(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_image_button.sizePolicy().hasHeightForWidth())
        self.import_image_button.setSizePolicy(sizePolicy)
        self.import_image_button.setToolTip("")
        self.import_image_button.setStyleSheet("QPushButton {\n"
"    color: #fcfcfc;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #13a29a, stop:1 #1b95cb); \n"
"    padding: 8px;\n"
"    border-radius: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #146f97, stop:1 #0d6e69); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #0d4964, stop:1 #063b38); \n"
"}")
        self.import_image_button.setObjectName("import_image_button")
        self.gridLayout_4.addWidget(self.import_image_button, 0, 4, 1, 1)
        self.gridLayout.addWidget(self.frame_4, 2, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_5.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ImageViewerORIGINAL = ImageViewer(parent=self.frame_5)
        self.ImageViewerORIGINAL.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.ImageViewerORIGINAL.setMouseTracking(False)
        self.ImageViewerORIGINAL.setStyleSheet("QGraphicsView {\n"
"  background-color: rgba(23, 34, 48, 55);  \n"
"  color: #d3d3d3;  \n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"  background: #2b2b2b;  \n"
"  border-radius: 5px;  \n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"  background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(16, 31, 50, 100), stop:1 rgba(20, 143, 163, 100));  \n"
"  border-radius: 4px;\n"
"  opacity: 0.8;\n"
"  width: 8px;  \n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"  width: 0px;\n"
"  height: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"  background: #2b2b2b;\n"
"}")
        self.ImageViewerORIGINAL.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.ImageViewerORIGINAL.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.ImageViewerORIGINAL.setObjectName("ImageViewerORIGINAL")
        self.gridLayout_5.addWidget(self.ImageViewerORIGINAL, 1, 0, 1, 1)
        self.ImageViewerTRANSLATED = ImageViewer(parent=self.frame_5)
        self.ImageViewerTRANSLATED.setStyleSheet("QGraphicsView {\n"
"  background-color: rgba(20, 143, 163, 55);  \n"
"  color: #2a1f2e;  \n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"  background: #2b2b2b;  \n"
"  border-radius: 5px;  \n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"  background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(16, 31, 50, 100), stop:1 rgba(20, 143, 163, 100));  \n"
"  border-radius: 4px;\n"
"  opacity: 0.8;\n"
"  width: 8px;  \n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"  width: 0px;\n"
"  height: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"  background: #2b2b2b;\n"
"}\n"
"\n"
"")
        self.ImageViewerTRANSLATED.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.ImageViewerTRANSLATED.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.ImageViewerTRANSLATED.setObjectName("ImageViewerTRANSLATED")
        self.gridLayout_5.addWidget(self.ImageViewerTRANSLATED, 1, 1, 1, 1)
        self.SyncSB = QtWidgets.QScrollBar(parent=self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SyncSB.sizePolicy().hasHeightForWidth())
        self.SyncSB.setSizePolicy(sizePolicy)
        self.SyncSB.setStyleSheet("QScrollBar {\n"
"  background: #2b2b2b;  \n"
"  border-radius: 5px;  \n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"  background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(16, 31, 50, 100), stop:1 rgba(20, 143, 163, 100));  \n"
"  border-radius: 4px;\n"
"  opacity: 0.8;\n"
"  width: 8px;  \n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"  width: 0px;\n"
"  height: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"  background: #2b2b2b;\n"
"}")
        self.SyncSB.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.SyncSB.setObjectName("SyncSB")
        self.gridLayout_5.addWidget(self.SyncSB, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.frame_5, 2, 3, 1, 1)
        self.information = QtWidgets.QLabel(parent=self.centralwidget)
        self.information.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.information.setStyleSheet("QLabel {\n"
"    font-weight: bold;\n"
"    color: #d7d7d7;\n"
"    background-color: none;\n"
"    border: 1px solid #101f32;\n"
"    padding: 5px; \n"
"    font-size: 14px;\n"
"    border-radius: 6px; \n"
"}\n"
"")
        self.information.setText("")
        self.information.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.information.setWordWrap(True)
        self.information.setObjectName("information")
        self.gridLayout.addWidget(self.information, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.KiraYumeCredits_button.setText(_translate("MainWindow", "KiraYume"))
        self.label_4.setText(_translate("MainWindow", "Translate From:"))
        self.label_5.setText(_translate("MainWindow", "Translate To:"))
        self.label.setText(_translate("MainWindow", "Translator:"))
        self.deepl_radio_button.setText(_translate("MainWindow", "DeepL"))
        self.google_radio_button.setText(_translate("MainWindow", "Google"))
        self.tess_settings_button.setToolTip(_translate("MainWindow", "Tesseract OCR Settings Menu"))
        self.tess_settings_button.setText(_translate("MainWindow", "   Tesseract OCR"))
        self.settings_button.setToolTip(_translate("MainWindow", "Settings Menu"))
        self.eraser_button.setText(_translate("MainWindow", "Text Eraser"))
        self.import_file_button.setToolTip(_translate("MainWindow", "Add new folder/images"))
        self.import_file_button.setText(_translate("MainWindow", "Add"))
        self.translate_button.setToolTip(_translate("MainWindow", "Scans & translates entire image"))
        self.translate_button.setText(_translate("MainWindow", "Scan Image"))
        self.scanner_button.setText(_translate("MainWindow", "Area Scanner"))
        self.import_folder_button.setText(_translate("MainWindow", "Folder"))
        self.import_image_button.setText(_translate("MainWindow", "Image"))
from core.ImageViewer import ImageViewer
