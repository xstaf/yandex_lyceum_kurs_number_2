import io
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap, QImage, QColor, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

SCREEN_SIZE = [400, 400]

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>805</width>
    <height>469</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>50</y>
      <width>80</width>
      <height>25</height>
     </rect>
    </property>
    <property name="text">
     <string>R</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">channelButtons</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>100</y>
      <width>80</width>
      <height>25</height>
     </rect>
    </property>
    <property name="text">
     <string>G</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">channelButtons</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="pushButton_3">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>160</y>
      <width>80</width>
      <height>25</height>
     </rect>
    </property>
    <property name="text">
     <string>B</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">channelButtons</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="pushButton_4">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>210</y>
      <width>80</width>
      <height>25</height>
     </rect>
    </property>
    <property name="text">
     <string>ALL</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">channelButtons</string>
    </attribute>
   </widget>
   <widget class="QLabel" name="image">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>10</y>
      <width>481</width>
      <height>311</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(120, 255, 120);</string>
    </property>
    <property name="text">
     <string>TextLabel</string>
    </property>
   </widget>
   <widget class="QPushButton" name="left">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>340</y>
      <width>201</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Против часовой стрелки</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">rotateButtons</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="right">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>340</y>
      <width>201</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>По часовой стрелке</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">rotateButtons</string>
    </attribute>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>805</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="channelButtons"/>
  <buttongroup name="rotateButtons"/>
 </buttongroups>
</ui>


'''


class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.filename = QFileDialog.getOpenFileName(self,
                                                    'Выбери картинку',
                                                    '',
                                                    'Картинка (*.jpg)')[0]
        self.orig_image = QImage(self.filename)  # оригинал
        self.curr_image = self.orig_image.copy()
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.image.setPixmap(self.pixmap)

        self.degree = 0
        self.right.clicked.connect(self.rotate)
        self.left.clicked.connect(self.rotate)

        self.pushButton.clicked.connect(self.set_channel)

    def set_channel(self):
        self.curr_image = self.orig_image.copy()
        x, y = self.curr_image.size().width(), self.curr_image.size().height()
        for i in range(x):
            for j in range(y):
                r, g, b = self.curr_image.pixelColor(i, j).getRgb()
                if (self.sender().text() == 'R'):
                    self.curr_image.setPixelColor(QPoint(i, j), QColor(r, 0, 0))
                elif (self.sender().text() == 'G'):
                    self.curr_image.setPixelColor(QPoint(i, j), QColor(0, g, 0))
                elif (self.sender().text() == 'B'):
                    self.curr_image.setPixelColor(QPoint(i, j), QColor(0, 0, b))
                elif (self.sender().text() == 'ALL'):
                    self.curr_image.setPixelColor(QPoint(i, j), QColor(r, g, b))
        transform = QTransform().rotate(self.degree)
        self.curr_image = self.curr_image.transformed(transform)

        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.image.setPixmap(self.pixmap)

    def rotate(self):
        if self.sender() is self.right:
            self.degree += 90
            degree = 90
        else:
            self.degree -= 90
            degree = -90
        self.degree = self.degree % 360
        transform = QTransform().rotate(degree)
        self.curr_image = self.curr_image.transformed(transform)
        self.pixmap = QPixmap(self.curr_image)
        self.image.setPixmap(self.pixmap)

    def run(self):
        self.label.setText("OK")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec_())
