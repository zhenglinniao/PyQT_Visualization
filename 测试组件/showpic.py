from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPalette, QBrush, QColor, QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multiple Backgrounds Example")
        self.setGeometry(100, 100, 800, 600)

        # 创建主部件和布局
        main_widget = QWidget(self)
        layout = QVBoxLayout(main_widget)

        # 创建第一个背景的 QWidget
        first_background = QWidget()
        first_background.setMinimumHeight(200)  # 设置高度以便看到效果
        first_palette = QPalette()
        first_palette.setBrush(QPalette.Background, QBrush(QColor(255, 0, 0)))  # 红色背景
        first_background.setPalette(first_palette)
        first_background.setAutoFillBackground(True)

        # 添加到布局
        layout.addWidget(first_background)

        # 创建第二个背景的 QWidget
        second_background = QWidget()
        second_background.setMinimumHeight(200)  # 设置高度以便看到效果
        second_palette = QPalette()
        second_palette.setBrush(QPalette.Background, QBrush(QColor(0, 255, 0)))  # 绿色背景
        second_background.setPalette(second_palette)
        second_background.setAutoFillBackground(True)

        # 添加到布局
        layout.addWidget(second_background)

        # 创建第三个背景的 QWidget
        third_background = QWidget()
        third_background.setMinimumHeight(200)  # 设置高度以便看到效果
        third_palette = QPalette()
        third_palette.setBrush(QPalette.Background, QBrush(QColor(0, 0, 255)))  # 蓝色背景
        third_background.setPalette(third_palette)
        third_background.setAutoFillBackground(True)

        # 添加到布局
        layout.addWidget(third_background)

        # 设置主窗口的中央小部件
        self.setCentralWidget(main_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
