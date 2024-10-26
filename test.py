from PyQt5 import QtWidgets, QtGui, QtCore

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)

        # 创建水平布局
        layout = QtWidgets.QHBoxLayout(self)

        # 创建 QLabel 用于显示图标
        icon_label = QtWidgets.QLabel()
        icon_pixmap = QtGui.QPixmap("icons/16x16/cil-3d.png")  # 替换为您的图标路径
        icon_label.setPixmap(icon_pixmap.scaled(32, 32, QtCore.Qt.KeepAspectRatio))  # 调整图标大小
        

        # 创建 QLabel 用于显示文本
        text_label = QtWidgets.QLabel("这是一个带图标的文本")

        # 将图标和文本添加到布局中
        layout.addWidget(icon_label)
        layout.addWidget(text_label)

        self.setLayout(layout)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
