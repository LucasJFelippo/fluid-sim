from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt


class Painter(QPainter):
    def __init__(self, window) -> None:
        super().__init__(window)

    def defaultBrush(self):
        self.brushStyle(Qt.blue)

    def penStyle(self, color, width, style = Qt.SolidLine) -> None:
        self.setPen(QPen(color, width, style))

    def brushStyle(self, color, style = Qt.SolidPattern) -> None:
        self.setBrush(QBrush(color, style))

    def drawCircle(self, x, y, radius):
        self.drawEllipse(x, y, int(radius / 2), int(radius / 2))