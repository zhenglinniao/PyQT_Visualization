import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置无边框和透明背景
        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明背景

        # 设置窗口大小和标题
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Transparent Window')

        # 创建一个中央控件和布局
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # 添加一个标签（QLabel）到窗口
        label = QLabel('这是一个透明窗口上的标签', self)
        label.setStyleSheet("color: red; font-size: 18px;")  # 设置标签样式
        label.setAlignment(Qt.AlignCenter)  # 居中对齐
        layout.addWidget(label)

        # 添加一个按钮（QPushButton）到窗口
        button = QPushButton('点击我', self)
        button.setStyleSheet("background-color: rgba(255, 255, 255, 0.5); color: black;")
        layout.addWidget(button)

        # 创建数据集
        set0 = QBarSet("类别 A")
        set1 = QBarSet("类别 B")
        set2 = QBarSet("类别 C")

        # 给数据集添加数据
        set0 << 1 << 2 << 3 << 4 << 5
        set1 << 5 << 0 << 0 << 4 << 1
        set2 << 3 << 5 << 8 << 13 << 8

        # 创建 QBarSeries 并添加数据集
        series = QBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)

        # 创建 QChart 对象并添加系列
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("简单柱状图示例")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # 创建类别轴并设置类别
        categories = ["一月", "二月", "三月", "四月", "五月"]
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        chart.setAxisX(axisX, series)
        chart.setBackgroundBrush(Qt.transparent)  # 设置背景透明
        # chart.setBackgroundVisible (False)  # 设置背景不可见

        # 创建 QChartView 以显示图表
        chart_view = QChartView(chart)
 # 设置渲染提示，启用抗锯齿
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart_view.setStyleSheet("background-color: transparent;")  # 设置背景透明
        layout.addWidget(chart_view)  # 将 chart_view 添加到布局中

        # 将中央控件设置为窗口的中央部件
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
    window.show()
    sys.exit(app.exec_())
