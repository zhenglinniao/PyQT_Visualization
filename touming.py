import sys
from PySide2.QtWidgets import QApplication, QWidget, QFrame, QGridLayout, QLabel

class Background(QWidget):
    def __init__(self, parent=None):
        super(Background, self).__init__(parent)
        
        # 创建一个 QFrame，作为背景
        self.frame = QFrame(self)
        self.frame.setStyleSheet("background-color: blue; border: 1px solid black;")

        # 创建一个 QGridLayout，添加到 QFrame
        self.layout = QGridLayout(self.frame)

        # 创建 QLabel
        self.setbel_1 = QLabel("Hello, World!", self)
        self.setbel_1.setStyleSheet("color: white; font-size: 20px;background-color: red;")
        self.setbel_2 = QLabel("Hello, World!", self)
        self.setbel_2.setStyleSheet("color: white; font-size: 20px;")
        self.setbel_3 = QLabel("Hello, World!", self)
        self.setbel_3.setStyleSheet("color: white; font-size: 20px;")

        # 将 QLabel 添加到 QGridLayout 中
        self.layout.addWidget(self.setbel_1, 0, 0)
        self.layout.addWidget(self.setbel_2, 1, 0)
        self.layout.addWidget(self.setbel_3, 2, 0)

   

        # 将 QFrame 添加到主窗口布局中
        main_layout = QGridLayout(self)  # 创建主窗口的布局
        main_layout.addWidget(self.frame)  # 将 QFrame 添加到主布局中
        self.setLayout(main_layout)  # 设置主窗口的布局

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Background()
    ex.resize(400, 300)  # 设置窗口大小
    ex.show()
    sys.exit(app.exec_())
