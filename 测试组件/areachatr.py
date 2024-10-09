import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QAreaSeries,QBarCategoryAxis,QBarSet,QBarSeries
from PyQt5.QtGui import QPen, QBrush, QPainter,QColor
from PyQt5.QtCore import Qt,QPointF

class AreaChartExample(QMainWindow):
    def __init__(self):
        super().__init__()

        print("Initializing the window...")
        # 设置窗口标题和大小
        self.setWindowTitle("QAreaSeries 示例")
        self.resize(480, 360)

     
        self.series1 = QLineSeries()
        self.series2 = QLineSeries()
        self.series1 << QPointF(1, 5) << QPointF(3, 7) << QPointF(7, 6) << QPointF(9, 7) << QPointF(12, 6) << QPointF(16, 7) << QPointF(18, 5)
        self.series2 << QPointF(1, 6) << QPointF(2, 4) << QPointF(7, 8) << QPointF(8, 2) << QPointF(12, 3) << QPointF(16, 4) << QPointF(18, 3)
        
        

        # 使用 QAreaSeries 创建区域系列
        print("Creating area series...")
        area_series = QAreaSeries(self.series1, self.series2)

        # 设置画笔和画刷
        pen = QPen(QColor(255, 0, 0, 200))
        pen.setWidth(2)
        area_series.setPen(pen)
      
      

        # 创建 QChart 对象并添加系列
        print("Creating chart...")
        chart = QChart()
        chart.addSeries(area_series)
        chart.setTitle("QAreaSeries 示例")
        chart.createDefaultAxes()  # 创建默认的坐标轴
        
        chart.axes(Qt.Horizontal)[0].setRange(0, 20) #横坐标数值范围
        chart.axes(Qt.Vertical)[0].setRange(0, 10) #纵坐标数值范围
         
        # 创建 QChartView 以显示图表
        print("Creating chart view...")
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)  # 启用抗锯齿

        # 创建一个中央控件并设置布局
        
        # layout.addWidget(chart_view)
  

        # 设置窗口的中心部件
        self.setCentralWidget(chart_view)
        print("Initialization finished.")

if __name__ == "__main__":
    print("Starting application...")
    app = QApplication(sys.argv)
    window = AreaChartExample()
    window.show()  # 确保窗口显示
    sys.exit(app.exec_())
