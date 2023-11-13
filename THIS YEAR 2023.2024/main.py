import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import requests


class Project(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Test.ui', self)
        self.Test.clicked.connect(self.text)
        self.api = 'https://api4.binance.com/api/v3/avgPrice'

    def text(self):
        data = {'symbol': f'BTCUSDT'}
        response = requests.get(self.api, data)
        self.textEdit_2.setText(response.json()['price'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec())
