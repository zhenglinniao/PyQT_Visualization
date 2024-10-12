import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl
from PySide2.QtCore import Qt
import os

class MainWindow_Html(QWidget):
    def __init__(self):
        super().__init__()

        
        layout = QVBoxLayout(self)

        # 创建 QWebEngineView 实例
        self.web_view1 = QWebEngineView()

        # 将 QWebEngineView 和按钮添加到布局中
        layout.addWidget(self.web_view1)
  
        
        file_path = os.path.abspath('pyqt配合js/index.html')
        print(file_path)
        self.default_file_url = QUrl.fromLocalFile(file_path)
        self.web_view1.load(self.default_file_url)
# 创建应用程序和主窗口

if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MainWindow_Html()
        window.setWindowTitle('加载和选择 HTML 文件')
        #全屏展示
        window.showMaximized()
        # window.setWindowFlag(Qt.FramelessWindowHint) # 隐藏边框
        window.resize(800, 600)
        window.show()

        # 运行应用程序的事件循环
        sys.exit(app.exec_())
