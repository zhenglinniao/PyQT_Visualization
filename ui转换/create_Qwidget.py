import random
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import numpy as np
import pyqtgraph as pg
# GUI FILE IMPORTS
from mian import *
class Create_Qwidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background:rgb(16, 17, 41)")
        self.layout = QVBoxLayout(self)
        self.init = main_ui()
        #TODO: 像Qwidget里加入图标 后面补充
        self.label = QLabel(self)
        self.label.setText("hello world")
        self.label.setStyleSheet("color:rgb(255, 255, 55)")  
        self.layout_Qwidget0 = QVBoxLayout(self.init.QWidget0)
        self.layout_Qwidget0.addWidget(self.label)


        #把self.init 传给主窗口
        self.layout.addWidget(self.init)
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Create_Qwidget()
    window.show()
    sys.exit(app.exec_())


        
    