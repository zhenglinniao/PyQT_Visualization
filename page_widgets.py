from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import pyqtgraph as pg


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
        # self.verticalLayout_6.setSpacing(0)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
       # 创建一个QFrame对象，并将其添加到page_widgets中
        self.frame = QFrame(self.page_widgets)
        # 设置对象的名称为"frame"
        self.frame.setObjectName(u"frame")
        # 设置对象的形状为StyledPanel
        self.frame.setStyleSheet(u"background-color: rgb(2, 45, 222); border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        # 设置对象的阴影为Raised
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_frame_1V = QVBoxLayout(self.frame)
        self.verticalLayout_frame_1V.setSpacing(0)
        self.verticalLayout_frame_1V.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_frame_1H = QHBoxLayout()  # 这里不再把布局绑定到 self.frame

        self.title_frame = QLabel()
        self.title_frame.setAlignment(Qt.AlignCenter)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setText("Title Frame")
        self.title_frame.setStyleSheet(u"background-color: rgb(211, 45, 222); border-radius: 5px;")
        self.title_frame.setFont(font1)
        self.verticalLayout_frame_1V.addWidget(self.title_frame)

        # Frame1 with TextEdit
        self.frame1_textedit = QFrame(self.frame)
        self.frame1_layout = QVBoxLayout(self.frame1_textedit)  # 添加布局到 frame1_textedit
        self.Text_edit1 = QTextEdit(self.frame1_textedit)
        self.Text_edit1.setObjectName(u"Text_edit1")
        self.Text_edit1.setText("huanyan boat")
        self.Text_edit1.setFont(font1)
        self.Text_edit1.setStyleSheet(u"QTextEdit{\n"
                                "background-color: #ffffff;\n"
                                "border-radius: 5px;\n"
                                "}\n"
                                "QTextEdit:hover{\n"
                                "border: 2px solid rgb(222, 115, 56);\n"
                                "}\n"
                                "QTextEdit:focus{\n"
                                "border: 2px solid rgb(22, 115, 56);\n"
                                "}\n")
        self.frame1_layout.addWidget(self.Text_edit1)  # 将 TextEdit 添加到 frame1_layout

        # Frame2 with TextEdit
        self.frame2_textedit = QFrame(self.frame)
        self.frame2_layout = QVBoxLayout(self.frame2_textedit)  # 添加布局到 frame2_textedit
        self.Text_edit2 = QTextEdit(self.frame2_textedit)
        self.Text_edit2.setObjectName(u"Text_edit2")
        self.Text_edit2.setFont(font1)
        self.Text_edit2.setText("江苏省镇江市")
        self.Text_edit2.setStyleSheet(u"QTextEdit{\n"
                                "background-color: #ffffff;\n"
                                "border-radius: 5px;\n"
                                "}\n"
                                "QTextEdit:hover{\n"
                                "border: 2px solid rgb(222, 15, 56);\n"
                                "}\n"
                                "QTextEdit:focus{\n"
                                "border: 2px solid rgb(22, 115, 56);\n"
                                "}\n")
        self.frame2_layout.addWidget(self.Text_edit2)  # 将 TextEdit 添加到 frame2_layout

        # 添加两个 frame 到 horizontal layout
        self.verticalLayout_frame_1H.addWidget(self.frame1_textedit)
        self.verticalLayout_frame_1H.addWidget(self.frame2_textedit)

        # 将 horizontal layout 添加到 vertical layout
        self.verticalLayout_frame_1V.addLayout(self.verticalLayout_frame_1H)
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
        # self.horizontalLayout_12.setSpacing(0)
        # 设置水平布局的名称为"horizontalLayout_12"
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        # 设置水平布局的外边距为0
          
        self.verticalLayout_6.addWidget(self.frame_3)

        
        
        self.content_1 = QFrame(self.frame_3)
        self.content_1.setStyleSheet(u"background-color: #A0A0A0;border-radius: 5px;")  # 正确的白色
        self.content_2 = QFrame(self.frame_3)
        self.content_2.setStyleSheet(u"background-color: #606060;border-radius: 5px;")  # 正确的白色
        self.content_3 = QFrame(self.frame_3)
        self.content_3.setStyleSheet(u"background-color: #202020;border-radius: 5px;")  # 正确的白色
        self.horizontalLayout_12.addWidget(self.content_1)
        self.horizontalLayout_12.addWidget(self.content_2)
        self.horizontalLayout_12.addWidget(self.content_3)



        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.page_widgets)
#+________________________________________________________________________   

if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    
    # 将init_page_widgets添加到主窗口
    widget = init_page_widgets()
    # 设置窗口大小
    widget.resize(1000, 720)
    widget.show()
    sys.exit(app.exec_())
    