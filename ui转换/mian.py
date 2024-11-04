# -*- coding: utf-8 -*-

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow,QTableWidget,QTableWidgetItem,QHeaderView
from PySide2.QtGui import QPalette, QBrush, QPixmap
from PySide2.QtCore import Qt,QSize

import os
from PySide2.QtCore import QTimer
try:
    from SQLbase.SQLAlchemy import *
except:
    from SQLAlchemy import *
from ChartThemes import *
from LineStack import *
# main
class main_ui(QWidget):
    def __init__(self):
        super().__init__()
        
        # 初始化窗口
        self.setWindowTitle("MainWindow")
        #全屏窗口
        self.showFullScreen()
        # self.setGeometry(100, 100, 1940, 813)
        # self.setStyleSheet("background:rgb(16, 17, 41)")

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
        self.QWidget0.setMaximumSize(636,250)

        
        self.chart = content_charts()

        # self.chart.setMaximumSize(400,400)
        self.chart.setStyleSheet("background-color: transparent;")
    
        self.QWidget0_right = QtWidgets.QVBoxLayout()
        self.QWidget0_right.setSpacing(20)
        self.QWidget0_right.setContentsMargins(0, 30, 0, 0)
       
        self.title = QtWidgets.QLabel("标题1")
        self.title.setContentsMargins(10, 20, 0, 0)
        
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
        self.label1.setStyleSheet("color: rgb(255, 255, 255); font-size: 15px; font-family: '微软雅黑';")
        self.label2 = QtWidgets.QLabel("新增生产：")
        self.label2.setStyleSheet("color: rgb(255, 255, 255); font-size: 15px; font-family: '微软雅黑';")
        self.label3 = QtWidgets.QLabel(" 待生产 ：")
        self.label3.setStyleSheet("color: rgb(255, 255, 255); font-size: 15px; font-family: '微软雅黑';")
   
        self.data_fetch_thread = DtaFetchThread_1()
# 当数据被获取时，调用update_labels方法
        self.data_fetch_thread.data_fetched.connect(self.update_labels)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data1)
        self.timer.start(6000)
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
        self.layout16 = QtWidgets.QHBoxLayout(self.QWidget16)
        self.piechart16 = createpie5()
        self.piechart16.setStyleSheet("background-color: transparent;")
        self.layout16.addWidget(self.piechart16)

        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.QWidget17 = self.SetQWidget("QWidget17", "./ui转换/border.png")
        self.QWidget17.setFixedHeight(300)
        self.verticalLayout_17.addWidget(self.QWidget17)
        self.verticalLayout_3.addLayout(self.verticalLayout_17)
        self.horizontalLayout_3.addWidget(self.verticalFrame1)
        self.layout17 = QtWidgets.QVBoxLayout(self.QWidget17)
        self.layout17.setSpacing(0)
        self.linchart17 = content_charts()
        self.linchart17.setStyleSheet("background-color: transparent;")
        self.layout17.addWidget(self.linchart17)



        # 中间内容布局
        self.verticalFrame_2 = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_5.setSpacing(6)
        self.verticalFrame_2.setMaximumSize(QSize(636,1000))
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.QWidget8 = self.SetQWidget("QWidget8", "")
        self.QWidget8.setStyleSheet("background-color: transparent;")
        self.verticalLayout_8.addWidget(self.QWidget8)
        self.verticalLayout_5.addLayout(self.verticalLayout_8)
        self.layout8 = QtWidgets.QVBoxLayout(self.QWidget8)
        self.layout8.setSpacing(0)
        self.table8 = QTableWidget()
        self.table8.setMaximumHeight(300)
        self.txt8  = QtWidgets.QLabel("生产设备监控")
        self.txt8.setStyleSheet("color:rgb(255, 255, 255);font: 14pt \"微软雅黑\";background-color: transparent;")
        self.txt8.setContentsMargins(10, 0, 0, 0)
        self.layout8.addWidget(self.txt8)
        self.layout8.addWidget(self.table8)


        self.table8.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table8.setStyleSheet("""
    QTableWidget {
        color: #3399FF;
        background-color: transparent;
        border: none;
        gridline-color: transparent;
        font: 16px "Microsoft YaHei";
    }
    QHeaderView::section {
        font: 16px "Microsoft YaHei";
        background-color: #1F4788;
        border: none;
    }
""")
        self.table8.verticalScrollBar().setStyleSheet("""
    QScrollBar:vertical {
        background-color: transparent;  /* 滚动条背景颜色 */
        width: 16px;            /* 滚动条宽度 */
    }
    QScrollBar::handle:vertical {
        background-color: #3399FF;  /* 滑块背景颜色 */
        border-radius: 5px;
        min-height: 20px;           /* 滑块的最小高度 */
    }
    QScrollBar::handle:vertical:hover {
        background-color: #FFFFFF;  /* 悬停时的滑块颜色 */
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        background: none;  /* 隐藏上下按钮 */
        height: 0px;
    }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
        background: none;  /* 隐藏滚动条的上下箭头 */
    }
""")
        
        self.table8.setRowCount(50)  # 设置行数
        self.table8.setColumnCount(4)  # 设置列数
        
        self.data_fetch_thread8 = DtaFetchThread_8()
# 当数据被获取时，调用update_labels方法
        self.data_fetch_thread8.data_fetched.connect(self.update_labels8)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data8)
        self.timer.start(1000)
        
        
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.QWidget2 = self.SetQWidget("QWidget2", "./ui转换/border.png")
# 设置QWidget2的最小尺寸为636x1000
        self.QWidget2.setMinimumHeight(500)
        self.horizontalLayout_2.addWidget(self.QWidget2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addWidget(self.verticalFrame_2)
        self.layout2 = QtWidgets.QVBoxLayout(self.QWidget2)
        self.layout2.setSpacing(0)
        self.layout2.setContentsMargins(0,10,0,0)
        self.title2 = QtWidgets.QLabel("数据概览")
        self.title2.setStyleSheet("font: 18px 'Microsoft YaHei';font-weight: bold; color: #3399FF;")
        self.title2.setAlignment(Qt.AlignCenter)
        self.chart2 = createBar6()
        self.chart2.setStyleSheet("background-color: transparent;")
        self.layout2.addWidget(self.title2)
        self.layout2.addWidget(self.chart2)
        
        
        # 右边内容布局
        self.verticalFrame_3 = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_6.setSpacing(6)
        self.verticalFrame_3.setMaximumSize(QSize(636,1000))
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.QWidget9 = self.SetQWidget("QWidget9", "./ui转换/border.png")
        self.QWidget9.setMaximumHeight(120)
        self.verticalLayout_9.addWidget(self.QWidget9)
        self.verticalLayout_6.addLayout(self.verticalLayout_9)
        self.layout9 = QtWidgets.QVBoxLayout(self.QWidget9)
        self.layout9.setSpacing(10)
        self.layout9_top = QtWidgets.QHBoxLayout()
        self.layout9_top.setContentsMargins(20,10,0,0)
        self.layout9.setAlignment(Qt.AlignTop)
        self.layout9.setContentsMargins(20,0,0,0)
        self.days_365 = QtWidgets.QPushButton("365天")
        self.txt_1 = QtWidgets.QLabel("|")
        self.txt_2 = QtWidgets.QLabel("|")
        self.txt_3 = QtWidgets.QLabel("|")
        self.styleSheet9 = """
                                    QPushButton{
                                        font: 12pt \"微软雅黑\";
                                        background-color: transparent;
                                        color:#0000CC;
                                    }
                                    QPushButton:pressed{
                                        border: 0px;
                                        color:rgb(255, 255, 255);
                                    }
                                    """
        self.days_90 = QtWidgets.QPushButton("90天")
        self.days_30 = QtWidgets.QPushButton("30天")
        self.days_1 = QtWidgets.QPushButton("1天")

        self.days_365.setFixedSize(QSize(50, 30))
        self.days_90.setFixedSize(QSize(50, 30))
        self.days_30.setFixedSize(QSize(50, 30))
        self.days_1.setFixedSize(QSize(50, 30))
        self.days_365.setStyleSheet(self.styleSheet9)
        self.txt_1.setStyleSheet("color:#3399FF;font: 15pt \"微软雅黑\";background-color: transparent;")
        self.days_90.setStyleSheet(self.styleSheet9)
        self.txt_2.setStyleSheet("color:#3399FF;font: 15pt \"微软雅黑\";background-color: transparent;")
        self.days_30.setStyleSheet(self.styleSheet9)
        self.txt_3.setStyleSheet("color:#3399FF;font: 15pt \"微软雅黑\";background-color: transparent;")
        self.days_1.setStyleSheet(self.styleSheet9)

        self.days_365.setCheckable(True)
        self.days_90.setCheckable(True)
        self.days_30.setCheckable(True)
        self.days_1.setCheckable(True)
        self.days_365.clicked.connect(self.updata_button9)
        self.days_90.clicked.connect(self.updata_button9)
        self.days_30.clicked.connect(self.updata_button9)
        self.days_1.clicked.connect(self.updata_button9)


        self.layout9_top.addWidget(self.days_365)
        self.layout9_top.addWidget(self.txt_1)
        self.layout9_top.addWidget(self.days_90)
        self.layout9_top.addWidget(self.txt_2)
        self.layout9_top.addWidget(self.days_30)
        self.layout9_top.addWidget(self.txt_3)
        self.layout9_top.addWidget(self.days_1)
        self.layout9_top.addStretch()
        self.layout9.addLayout(self.layout9_top)
        self.layout9_bottom = QtWidgets.QHBoxLayout()
        self.layout9_bottom.setContentsMargins(0,0,0,10)
        self.layout9_bottom_left = QtWidgets.QVBoxLayout()
        self.layout9_bottom_left.setSpacing(10)
        self.layout9_bottom_right = QtWidgets.QVBoxLayout()
        self.layout9_bottom_right.setSpacing(10)

        self.label9_1 = QtWidgets.QLabel("销售额(万元)")
        self.label9_1.setStyleSheet("color:#3399FF;font: 10pt \"微软雅黑\";background-color: transparent;")
        self.label9_1.setAlignment(Qt.AlignCenter)
        self.label9_1_value = QtWidgets.QLabel("0")
        self.label9_1_value.setStyleSheet("color:#FFFFFF;font: 25pt \"微软雅黑\";background-color: transparent;")
        self.label9_1_value.setAlignment(Qt.AlignCenter)
        self.label9_2 = QtWidgets.QLabel("销售量")
        self.label9_2.setStyleSheet("color:#3399FF;font: 10pt \"微软雅黑\";background-color: transparent;")
        self.label9_2.setAlignment(Qt.AlignCenter)
        self.label9_2_value = QtWidgets.QLabel("0")
        self.label9_2_value.setStyleSheet("color:#FFFFFF;font: 25pt \"微软雅黑\";background-color: transparent;")
        self.label9_2_value.setAlignment(Qt.AlignCenter)

        self.layout9_bottom_left.addWidget(self.label9_1)
        self.layout9_bottom_left.addWidget(self.label9_1_value)
        self.layout9_bottom_right.addWidget(self.label9_2)
        self.layout9_bottom_right.addWidget(self.label9_2_value)

        self.layout9_bottom.addLayout(self.layout9_bottom_left)
        self.layout9_bottom.addLayout(self.layout9_bottom_right)
        self.layout9.addLayout(self.layout9_bottom)

        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.QWidget10 = self.SetQWidget("QWidget10", "./ui转换/border.png")
        self.verticalLayout_10.addWidget(self.QWidget10)
        self.verticalLayout_6.addLayout(self.verticalLayout_10)
        self.QWidget10.setMaximumHeight(300)

        self.layout10 = QtWidgets.QVBoxLayout(self.QWidget10)
        self.layout10.setSpacing(0)
        
        self.layout10_1 = QtWidgets.QHBoxLayout()
        self.layout10_1.setAlignment(Qt.AlignTop)
        self.layout10_1.setSpacing(10)
        self.layout10_1.setContentsMargins(30, 0, 0, 0)
        self.title10 = QtWidgets.QLabel("销售额统计")
        self.txt10 = QtWidgets.QLabel("|  ")
        self.txt10.setStyleSheet("color:#3399FF;font: 15pt \"微软雅黑\";background-color: transparent;")
        self.title10.setFixedSize(QSize(150, 30))
        self.title10.setStyleSheet("color:rgb(255, 255, 255);font: 15pt \"微软雅黑\";background-color: transparent;")
        #按钮布局
        self.button_style10 ="""
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
        """
        
        self.year10 = QtWidgets.QPushButton("年")
        self.year10.setFixedSize(QSize(30, 30))
        self.year10.setStyleSheet(self.button_style10)
        self.month10 = QtWidgets.QPushButton("月")
        self.month10.setFixedSize(QSize(30, 30))
        self.month10.setStyleSheet(self.button_style10)
        self.season10 = QtWidgets.QPushButton("季")
        self.season10.setFixedSize(QSize(30, 30))
        self.season10.setStyleSheet(self.button_style10)
        self.year10.setCheckable(True)
        self.month10.setCheckable(True)
        self.season10.setCheckable(True)
        self.year10.clicked.connect(self.updata_button10)
        self.month10.clicked.connect(self.updata_button10)
        self.season10.clicked.connect(self.updata_button10)
                                      
        self.layout10_1.addWidget(self.title10)
        self.layout10_1.addWidget(self.txt10)
        self.layout10_1.addWidget(self.year10)
        self.layout10_1.addWidget(self.month10)
        self.layout10_1.addWidget(self.season10)
        self.layout10_1.addStretch()
        self.layout10.addLayout(self.layout10_1)
        self.char10 = createBar()
        self.char10.setFixedSize(QSize(610, 300))
        self.char10.setStyleSheet("background-color: transparent;border: 0px;border-radius: 20px;")
        self.layout10.addWidget(self.char10)
        # self.layout10.addStretch()
        


        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.QWidget11 = self.SetQWidget("QWidget11", "./ui转换/border.png")
        self.QWidget11.setMaximumHeight(150)
        self.verticalLayout_11.addWidget(self.QWidget11)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        
        self.layout11 = QtWidgets.QHBoxLayout(self.QWidget11)
        self.layout11.setSpacing(0)
        self.layout11.setContentsMargins(0, 0, 0, 0)
        self.layout11_left = QtWidgets.QVBoxLayout()
        self.layout11_left.setSpacing(0)
        self.layout11_left.setContentsMargins(0, 40, 0, 40)
        self.layout11_right = QtWidgets.QVBoxLayout()
        self.layout11_right.setContentsMargins(0, 25, 0, 25)
        self.layout11_right.setSpacing(0)
        self.layout11.addLayout(self.layout11_left)
        self.layout11.addLayout(self.layout11_right)


        self.layout11_left_txt1 = QtWidgets.QLabel("年累计毛利率")
        self.layout11_left_txt1.setAlignment(QtCore.Qt.AlignCenter)
        self.layout11_left_txt1.setStyleSheet("color:rgb(255, 255, 255);font: 12pt \"微软雅黑\";background-color: transparent;")
        self.layout11_left_num1 = QtWidgets.QLabel("86.0%")
        self.layout11_left_num1.setAlignment(QtCore.Qt.AlignCenter)
        self.layout11_left_num1.setStyleSheet("color:rgb(255, 255, 255);font: 17pt \"微软雅黑\";background-color: transparent;font-weight: bold;")
        self.layout11_left.addWidget(self.layout11_left_txt1)
        self.layout11_left.addWidget(self.layout11_left_num1)


        self.layout11_right_txt1 = QtWidgets.QLabel("预算比")
        self.layout11_right_txt1.setAlignment(QtCore.Qt.AlignCenter)
        self.layout11_right_txt1.setStyleSheet("color:rgb(255, 255, 255);font: 11pt \"微软雅黑\";background-color: transparent;")
        self.layout11_right_lyout1 = QtWidgets.QHBoxLayout()
        self.layout11_right_lyout1.setAlignment(QtCore.Qt.AlignCenter)
        self.layout11_right_lyout1.setSpacing(10)
        icon_label11_1 = QtWidgets.QLabel()
        icon_pixmap = QtGui.QPixmap("icons/16x16/cil-caret-top.png")  # 替换为您的图标路径
        painter = QtGui.QPainter(icon_pixmap)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon_pixmap.rect(), Qt.red)  # 设置图标颜色为红色
        painter.end()
        icon_label11_1.setPixmap(icon_pixmap.scaled(15, 15, QtCore.Qt.KeepAspectRatio)) 
        icon_label11_1.setFixedSize(15, 15)
        self.num11_1 = QtWidgets.QLabel("21.29%")
        self.num11_1.setStyleSheet("color:rgb(255, 255, 255);font: 15pt \"微软雅黑\";background-color: transparent;font-weight: bold;")
        self.layout11_right_lyout1.addWidget(icon_label11_1)
        self.layout11_right_lyout1.addWidget(self.num11_1)
        
        self.layout11_right_txt2 = QtWidgets.QLabel("实际比")
        self.layout11_right_txt2.setAlignment(QtCore.Qt.AlignCenter)
        self.layout11_right_txt2.setStyleSheet("color:rgb(255, 255, 255);font: 11pt \"微软雅黑\";background-color: transparent;")
        self.layout11_right_lyout2 = QtWidgets.QHBoxLayout()
        self.layout11_right_lyout2.setAlignment(QtCore.Qt.AlignCenter)
        self.layout11_right_lyout2.setSpacing(10)
        icon_label11_2 = QtWidgets.QLabel()
        
        icon_label11_2.setPixmap(icon_pixmap.scaled(15, 15, QtCore.Qt.KeepAspectRatio)) 
        icon_label11_2.setFixedSize(15, 15)
        self.num11_2 = QtWidgets.QLabel("55.9%")
        self.num11_2.setStyleSheet("color:rgb(255, 255, 255);font: 15pt \"微软雅黑\";background-color: transparent;font-weight: bold;")
        self.layout11_right_lyout2.addWidget(icon_label11_2)
        self.layout11_right_lyout2.addWidget(self.num11_2)

        self.layout11_right.addWidget(self.layout11_right_txt1)
        self.layout11_right.addLayout(self.layout11_right_lyout1)
        self.layout11_right.addWidget(self.layout11_right_txt2)
        self.layout11_right.addLayout(self.layout11_right_lyout2)



        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.QWidget13 = self.SetQWidget("QWidget13", "./ui转换/border.png")
        self.QWidget13.setMaximumHeight(150)
        self.verticalLayout_13.addWidget(self.QWidget13)
        self.horizontalLayout_5.addLayout(self.verticalLayout_13)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        ################### 
        self.layout13 = QtWidgets.QHBoxLayout(self.QWidget13)
        self.layout13.setSpacing(0)
        self.layout13.setContentsMargins(0, 0, 0, 0)
        self.layout13_left = QtWidgets.QVBoxLayout()
        self.layout13_left.setSpacing(0)
        self.layout13_left.setContentsMargins(0, 40, 0, 40)
        self.layout13_right = QtWidgets.QVBoxLayout()
        self.layout13_right.setContentsMargins(0, 25, 0, 25)
        self.layout13_right.setSpacing(0)
        self.layout13.addLayout(self.layout13_left)
        self.layout13.addLayout(self.layout13_right)
        self.layout13_left_txt1 = QtWidgets.QLabel("年累计主盈收入")
        self.layout13_left_txt1.setAlignment(QtCore.Qt.AlignCenter)
        self.layout13_left_txt1.setStyleSheet("color:rgb(255, 255, 255);font: 12pt \"微软雅黑\";background-color: transparent;")
        self.layout13_left_num1 = QtWidgets.QLabel("256644")
        self.layout13_left_num1.setAlignment(QtCore.Qt.AlignCenter)
        self.layout13_left_num1.setStyleSheet("color:rgb(255, 255, 255);font: 17pt \"微软雅黑\";background-color: transparent;font-weight: bold;")
        self.layout13_left.addWidget(self.layout13_left_txt1)
        self.layout13_left.addWidget(self.layout13_left_num1)
        self.layout13_right_txt1 = QtWidgets.QLabel("预算比")
        self.layout13_right_txt1.setAlignment(QtCore.Qt.AlignCenter)
        self.layout13_right_txt1.setStyleSheet("color:rgb(255, 255, 255);font: 11pt \"微软雅黑\";background-color: transparent;")
        self.layout13_right_lyout1 = QtWidgets.QHBoxLayout()
        self.layout13_right_lyout1.setAlignment(QtCore.Qt.AlignCenter)
        self.layout13_right_lyout1.setSpacing(10)
        icon_label13_1 = QtWidgets.QLabel()
        
        icon_label13_1.setPixmap(icon_pixmap.scaled(15, 15, QtCore.Qt.KeepAspectRatio)) 
        icon_label13_1.setFixedSize(15, 15)
        self.num13_1 = QtWidgets.QLabel("44.29%")
        self.num13_1.setStyleSheet("color:rgb(255, 255, 255);font: 15pt \"微软雅黑\";background-color: transparent;font-weight: bold;")
        self.layout13_right_lyout1.addWidget(icon_label13_1)
        self.layout13_right_lyout1.addWidget(self.num13_1)
        self.layout13_right_txt2 = QtWidgets.QLabel("实际比")
        self.layout13_right_txt2.setAlignment(QtCore.Qt.AlignCenter)
        self.layout13_right_txt2.setStyleSheet("color:rgb(255, 255, 255);font: 11pt \"微软雅黑\";background-color: transparent;")
        self.layout13_right_lyout2 = QtWidgets.QHBoxLayout()
        self.layout13_right_lyout2.setAlignment(QtCore.Qt.AlignCenter)
        self.layout13_right_lyout2.setSpacing(10)
        icon_label13_2 = QtWidgets.QLabel()
        
        icon_label13_2.setPixmap(icon_pixmap.scaled(15, 15, QtCore.Qt.KeepAspectRatio)) 
        icon_label13_2.setFixedSize(15, 15)
        self.num13_2 = QtWidgets.QLabel("65.15%")
        self.num13_2.setStyleSheet("color:rgb(255, 255, 255);font: 15pt \"微软雅黑\";background-color: transparent;font-weight: bold;")
        self.layout13_right_lyout2.addWidget(icon_label13_2)
        self.layout13_right_lyout2.addWidget(self.num13_2)
        self.layout13_right.addWidget(self.layout13_right_txt1)
        self.layout13_right.addLayout(self.layout13_right_lyout1)
        self.layout13_right.addWidget(self.layout13_right_txt2)
        self.layout13_right.addLayout(self.layout13_right_lyout2)

        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.QWidget14 = self.SetQWidget("QWidget14", "./ui转换/border.png")
        self.QWidget14.setMaximumHeight(280)
        self.verticalLayout_14.addWidget(self.QWidget14)
        self.verticalLayout_6.addLayout(self.verticalLayout_14)
        self.layout14 = QtWidgets.QHBoxLayout(self.QWidget14)
        self.layout14.setSpacing(0)
        self.pichart14_1 = createpie4()
        self.pichart14_2 = createpie5()
        self.layout14.addWidget(self.pichart14_1)
        self.layout14.addWidget(self.pichart14_2)
        
        



        self.horizontalLayout_3.addWidget(self.verticalFrame_3)
        self.verticalLayout_2.addWidget(self.horizontalFrame)
    
    def updata_button9(self):
        # 检查哪个按钮被按下
        sender = self.sender()  # 获取发送信号的按钮
        if sender.isChecked():
            # 将其他按钮的背景颜色恢复为默认状态
            if sender != self.days_365:
                self.days_365.setChecked(False)
                self.days_365.setStyleSheet(self.styleSheet9)  # 恢复默认背景颜色
            if sender != self.days_90:
                self.days_90.setChecked(False)
                self.days_90.setStyleSheet(self.styleSheet9)  # 恢复默认背景颜色
            if sender != self.days_30:
                self.days_30.setChecked(False)
                self.days_30.setStyleSheet(self.styleSheet9)
            if sender != self.days_1:
                self.days_1.setChecked(False)
                self.days_1.setStyleSheet(self.styleSheet9)
            sender.setStyleSheet("""
                                 QPushButton{
                                        font: 12pt \"微软雅黑\";
                                        background-color: transparent;
                                        color: #ffffff;
                                    }
                                 """)
        else:
            sender.setStyleSheet(self.styleSheet9)
    def updata_button10(self):
        # 检查哪个按钮被按下
        sender = self.sender()  # 获取发送信号的按钮
        if sender.isChecked():
            # 将其他按钮的背景颜色恢复为默认状态
            if sender != self.year10:
                self.year10.setChecked(False)
                self.year10.setStyleSheet(self.button_style10)  # 恢复默认背景颜色
            if sender != self.month10:
                self.month10.setChecked(False)
                self.month10.setStyleSheet(self.button_style10)  # 恢复默认背景颜色
            if sender != self.season10:
                self.season10.setChecked(False)
                self.season10.setStyleSheet(self.button_style10)  # 恢复默认背景颜色

            # 设置当前按下的按钮背景为红色
            sender.setStyleSheet("""
        QPushButton{
            background-color: #333fff;
            color: #ffffff;
            font: 15pt \"微软雅黑\";
            border= 0px;
            border-radius: 5px;
        }
        QPushButton:pressed{
            border= 0px;
            border-radius: 5px;
            background-color: #333fff;
            color: #ffffff;
        }
        """)
        else:
            # 如果按钮取消选中，则恢复默认背景
            sender.setStyleSheet(self.button_style10)


    def update_data1(self):
        self.data_fetch_thread.start()

    def update_labels(self,data):
        if data:
        # 假设只显示第一个数据项的信息
            first_data = data
            self.label1.setText(f'生产总数: {first_data["data_list"]}')
            self.label2.setText(f'新增生产: {first_data["data_list"]}')
            self.label3.setText(f'待生产: {first_data["data_list"]}')


    def update_data8(self):
        self.data_fetch_thread8.start()
    def update_labels8(self,datas):
        self.table8.setHorizontalHeaderLabels(datas["head"])  # 设置表头
        # 填充数据
        production_data = datas["data_list"]
        
     
        for row_index, row_data in enumerate(production_data):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(col_data)
                #禁止编辑
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.table8.setItem(row_index, col_index, item)

    

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
