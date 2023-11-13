import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class WordTrick(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Фокус со словами')
        self.resize(300, 100)

        self.trick_button = QPushButton('->', self)
        self.trick_button.resize(self.trick_button.sizeHint())
        self.trick_button.move(120, 30)
        self.trick_button.clicked.connect(self.hello)
        self.trick_button.resize(30, 25)

        self.first_value = QLineEdit(self)
        self.first_value.move(30, 30)
        self.first_value.resize(80, 25)
        self.first_value.setText(self.inp)

        self.second_value = QLineEdit(self)
        self.second_value.move(160, 30)
        self.second_value.resize(80, 25)
        self.set_second_value = self.set_first_value

    def hello(self):
        if self.trick_button.text() == '->':
            self.second_value.setText(self.first_value.text())
            self.first_value.setText('')
            self.trick_button.setText('<-')
        else:
            self.first_value.setText(self.second_value.text())
            self.second_value.setText('')
            self.trick_button.setText('->')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())
