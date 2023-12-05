import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from window.window import Window
from draw.draw import *


app = QApplication(sys.argv)


screen_width = app.primaryScreen().size().width()
screen_height = app.primaryScreen().size().height()

win = Window("The Sim", int(screen_width * 0.66), int(screen_height * 0.66))