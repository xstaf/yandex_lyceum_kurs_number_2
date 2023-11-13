import sys, time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)

        self.resize(1280, 720)
        self.setWindowTitle('FIRST PROGRAM EEEEEEEEE')
        self.btm = QPushButton('Button', self)
        self.btm.resize(1280, 720)
        self.btm.clicked.connect(self.hello)
        self.btm.colorCount()

    def hello(self):
        print('Yep, u clicked that')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
