
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PySide2.QtGui import QColor, QPalette
from PySide2.QtCore import Signal
from PySide2.QtCore import Qt
class ColorChangeWindow(QWidget):
    # 定义一个信号，用于传递选中的颜色
    color_changed = Signal(QColor)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉边框

        # 假设有一个按钮可以用来选择颜色
        self.button = QPushButton("选择颜色", self)
        self.button.clicked.connect(self.choose_color)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def choose_color(self):
        # 这里可以使用 QColorDialog 让用户选择颜色
        color = QColor(255, 0, 0)  # 示例：红色
        self.color_changed.emit(color)  # 发出信号，传递选择的颜色
        self.close()  # 关闭调色板窗口

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("主窗口")
        self.setGeometry(100, 100, 800, 600)

        self.color_change_window = ColorChangeWindow(self)
        self.color_change_window.color_changed.connect(self.change_background)  # 连接信号

        self.button = QPushButton("打开调色板", self)
        self.button.clicked.connect(self.open_color_change_window)
        self.button.setGeometry(10, 10, 150, 30)

    def open_color_change_window(self):
        self.color_change_window.show()

    def change_background(self, color):
        # 更改主窗口的背景颜色
        palette = QPalette()
        palette.setColor(QPalette.Window, color)
        self.setPalette(palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
