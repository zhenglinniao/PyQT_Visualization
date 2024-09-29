import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QColorDialog
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt


class ColorChangeWindow(QWidget):
    def __init__(self):
        super().__init__()



        # 初始化UI
        # 布局
        layout = QVBoxLayout()
        self.button = QPushButton(self)
        self.button.setFixedSize(15, 15)  # 设置按钮大小
        self.button.setStyleSheet("QPushButton{\n"
                                  "border-radius: 5px; background-color: rgb(100, 100, 100);\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color: rgb(150, 150, 50);\n"
                                  "}\n")  # 设置为圆形
        self.button.clicked.connect(self.show_color_dialog)  # 连接按钮点击事件
        layout.addWidget(self.button)

        # 设置布局
        self.setLayout(layout)

    def show_color_dialog(self):
        # 弹出调色板
        color_dialog = QColorDialog()
        color = color_dialog.getColor()
        # color_dialog.setWindowFlags(Qt.FramelessWindowHint)  咩用

        if color.isValid():
            # 如果颜色有效，则设置窗口的背景颜色
            self.setStyleSheet(f"background-color: {color.name()};")


if __name__ == "__main__":
    # 创建应用程序
    app = QApplication(sys.argv)

    # 创建主窗口
    window = ColorChangeWindow()
    window.setWindowTitle("调色板示例")
    window.resize(400, 300)
    # window.setWindowFlags(Qt.FramelessWindowHint)  # 去掉窗口边框
    window.show()

    # 进入主循环
    sys.exit(app.exec_())
