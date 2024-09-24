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
# GUI FILE
from app_modules import *

from app_modules import *
from LineStack import *
from ChartThemes import *

class MainWindow(QMainWindow):
    def __init__(self):     

        QMainWindow.__init__(self)
        # 创建一个Ui_MainWindow对象
        self.ui = Ui_MainWindow()
        # 设置主窗口的UI
        self.ui.setupUi(self)
        self.home_layout()    
        print('System: ' + platform.system())
        print('Version: ' +platform.release())
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
        # 添加新菜单
        UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Add User", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "Setting", "btn_widgets", "url(:/16x16/icons/16x16/cil-settings.png)", False)
        # 设置默认菜单
        UIFunctions.selectStandardMenu(self, "btn_home")
        # 设置默认页面
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        # 设置用户图标
        UIFunctions.userIcon(self, "user", "", True)
       
        def moveWindow(event):
           
            # 如果窗口最大化，则切换为正常状态
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # 移动窗口
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

       
        # 设置可移动的窗口部件
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
   

      
        # 加载定义
        UIFunctions.uiDefinitions(self)
      
        # 设置QTableWidget参数
        
        # 显示主窗口
        self.show()
        ## ==> END ##

# 初始化随机数据的Qchart图表
    def home_layout(self):
        #创建一个垂直布局
        self.ui.content = QVBoxLayout(self.ui.page_home)
        chart = ThemeWidget()
        self.ui.content.addWidget(chart)
        
        
#QstackedWidget 的堆叠窗口触发事件 显示
    def Button(self):
        # GET BT CLICKED
        # 获取点击的按钮
        btnWidget = self.sender()

        # PAGE HOME
        # 首页
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")#选中状态
            UIFunctions.labelPage(self, "Home")
            
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        # 新用户
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "New User") 
            # 设置按钮的样式表
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        # 自定义部件
        if btnWidget.objectName() == "btn_widgets":
            # 设置当前页面为page_widgets
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            # 重置按钮样式
            UIFunctions.resetStyle(self, "btn_widgets")
            # 设置标签页标题
            UIFunctions.labelPage(self, "Custom Widgets")
            # 设置按钮样式
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))



##########################################################################
#窗口监控 鼠标监控 键盘监控事件
    #鼠标监控
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')

    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
  
  #双击事件 触发 需要安装过滤器 self.le.installEventFilter(self)  # 安装事件过滤器
    def eventFilter(self, watched, event):
        # 如果被监视的对象是le，并且事件类型是鼠标双击事件
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            # 打印鼠标双击的位置
            print("pos: ", event.pos())
# 定义resizeEvent函数，用于处理窗口大小改变事件
    def resizeEvent(self, event):
        # 调用resizeFunction函数
        self.resizeFunction()
        # 调用父类的resizeEvent函数
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')#字体文件
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
