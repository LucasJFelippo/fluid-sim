from turtle import width
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget

from draw.classes.painter import Painter

class Circle():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        self.radius = 100

    def draw(self, painter) -> None:
        print("entrou")
        painter.drawEllipse(self.x, self.y, int(self.radius / 2), int(self.radius / 2))

class Window(QMainWindow):
    def __init__(self, title, width, heigth) -> None:
        super().__init__()
        self.title = title
        self.width = width
        self.height = heigth
        self.setStyleSheet("background: rgb(30, 30, 30)")
        self.initWindow()
        self.objects = []
        self.objects.append(Circle(100, 100))
        self.objects.append(Circle(200, 100))

        self.painter = Painter(self)

    def initWindow(self) -> None:
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.show()

    def paintEvent(self, event) -> None:
        self.painter.begin(self)
        self.painter.defaultBrush()
        self.objects[0].draw(self.painter)
        self.objects[1].draw(self.painter)
        self.painter.end()