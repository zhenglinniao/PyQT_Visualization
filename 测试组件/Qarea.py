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
        #面积图的上下两条曲线
        #注意line0和line1的生存周期!!!!!
        self.line0 = QLineSeries()
        self.line1 = QLineSeries()
        
        self.line0 << QPointF(1, 5) << QPointF(3, 7) << QPointF(7, 6) << QPointF(9, 7) << QPointF(12, 6) << QPointF(16, 7) << QPointF(18, 5)
        self.line1 << QPointF(1, 3) << QPointF(3, 4) << QPointF(7, 3) << QPointF(8, 2) << QPointF(12, 3) << QPointF(16, 4) << QPointF(18, 3)
        
        #面积图
        areaSeries = QAreaSeries(self.line0, self.line1)
        areaSeries.setName('蝙蝠侠') #Batman
        
        pen = QPen(QColor(0x059605))
        pen.setWidth(3)
        areaSeries.setPen(pen)
        
        #渐变设置
        
            
        #创建图表
        chart = QChart()
        chart.addSeries(areaSeries)
        chart.setTitle('简单面积图示例')
        chart.createDefaultAxes()
        chart.axes(Qt.Horizontal)[0].setRange(0, 20) #横坐标数值范围
        chart.axes(Qt.Vertical)[0].setRange(0, 10) #纵坐标数值范围
        chart.setBackgroundBrush(QColor(0, 0, 0, 0))
        chart.setBackgroundVisible(False)
        
        #图表视图
        chartView = QChartView(chart)
        chartView.setStyleSheet("background-color:rgba(0,0,0,0);");
        chartView.setRenderHint(QPainter.Antialiasing)
        
        self.setCentralWidget(chartView)
    
        
    

if __name__ == "__main__":
    print("Starting application...")
    app = QApplication(sys.argv)
    window = AreaChartExample()
    window.show()  # 确保窗口显示
    sys.exit(app.exec_())
