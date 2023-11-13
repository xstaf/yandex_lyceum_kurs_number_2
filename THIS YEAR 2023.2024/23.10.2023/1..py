import random
import sys

from PyQt5.Qt import QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Suprematize(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(self)

    def initUI(self):
        self.setGeometry(0, 0, 1000, 1000)
        self.setWindowTitle('Супрематизм')

    def mousePressEvent(self, event):
        self.coords = [event.x(), event.y()]
        if event.button() == Qt.LeftButton:
            self.status = 1
        elif event.button() == Qt.RightButton:
            self.status = 2
        self.drawf()

    def mouseMoveEvent(self, event):
        self.coords = [event.x(), event.y()]

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.status = 3
            self.drawf()

    def drawf(self):
        self.flag = False
        self.update()

    def QPainter(self):
        pass

    def paintEvent(self, event):
        if self.flag:
            self.qp = self.QPainter()
            self.qp.begin(self)
            self.draw(self.status)
            self.qp.endd()

    def draw(self, status):
        if status == 1:
            r = random.randint(20, 100)
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            self.qp.setBrush(QColor(red, green, blue))
            self.qp.drawEllipse(int(self.coords[0] - r / 2), int(self.coords[1] - r / 2, r, r))
        if status == 2:
            r = random.randint(20, 100)
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            self.qp.setBrush(QColor(red, green, blue))
            self.qp.drawEllipse(int(self.coords[0] - r / 2), int(self.coords[1] - r / 2, r, r))
        if status == 3:
            r = random.randint(20, 100)
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            self.qp.setBrush(QColor(red, green, blue))
            self.qp.drawEllipse(int(self.coords[0] - r / 2), int(self.coords[1] - r / 2, r, r))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematize()
    ex.show()
    sys.exit(app.exec())
