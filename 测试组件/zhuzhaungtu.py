import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
class BarChartExample(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("QBarSeries 示例")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框窗口
        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明背景

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

        # 创建 QChartView 以显示图表
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # 创建一个中央控件并设置布局
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(chart_view)

        # 设置一个文本标签
        label = QLabel("这是一个文本标签")
        layout.addWidget(label)
        

        # 设置窗口的中心部件
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BarChartExample()
    # window.setWindowFlags(Qt.FramelessWindowHint)
    window.show()
    sys.exit(app.exec_())
