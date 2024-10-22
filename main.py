################################################################################
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
################################################################################

import random
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import numpy as np
import pyqtgraph as pg
import ui_qt.files_rc
# GUI FILE IMPORTS
from app_modules import *
from log.log import *
# 配置日志，输出到文件
class MainWindow(QMainWindow):
    def __init__(self):     
        QMainWindow.__init__(self)
        logging.info('log information...')
        
        # 创建一个Ui_MainWindow对象
        try:
            self.ui = Ui_MainWindow()
            # 设置主窗口的UI
            self.ui.setupUi(self)
            
        except Exception as e:
            logging.error("Error occurred:", exc_info=True)

        try:
            logging.info(f"System info: {platform.system()}")
            logging.info(f"System version: {platform.release()}")
            logging.info(f"Python version: {platform.python_version()}")
        except Exception as e:
            logging.error("Error occurred:", exc_info=True)

        try:
            # 移除标题栏
            UIFunctions.removeTitleBar(True)
            # 设置窗口标题
            self.setWindowTitle('data base')
            # 设置标签标题
            UIFunctions.labelTitle(self, 'Main Window - Python Base')
            # 设置标签描述
            UIFunctions.labelDescription(self, 'Set text')
            # 设置窗口默认大小
            startSize = QSize(1000, 720)
            self.resize(startSize)
            self.setMinimumSize(startSize)
            # 点击按钮切换菜单大小
            self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
            # 设置菜单最小宽度
            self.ui.stackedWidget.setMinimumWidth(20)
        except Exception as e:
            logging.error("Error occurred:", exc_info=True)
        
        # 添加新菜单
        try:
            UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
            UIFunctions.addNewMenu(self, "Add User", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
            UIFunctions.addNewMenu(self, "Setting", "btn_widgets", "url(:/16x16/icons/16x16/cil-settings.png)", False)
            UIFunctions.addNewMenu(self, "new_page", "new_page", "url(:/16x16/icons/16x16/cil-media-step-forward.png)", True)

            UIFunctions.setPanelColor(self, "frame_center")
            UIFunctions.setPanelColor(self, "frame_top_info")
            UIFunctions.setPanelColor(self, "frame_top_btns")
        except Exception as e:
            logging.error("Error occurred:", exc_info=True)
        
        # 设置默认菜单和页面
        try:
            UIFunctions.selectStandardMenu(self, "btn_home")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.userIcon(self, "user", "", True)
        except Exception as e:
            logging.error("Error occurred:", exc_info=True)

        def moveWindow(event):       
            try:
                if UIFunctions.returStatus() == 1:
                    UIFunctions.maximize_restore(self)
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            except Exception as e:
                logging.error("Error occurred:", exc_info=True)

        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow     
        
        # 加载定义 透明窗口
        try:
            UIFunctions.uiDefinitions(self)  
        except Exception as e:
            logging.error("Error occurred:", exc_info=True)

        # 显示主窗口
        try:
            self.show()
        except Exception as e:
            logging.error("Error occurred:", exc_info=True)

    def changeColor(self, color):
        try:
            btn = self.sender()
            if btn.objectName() == "frame_center":
                self.ui.frame_center.setStyleSheet(f"background-color: rgb({color.red()}, {color.green()}, {color.blue()});")
            if btn.objectName() == "frame_top_info":
                self.ui.frame_top_info.setStyleSheet(f"background-color: rgb({color.red()}, {color.green()}, {color.blue()});")
            if btn.objectName() == "frame_top_btns":
                self.ui.frame_top_btns.setStyleSheet(f"background-color: rgb({color.red()}, {color.green()}, {color.blue()});")
        except Exception as e:
            logging.error("Error occurred:", exc_info=True)

    def Button(self):
        try:
            btnWidget = self.sender()
            if btnWidget.objectName() == "btn_home":
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
                UIFunctions.resetStyle(self, "btn_home")
                UIFunctions.labelPage(self, "Home")
                btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            elif btnWidget.objectName() == "btn_new_user":
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_two_home)
                UIFunctions.resetStyle(self, "btn_new_user")
                UIFunctions.labelPage(self, "New User")
                btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            elif btnWidget.objectName() == "btn_widgets":
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_widget)
                UIFunctions.resetStyle(self, "btn_widgets")
                UIFunctions.labelPage(self, "Custom Widgets")
                btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            elif btnWidget.objectName() == "new_page":
                self.ui.stackedWidget.setCurrentWidget(self.ui.new_page)
                UIFunctions.resetStyle(self, "btn_widgets")
                UIFunctions.labelPage(self, "Custom Widgets")
                btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        except Exception as e:
            logging.error("Error occurred:", exc_info=True)
            
    def mousePressEvent(self, event):
        try:
            self.dragPos = event.globalPos()
            if event.buttons() == Qt.LeftButton:
                print('Mouse click: LEFT CLICK')
            elif event.buttons() == Qt.RightButton:
                print('Mouse click: RIGHT CLICK')
            elif event.buttons() == Qt.MidButton:
                print('Mouse click: MIDDLE BUTTON')
        except Exception as e:
            logging.error("Error occurred:", exc_info=True)

    def keyPressEvent(self, event):
        try:
            print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
        except Exception as e:
            logging.error(f"Error during key press event: {e}")

    def eventFilter(self, watched, event):
        try:
            if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
                print("pos: ", event.pos())
        except Exception as e:
            logging.error(f"Error in event filter: {e}")

    def resizeEvent(self, event):
        try:
            self.resizeFunction()
        except Exception as e:
            logging.error(f"Error during resize event: {e}")
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        try:
            print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
        except Exception as e:
            logging.error(f"Error in resize function: {e}")

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')#字体文件
        QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
        window = MainWindow()
        sys.exit(app.exec_())
    except Exception as e:
        logging.error("Error occurred:", exc_info=True)

