from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个 QLabel 来显示图片
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.width(), self.height())

        # 加载图片并设置为 QLabel 的背景
        self.pixmap = QPixmap("C:/Users/ZJB-24082001/Downloads/【框架】可视化大屏 (1)/logo.png")
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)  # 自动缩放图片以适应窗口大小
    
        

    def resizeEvent(self, event):
        # 调整 QLabel 大小以适应窗口大小
        self.label.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())