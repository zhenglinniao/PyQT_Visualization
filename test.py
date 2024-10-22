import sys
from PySide2 import QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("调整标签间隙示例")
        self.setGeometry(100, 100, 600, 400)

        # 设置主布局
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setSpacing(2)  # 设置竖直方向的间隔为2像素
        main_layout.setContentsMargins(0, 0, 0, 0)  # 设置布局边距为0

        # 按钮和标签
        self.but1 = QtWidgets.QPushButton()
        self.but1.setFixedSize(15, 15)
        self.label1 = QtWidgets.QLabel("生产总数：")
        self.text1 = QtWidgets.QLabel("100")

        self.but2 = QtWidgets.QPushButton()
        self.but2.setFixedSize(15, 15)
        self.label2 = QtWidgets.QLabel("新增生产：")
        self.text2 = QtWidgets.QLabel("200")

        self.but3 = QtWidgets.QPushButton()
        self.but3.setFixedSize(15, 15)
        self.label3 = QtWidgets.QLabel("待生产：")
        self.text3 = QtWidgets.QLabel("300")

        # 添加布局
        layout1 = QtWidgets.QHBoxLayout()
        layout1.addWidget(self.but1)
        layout1.addWidget(self.label1)
        layout1.addWidget(self.text1)
        main_layout.addLayout(layout1)

        layout2 = QtWidgets.QHBoxLayout()
        layout2.addWidget(self.but2)
        layout2.addWidget(self.label2)
        layout2.addWidget(self.text2)
        main_layout.addLayout(layout2)

        layout3 = QtWidgets.QHBoxLayout()
        layout3.addWidget(self.but3)
        layout3.addWidget(self.label3)
        layout3.addWidget(self.text3)
        main_layout.addLayout(layout3)

        # 设置主布局
        self.setLayout(main_layout)

# 主程序入口
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
