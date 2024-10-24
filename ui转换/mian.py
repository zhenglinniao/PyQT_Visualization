# -*- coding: utf-8 -*-

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
from PySide2.QtGui import QPalette, QBrush, QPixmap
from PySide2.QtCore import Qt,QSize
from LineStack import *
import os
from PySide2.QtCore import QTimer
from SQLAlchemy import *
from ChartThemes import *
# main
class main_ui(QWidget):
    def __init__(self):
        super().__init__()
        
        # 初始化窗口
        self.setWindowTitle("MainWindow")
        #全屏窗口
        self.showFullScreen()
        # self.setGeometry(100, 100, 1940, 813)
        self.setStyleSheet("background:rgb(16, 17, 41)")

        # 创建布局
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setSpacing(0)

        # 创建顶部的 logo 帧
        self.verticalFrame = QtWidgets.QFrame(self)
        self.verticalFrame.setMaximumSize(QtCore.QSize(16777215, 130))
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.verticalFrame)
        self.label = QtWidgets.QLabel(self.verticalFrame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setPixmap(QtGui.QPixmap("./ui转换/logo.png"))
        self.label.setScaledContents(True)
        self.horizontalLayout_9.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.verticalFrame)

        # 创建内容的水平布局
        self.horizontalFrame = QtWidgets.QFrame(self)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame)

        # 创建左边的垂直布局
        self.verticalFrame1 = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame1)
        self.verticalFrame1.setMaximumSize(QSize(636,1000))
        self.verticalLayout_3.setSpacing(6)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.QWidget0 = self.SetQWidget("QWidget0", "./ui转换/border.png")
        self.verticalLayout.addWidget(self.QWidget0)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.setStyleSheet("""
    QWidget {
        background: rgb(16, 17, 41);  /* 设置窗口背景颜色 */
        font-family: "微软雅黑";  /* 全局字体 */
        font-size: 12px;  /* 全局字体大小 */
        color: rgb(255, 255, 255);  /* 全局字体颜色 */
    }
    QChart {
        font-size: 14px;  /* 图表标题字体大小 */
        font-weight: bold;  /* 图表标题字体加粗 */
    }
    QLegend {
        font-size: 10px;  /* 图例字体大小 */
    }
    QValueAxis {
        font-size: 12px;  /* 坐标轴标签字体大小 */
    }
""")

#TODO: 添加其他内容 verticalLayout一号布局 verticalLayout_3左边布局
        layout0 = QtWidgets.QHBoxLayout()
        layout0.setSpacing(0)
        self.QWidget0.setMaximumSize(636,300)

        
        self.chart = content_charts()

        self.chart.setMaximumSize(400,400)
        self.chart.setStyleSheet("background-color: transparent;")
    
        self.QWidget0_right = QtWidgets.QVBoxLayout()
        self.QWidget0_right.setSpacing(20)
       
        self.title = QtWidgets.QLabel("标题1")
        self.title.setContentsMargins(0, 20, 0, 0)
        
        self.title.setAlignment(Qt.AlignCenter)

        self.title_text_layout1 = QtWidgets.QHBoxLayout()
        
        self.title_text_layout2 = QtWidgets.QHBoxLayout()
        self.title_text_layout3 = QtWidgets.QHBoxLayout()
        self.but1 = QtWidgets.QPushButton()
        self.but1.setFixedSize(15,15)

        


# 设置按钮的样式
        self.but1.setStyleSheet("""
            QPushButton {
                background-color: red;  /* 默认背景颜色 */
                border: 0px;  /* 去掉边框 */
                border-radius: 7px;  /* 圆角半径 */
            }
            QPushButton:pressed {
                background-color: #66FFFF;  /* 按下时的背景颜色 */
            }
        """)
        
        self.but2 = QtWidgets.QPushButton()
        self.but2.setFixedSize(15,15)
        self.but2.setStyleSheet("""
            QPushButton {
                background-color: blue;  /* 默认背景颜色 */
                border: 0px;  /* 去掉边框 */
                border-radius: 7px;  /* 圆角半径 */
            }
            QPushButton:pressed {
                background-color: #66FFFF;  /* 按下时的背景颜色 */
            }
        """)
        self.but3 = QtWidgets.QPushButton()
        self.but3.setFixedSize(15,15)
        self.but3.setStyleSheet("""
            QPushButton {
                background-color: green;  /* 默认背景颜色 */
                border: 0px;  /* 去掉边框 */
                border-radius: 7px;  /* 圆角半径 */
            }
            QPushButton:pressed {
                background-color: #66FFFF;  /* 按下时的背景颜色 */
            }
        """)
        
        
        self.label1 = QtWidgets.QLabel("生产总数：")
        self.label2 = QtWidgets.QLabel("新增生产：")
        self.label3 = QtWidgets.QLabel(" 待生产 ：")
   
        
        self.data_fetch_thread = DtaFetchThread_1()
# 当数据被获取时，调用update_labels方法
        self.data_fetch_thread.data_fetched.connect(self.update_labels)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data1)
        self.timer.start(1000)
        # 初始化界面数据
        self.update_data1()
        self.title_text_layout1.addSpacerItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.title_text_layout1.addWidget(self.but1)
        self.title_text_layout1.addWidget(self.label1)
        self.title_text_layout1.addSpacerItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.title_text_layout2.addSpacerItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.title_text_layout2.addWidget(self.but2)
        self.title_text_layout2.addWidget(self.label2)
        self.title_text_layout2.addSpacerItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.title_text_layout3.addSpacerItem(QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.title_text_layout3.addWidget(self.but3)
        self.title_text_layout3.addWidget(self.label3)
        self.title_text_layout3.addSpacerItem(QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.title.setMinimumSize(200, 0)
        self.title.setMaximumSize(200, 50)
        self.title.setStyleSheet("color:rgb(255, 255, 255);font: 15pt \"微软雅黑\";background-color: transparent;")
        self.QWidget0_right.addWidget(self.title)
        self.QWidget0_right.addStretch()
        self.QWidget0_right.addLayout(self.title_text_layout1)
        self.QWidget0_right.addLayout(self.title_text_layout2)
        self.QWidget0_right.addLayout(self.title_text_layout3)
        self.QWidget0_right.addStretch()
        layout0.addLayout(self.QWidget0_right)
        layout0.addWidget(self.chart)
        # 设置布局对齐方式为顶部
        layout0.setAlignment(Qt.AlignTop)
        # 将布局应用到 QWidget
        self.QWidget0.setLayout(layout0)
        
############################
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.QWidget16 = self.SetQWidget("QWidget16", "./ui转换/border.png")
        self.verticalLayout_16.addWidget(self.QWidget16)
        self.verticalLayout_3.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.QWidget17 = self.SetQWidget("QWidget17", "./ui转换/border.png")
        self.verticalLayout_17.addWidget(self.QWidget17)
        self.verticalLayout_3.addLayout(self.verticalLayout_17)

        self.horizontalLayout_3.addWidget(self.verticalFrame1)



        # 中间内容布局
        self.verticalFrame_2 = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_5.setSpacing(6)
        self.verticalFrame_2.setMaximumSize(QSize(636,1000))
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.QWidget8 = self.SetQWidget("QWidget8", "")
        self.verticalLayout_8.addWidget(self.QWidget8)
        self.verticalLayout_5.addLayout(self.verticalLayout_8)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.QWidget2 = self.SetQWidget("QWidget2", "./ui转换/border.png")
        self.horizontalLayout_2.addWidget(self.QWidget2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addWidget(self.verticalFrame_2)


        # 右边内容布局
        self.verticalFrame_3 = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_6.setSpacing(6)
        self.verticalFrame_3.setMaximumSize(QSize(636,1000))
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.QWidget9 = self.SetQWidget("QWidget9", "./ui转换/border.png")
        self.verticalLayout_9.addWidget(self.QWidget9)
        self.verticalLayout_6.addLayout(self.verticalLayout_9)


        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.QWidget10 = self.SetQWidget("QWidget10", "./ui转换/border.png")
        self.verticalLayout_10.addWidget(self.QWidget10)
        self.verticalLayout_6.addLayout(self.verticalLayout_10)
        self.QWidget10.setMaximumHeight(350)

        self.layout10 = QtWidgets.QVBoxLayout(self.QWidget10)
        self.layout10.setSpacing(0)
        self.layout10.setContentsMargins(0, 0, 0, 0)
        self.layout10_1 = QtWidgets.QHBoxLayout()
        self.layout10_1.setAlignment(Qt.AlignTop)
        self.layout10_1.setSpacing(10)
        self.layout10_1.setContentsMargins(20, 10, 0, 0)
        self.title10 = QtWidgets.QLabel("销售额统计  |")
        self.title10.setFixedSize(QSize(150, 30))
        self.title10.setStyleSheet("color:rgb(255, 255, 255);font: 15pt \"微软雅黑\";background-color: transparent;")
        self.year10 = QtWidgets.QPushButton("年")
        self.year10.setFixedSize(QSize(30, 30))
        self.year10.setStyleSheet("""
        QPushButton{
            background-color: transparent;
            color: #33ffff;
            font: 15pt \"微软雅黑\";
        }
        QPushButton:pressed{
            border= 0px;
            border-radius: 5px;
            background-color: #333fff;
            color: #ffffff;
        }
        """)
        self.month10 = QtWidgets.QPushButton("月")
        self.month10.setFixedSize(QSize(30, 30))
        self.month10.setStyleSheet("""
        QPushButton{
            background-color: transparent;
            color: #33ffff;
            font: 15pt \"微软雅黑\";
        }
        QPushButton:pressed{
            border= 0px;
            border-radius: 5px;
            background-color: #333fff;
            color: #ffffff;

        }
        """)
        self.season10 = QtWidgets.QPushButton("季")
        self.season10.setFixedSize(QSize(30, 30))
        self.season10.setStyleSheet("""
        QPushButton{
            background-color: transparent;
            color: #33ffff;
            font: 15pt \"微软雅黑\";
        }
        QPushButton:pressed{
            border= 0px;
            border-radius: 5px;
            background-color: #333fff;
            color: #ffffff;

        }
        """)
        self.layout10_1.addWidget(self.title10)
        self.layout10_1.addWidget(self.year10)
        self.layout10_1.addWidget(self.month10)
        self.layout10_1.addWidget(self.season10)
        self.layout10.addLayout(self.layout10_1)
        self.char10 = createpie()
        self.char10.setFixedSize(QSize(636, 300))
        self.char10.setStyleSheet("background-color: transparent;border: 0px;border-radius: 20px;")
        self.layout10.addWidget(self.char10)
        self.layout10.addStretch()
        

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.QWidget11 = self.SetQWidget("QWidget11", "./ui转换/border.png")
        self.verticalLayout_11.addWidget(self.QWidget11)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)

        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.QWidget13 = self.SetQWidget("QWidget13", "./ui转换/border.png")
        self.verticalLayout_13.addWidget(self.QWidget13)
        self.horizontalLayout_5.addLayout(self.verticalLayout_13)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.QWidget14 = self.SetQWidget("QWidget14", "./ui转换/border.png")
        self.verticalLayout_14.addWidget(self.QWidget14)
        self.verticalLayout_6.addLayout(self.verticalLayout_14)



        self.horizontalLayout_3.addWidget(self.verticalFrame_3)
        self.verticalLayout_2.addWidget(self.horizontalFrame)


    def update_data1(self):
        self.data_fetch_thread.start()

    def update_labels(self,data):
        if data:
        # 假设只显示第一个数据项的信息
            first_data = data
            self.label1.setText(f'生产总数: {first_data["data_list"]}')
            self.label2.setText(f'新增生产: {first_data["data_list"]}')
            self.label3.setText(f'待生产: {first_data["data_list"]}')
            


    def SetQWidget(self, name, path=None):
        # 创建带背景图片的QWidget
        first_background = QWidget()
        first_background.setStyleSheet("background: none;")
        first_background.setObjectName(name)
        first_background.setMinimumHeight(100)

        # 初始化背景图片
        self.set_background_image(first_background, path)

        # 绑定resize事件以动态调整背景图片大小
        first_background.resizeEvent = lambda event: self.on_widget_resize(event, first_background, path)

        return first_background

    # 设置背景图片函数
    def set_background_image(self, widget, image_path):
        first_palette = QPalette()
        if image_path:
# 创建一个QPixmap对象，加载图像文件
            pixmap = QPixmap(image_path).scaled(widget.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        
# 设置第一个调色板的背景画刷为加载的图像
            first_palette.setBrush(QPalette.Background, QBrush(pixmap))
# 将第一个调色板设置为widget的调色板
            widget.setPalette(first_palette)
# 设置widget自动填充背景
            widget.setAutoFillBackground(True)

    # 处理resize事件以更新背景图片大小
    def on_widget_resize(self, event, widget, path):
        if path:
            self.set_background_image(widget, path)
        widget.update()


if __name__ == "__main__":
    app = QApplication([])
    window = main_ui()
    window.show()
    sys.exit(app.exec_())
