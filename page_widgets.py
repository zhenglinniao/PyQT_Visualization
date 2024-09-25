from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import pyqtgraph as pg
import files_rc

class init_page_widgets(QWidget):
    def __init__(self):
        super().__init__()
         # 设置无边框窗口
        # self.setWindowFlags(Qt.FramelessWindowHint)
        
       
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.page_widgets.setStyleSheet(u"background-color: transparent;")
        
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 创建一个QFrame对象，并将其添加到page_widgets中
        self.frame = QFrame(self.page_widgets)
        # 设置对象的名称为"frame"
        self.frame.setObjectName(u"frame")
        # 设置对象的样式为边框半径为5px
        self.frame.setStyleSheet(u"border-radius: 5px;")
        # 设置对象的形状为StyledPanel
        self.frame.setStyleSheet(u"background-color: rgb(2, 45, 222);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        # 设置对象的阴影为Raised
        self.frame.setFrameShadow(QFrame.Raised)
        
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)

        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
                                        "border-radius: 5px;\n")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        # Frame Title Widget
        self.frame_title_wid = QFrame(self.frame_div_content_1)
        self.frame_title_wid.setStyleSheet(u"background-color: rgb(222, 44, 54);")
        self.frame_title_wid.setMinimumHeight(25)
        self.title_layout = QVBoxLayout(self.frame_title_wid)
 # 设置标题布局的边距为
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        self.title_frame = QLabel(self.frame_title_wid)
        self.title_frame.setAlignment(Qt.AlignCenter)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setText("Title Frame")
        self.title_frame.setFont(font1)
        self.title_layout.addWidget(self.title_frame)
        self.verticalLayout_7.addWidget(self.frame_title_wid)

        # Text Edit Layout
        self.edit_frame = QFrame(self.frame_div_content_1)
        self.edit_frame.setMinimumHeight(100)
        self.layout_VH = QHBoxLayout(self.edit_frame)
        self.Text_edit1 = QTextEdit(self.frame_div_content_1)
        self.Text_edit1.setObjectName(u"Text_edit1")
        self.Text_edit1.setFont(font1)
        self.Text_edit1.setStyleSheet(u"QTextEdit{\n"
                                "background-color: rgb(0, 45, 56);\n"
                                "border-radius: 5px;\n"
                                "border: 2px solid rgb(222, 115, 56);\n"
                                "padding-left: 5px;\n"
                                "padding-right: 5px;\n"
                                "}")
        self.Text_edit2 = QTextEdit(self.frame_div_content_1)
        self.Text_edit2.setObjectName(u"Text_edit2")
        self.Text_edit2.setFont(font1)
        self.Text_edit2.setStyleSheet(u"QTextEdit{\n"
                                "background-color: rgb(0, 45, 56);\n"
                                "border-radius: 5px;\n"
                                "border: 2px solid rgb(22, 45, 56);\n"
                                "padding-left: 5px;\n"
                                "padding-right: 5px;\n"
                                "}")
        self.layout_VH.addWidget(self.Text_edit1)
        self.layout_VH.addWidget(self.Text_edit2)
        self.verticalLayout_7.addWidget(self.edit_frame)
        self.verticalLayout_15.addWidget(self.frame_div_content_1)
        self.verticalLayout_6.addWidget(self.frame)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.frame_2 = QFrame(self.page_widgets)
        self.frame_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.frame_2.setObjectName(u"frame_2")
        # self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 144, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")

        self.content = QFrame(self.frame_2)
        self.content.setMinimumHeight(150)
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.content.setStyleSheet(u"background-color: #ffffff;border-radius: 5px;")  # 正确的白色
        
        
        # 添加frame到布局
        self.verticalLayout_11.addWidget(self.content)


        self.verticalLayout_6.addWidget(self.frame_2)
#-----------------------------------------------------------------
        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setStyleSheet(u"background-color: rgb(39, 144, 154);\n"
                                   "border-radius: 5px;")
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        # 设置水平布局的间距为0
        self.horizontalLayout_12.setSpacing(0)
        # 设置水平布局的名称为"horizontalLayout_12"
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        # 设置水平布局的外边距为0
          


        self.content2 = QFrame(self.frame_3)
        self.content2.setMinimumHeight(150)
        self.content2.setFrameShape(QFrame.StyledPanel)
        self.content2.setFrameShadow(QFrame.Raised)
        self.content2.setStyleSheet(u"background-color: #ff22;border-radius: 5px;")  # 正确的白色
        self.content_layout = QHBoxLayout(self.content2)
        self.content_1 = QFrame(self.content2)
        self.content_1.setStyleSheet(u"background-color: #A0A0A0;border-radius: 5px;")  # 正确的白色
        self.content_2 = QFrame(self.content2)
        self.content_2.setStyleSheet(u"background-color: #606060;border-radius: 5px;")  # 正确的白色
        self.content_3 = QFrame(self.content2)
        self.content_3.setStyleSheet(u"background-color: #202020;border-radius: 5px;")  # 正确的白色
        self.content_layout.addWidget(self.content_1)
        self.content_layout.addWidget(self.content_2)
        self.content_layout.addWidget(self.content_3)

        self.content_layout.addWidget(self.content_1)
        self.horizontalLayout_12.addWidget(self.content2)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.page_widgets)
#+________________________________________________________________________   

if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    
  
   

    # 将init_page_widgets添加到主窗口
    widget = init_page_widgets()
    widget.show()
    sys.exit(app.exec_())