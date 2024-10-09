# -*- coding: utf-8 -*-

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
from PySide2.QtGui import QPalette, QBrush, QPixmap
from PySide2.QtCore import Qt


class main_ui(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化窗口
        self.setWindowTitle("MainWindow")
        self.setGeometry(100, 100, 1940, 813)
        self.setStyleSheet("background:rgb(16, 17, 41)")

        # 创建布局
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)

        # 创建顶部的 logo 帧
        self.verticalFrame = QtWidgets.QFrame(self)
        self.verticalFrame.setMaximumSize(QtCore.QSize(16777215, 130))
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.verticalFrame)
        self.label = QtWidgets.QLabel(self.verticalFrame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 130))
        self.label.setPixmap(QtGui.QPixmap("C:/Users/ZJB-24082001/Downloads/【框架】可视化大屏 (1)/logo.png"))
        self.label.setScaledContents(True)
        self.horizontalLayout_9.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.verticalFrame)

        # 创建内容的水平布局
        self.horizontalFrame = QtWidgets.QFrame(self)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame)

        # 创建左边的垂直布局
        self.verticalFrame1 = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.addWidget(self.SetQWidget("QWidget", "C:/Users/ZJB-24082001/Downloads/【框架】可视化大屏 (1)/border.png"))
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.addWidget(self.SetQWidget("QWidget16", "C:/Users/ZJB-24082001/Downloads/【框架】可视化大屏 (1)/border.png"))
        self.verticalLayout_3.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.addWidget(self.SetQWidget("QWidget17", "C:/Users/ZJB-24082001/Downloads/【框架】可视化大屏 (1)/border.png"))
        self.verticalLayout_3.addLayout(self.verticalLayout_17)

        self.horizontalLayout_3.addWidget(self.verticalFrame1)

        # 中间内容布局
        self.verticalFrame_2 = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.addWidget(self.SetQWidget("QWidget8", ""))
        self.verticalLayout_5.addLayout(self.verticalLayout_8)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.addWidget(self.SetQWidget("QWidget2", "C:/Users/ZJB-24082001/Downloads/【框架】可视化大屏 (1)/border.png"))
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3.addWidget(self.verticalFrame_2)

        # 右边内容布局
        self.verticalFrame_3 = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.addWidget(self.SetQWidget("QWidget9", "C:/Users/ZJB-24082001/Downloads/【框架】可视化大屏 (1)/border.png"))
        self.verticalLayout_6.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.addWidget(self.SetQWidget("QWidget10", "C:/Users/ZJB-24082001/Downloads/【框架】可视化大屏 (1)/border.png"))
        self.verticalLayout_6.addLayout(self.verticalLayout_10)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.addWidget(self.SetQWidget("QWidget11", "C:/Users/ZJB-24082001/Downloads/【框架】可视化大屏 (1)/border.png"))
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)

        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.addWidget(self.SetQWidget("QWidget13", "C:/Users/ZJB-24082001/Downloads/【框架】可视化大屏 (1)/border.png"))
        self.horizontalLayout_5.addLayout(self.verticalLayout_13)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.addWidget(self.SetQWidget("QWidget14", "C:/Users/ZJB-24082001/Downloads/【框架】可视化大屏 (1)/border.png"))
        self.verticalLayout_6.addLayout(self.verticalLayout_14)

        self.horizontalLayout_3.addWidget(self.verticalFrame_3)

        self.verticalLayout_2.addWidget(self.horizontalFrame)

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
            pixmap = QPixmap(image_path).scaled(widget.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            first_palette.setBrush(QPalette.Background, QBrush(pixmap))
            widget.setPalette(first_palette)
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
