# Copyright (C) 2024 Yousef A. (Vyoxa).
# Licensed under the GPL-3.0 License.
# Created for KiraYume: https://github.com/Vyoxa/KiraYume

from PyQt6.QtGui import QPixmap, QPen, QColor
from PyQt6.QtWidgets import QGraphicsView, QGraphicsRectItem, QGraphicsScene, QGraphicsPixmapItem
from PyQt6.QtCore import Qt, QRectF

from .Constants import RATIO_MODES

class ImageViewer(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main = None
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.selector_mode = False
        self.selection_rect = None
        self.start_point = None

    def displayImageOnScene(self, imagePath):
        try:
            self.scene.clear()
            if imagePath:
                pixmap = QPixmap(imagePath)
                item = QGraphicsPixmapItem(pixmap)
                item.setPos(0, 0)
                self.scene.addItem(item)
                self.scene.setSceneRect(item.boundingRect())
                self.horizontalScrollBar().setValue(0)
                self.verticalScrollBar().setValue(10)
        except Exception as e:
            print(e)

    def mousePressEvent(self, event):
        try:
            if self.selector_mode and event.button() == Qt.MouseButton.LeftButton:
                self.start_point = self.mapToScene(event.pos())
                self.selection_rect = QGraphicsRectItem(QRectF(self.start_point, self.start_point))
                if self.main.scanner_mode:
                    pen = QPen(QColor("#101f32"))
                else:
                    pen = QPen(QColor("#b0454b"))
                pen.setStyle(Qt.PenStyle.DashDotLine)
                pen.setWidth(3)

                self.selection_rect.setPen(pen)
                self.scene.addItem(self.selection_rect)
        except Exception as e:
            print(e)

    def mouseMoveEvent(self, event):
        try:
            if self.selector_mode and self.selection_rect:
                end_point = self.mapToScene(event.pos())
                self.selection_rect.setRect(QRectF(self.start_point, end_point))
        except Exception as e:
            print(f"Error in mouseMoveEvent: {e}")

    def mouseReleaseEvent(self, event):
        try:
            if self.selector_mode and self.selection_rect:
                selection_rect = self.selection_rect.rect()
                self.scene.removeItem(self.selection_rect)
                self.selection_rect = None

                if selection_rect.width() == 0 or selection_rect.height() == 0:
                    return

                x0 = int(min(selection_rect.left(), selection_rect.right()))
                y0 = int(min(selection_rect.top(), selection_rect.bottom()))
                x1 = int(max(selection_rect.left(), selection_rect.right()))
                y1 = int(max(selection_rect.top(), selection_rect.bottom()))

                if self.main.scanner_mode:
                    self.main.start_translation_worker((1, x0, y0, x1, y1))
                else:
                    self.main.start_translation_worker((2, x0, y0, x1, y1))
        except Exception as e:
            print(f"Error in mouseReleaseEvent: {e}")


    def ratio_mode(self, mode):
        try:
            ratio_mode = RATIO_MODES.get(mode, 'Qt.AspectRatioMode.KeepAspectRatioByExpanding')
            self.fitInView(self.scene.itemsBoundingRect(), eval(ratio_mode))
        except Exception as e:
            print(f"Error in ratio_mode: {e}")
