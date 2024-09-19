# Copyright (C) 2024 Yousef A. (Vyoxa).
# Licensed under the GPL-3.0 License.
# Created for KiraYume: https://github.com/Vyoxa/KiraYume

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QDesktopServices, QIcon
from PyQt6.QtCore import QUrl

from src.core.Constants import PROGRAM_VERSION
from src.pyui.KiraYumeCreditsWidget import Ui_Form

class KiraYumeCreditsWidget(QWidget):
    def __init__(self, parent=None):
        super(KiraYumeCreditsWidget, self).__init__(parent)
        try:
            self.ui = Ui_Form()
            self.ui.setupUi(self)
            self.show()

            self.setGeometry(
                (parent.width() - self.width()) // 2,
                (parent.height() - self.height()) // 2,
                400, 300)
            self.ui.ReleasesGitHubPage.setText(f'<a href="https://github.com/Vyoxa/KiraYume/commits/main" style="text-decoration:none; color:#7289da; ">Version {PROGRAM_VERSION}</a>')
            self.ui.AppIcon.setPixmap(QIcon(parent.resource_path('assets', 'AppIcon512.png')).pixmap(512, 512))
            self.ui.KiraYumeGitHubPage.linkActivated.connect(self.open_link)
            self.ui.ReleasesGitHubPage.linkActivated.connect(self.open_link)
            self.ui.CreatorGitHubPage.linkActivated.connect(self.open_link)
            self.ui.ContributorsGitHubPage.linkActivated.connect(self.open_link)
            self.hide()
        except Exception as e:
            print('err', e)

    def open_link(self, url):
        QDesktopServices.openUrl(QUrl(url))
