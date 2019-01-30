import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QWidget, QVBoxLayout, QScrollArea, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QRect
import modules.Map as map

class WindowContent(QWidget):
    def __init__(self, map):
        super().__init__()
        self.map = map

    def paintEvent(self, e):
        qp = QPainter()

        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):

        content = self.map.get_map()
        for i in range(len(content)):
            for j in range(len(content[i])):
                if content[i][j] == "w":
                    qp.setBrush(QColor(150, 150, 150, 160))
                    qp.drawRect((j * 20) + 50, (i * 20) + 50, 20, 20)
                if content[i][j] == "I":
                    qp.setBrush(QColor(0, 255, 0))
                    qp.drawRect((j * 20) + 50, (i * 20) + 50, 20, 20)
                if content[i][j] == "O":
                    qp.setBrush(QColor(0, 0, 255))
                    qp.drawRect((j * 20) + 50, (i * 20) + 50, 20, 20)
                if content[i][j] == "x":
                    qp.setBrush(QColor(255, 0, 0))
                    qp.drawRect((j * 20) + 50, (i * 20) + 50, 20, 20)
                if content[i][j] == "A":
                    qp.setBrush(QColor(0, 0, 0))
                    qp.drawRect((j * 20) + 50, (i * 20) + 50, 20, 20)

