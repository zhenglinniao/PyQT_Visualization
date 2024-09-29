from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PySide2 import QtCore
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.le = QLineEdit(self)
        self.le.setPlaceholderText("双击我")

        layout = QVBoxLayout()
        layout.addWidget(self.le)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.le.installEventFilter(self)  # 安装事件过滤器

    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())  # 打印鼠标双击位置
        return super().eventFilter(watched, event)  # 允许事件继续传播

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
