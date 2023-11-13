import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber, QLineEdit


class WordTrick(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.c = 0

    def initUI(self):

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Вычисление выражений')
        self.resize(300, 100)

        self.trick_button = QPushButton('->', self)
        self.trick_button.resize(self.trick_button.sizeHint())
        self.trick_button.move(120, 30)
        self.trick_button.clicked.connect(self.hello)
        self.trick_button.resize(30, 25)

        self.first_value = QLineEdit(self)
        self.first_value.move(30, 30)
        self.first_value.resize(80, 25)

        self.second_value = QLineEdit(self)
        self.second_value.move(160, 30)
        self.second_value.resize(80, 25)


    def hello(self):
        self.c += 1
        if self.c % 2 == 1:
            self.first_value.setText('')
            self.second_value.setText('Фокус')
        else:
            self.first_value.setText('Фокус')
            self.second_value.setText('')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())
