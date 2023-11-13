import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)  # Загружаем дизайн
        self.btn_clear.clicked.connect(self.clear)
        self.btn1.clicked.connect(self.one)

    def clear(self):
        self.table.setText(0)

    def one(self):
        a = str(self.table.te   xt)
        self.table.setText(int(a + '1'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec_())
