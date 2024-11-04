from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtGui import QFont, QPainter
from PyQt5.QtCore import Qt, QSize
import sys

class LineChart(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.series = QLineSeries()
        self.series.append(0, 6)
        self.series.append(2, 4)
        self.series.append(3, 8)
        self.series.append(7, 4)
        self.series.append(10, 5)

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("动态调整标题和标注")
        self.chart.createDefaultAxes()

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        layout = QVBoxLayout()
        layout.addWidget(self.chart_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # 初始化字体
        self.update_font()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_font()

    def update_font(self):
        # 根据窗口大小设置字体大小
        font_size = max(10, self.width() // 30)
        title_font = QFont("Arial", font_size, QFont.Bold)
        legend_font = QFont("Arial", font_size - 2)
        
        self.chart.setTitleFont(title_font)
        self.chart.legend().setFont(legend_font)

app = QApplication(sys.argv)
window = LineChart()
window.resize(640, 480)
window.show()
sys.exit(app.exec_())
