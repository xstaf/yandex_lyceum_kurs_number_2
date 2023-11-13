import io
import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>111</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Получить</string>
    </property>
   </widget>
   <widget class="QTextBrowser" name="text_field">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>20</y>
      <width>551</width>
      <height>51</height>
     </rect>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class RandomString(QMainWindow):
    def __init__(self):
        super(RandomString, self).__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.button.clicked.connect(self.click)
        f = open("lines.txt", encoding="utf8")
        self.lines = f.readlines()
        f.close()

    def click(self):
        self.text_Field.setHtml(self.lines[random.randrange(len(self.lines))])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.show()
    sys.exit(app.exec_())
