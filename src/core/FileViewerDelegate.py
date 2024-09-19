# Copyright (C) 2024 Yousef A. (Vyoxa).
# Licensed under the GPL-3.0 License.
# Created for KiraYume: https://github.com/Vyoxa/KiraYume

import os

from PyQt6.QtWidgets import QStyledItemDelegate
from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtCore import QRect, QSize, QEvent
from PyQt6.QtCore import Qt

from .Constants import ITEM_PATH_ROLE, TRANSLATED_ITEM_PATH_ROLE


class FileViewerDelegate(QStyledItemDelegate):
    def __init__(self, parent=None, main=None):
        super(FileViewerDelegate, self).__init__(parent)
        try:
            self.delete_icon = QIcon(main.resource_path("assets", "delete32.png"))
            self.delete_translated_icon = QIcon(main.resource_path("assets", "delete_translated32.png"))
            self.delete_folder_icon = QIcon(main.resource_path("assets", "delete_folder32.png"))
        except Exception as e:
            print(e)

    def paint(self, painter, option, index):
        try:
            painter.save()

            is_directory = os.path.isdir(index.data(ITEM_PATH_ROLE))
            is_translated = index.data(TRANSLATED_ITEM_PATH_ROLE)

            icon_size = 16
            icon_rect = QRect(int(option.rect.right() - icon_size - 5),
                              int(option.rect.top() + (option.rect.height() - icon_size) / 2),
                              icon_size, icon_size)

            text = index.data(Qt.ItemDataRole.DisplayRole)
            text_rect = option.rect
            text_rect.setLeft(option.rect.left() + 6)

            if is_directory:
                text_color = QColor(236, 236, 236)
                font = painter.font()
                font.setBold(True)
                painter.setFont(font)
                self.delete_folder_icon.paint(painter, icon_rect, Qt.AlignmentFlag.AlignCenter)
            elif is_translated:
                text_color = QColor(83, 211, 224)
                self.delete_translated_icon.paint(painter, icon_rect, Qt.AlignmentFlag.AlignCenter)
            else:
                self.delete_icon.paint(painter, icon_rect, Qt.AlignmentFlag.AlignCenter)
                text_color = QColor(159, 163, 196)

            painter.setPen(text_color)

            metrics = painter.fontMetrics()
            elided_text = metrics.elidedText(text, Qt.TextElideMode.ElideRight, text_rect.width() - 40)
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, elided_text)

            painter.restore()
        except Exception as e:
            print(e)

    def sizeHint(self, option, index):
        is_directory = os.path.isdir(index.data(ITEM_PATH_ROLE))
        is_translated = index.data(TRANSLATED_ITEM_PATH_ROLE)
        if is_directory:
            return QSize(200, 28)
        elif is_translated:
            return QSize(200, 22)
        else:
            return QSize(200, 20)

    def editorEvent(self, event, model, option, index):
        if event.type() == QEvent.Type.MouseButtonPress:
            # Check if the click is within the remove icon area
            icon_size = 16
            icon_rect = QRect(int(option.rect.right() - icon_size - 5),
                              int(option.rect.top() + (option.rect.height() - icon_size) / 2),
                              icon_size, icon_size)

            if icon_rect.contains(event.pos()):
                # Handle the remove action
                model.removeRow(index.row(), index.parent())
                return True
        return super(FileViewerDelegate, self).editorEvent(event, model, option, index)
