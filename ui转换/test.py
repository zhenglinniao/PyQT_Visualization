from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QFont, QBrush, QColor
from PySide2.QtCore import Qt

class PieChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("饼图示例")
        
        # 创建一个 QWidget 作为主窗口的中心组件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 创建 QVBoxLayout 布局
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        # 创建饼图数据系列
        self.series = QtCharts.QPieSeries()
        self.series.append("类别 A", 40)
        self.series.append("类别 B", 30)
        self.series.append("类别 C", 20)
        self.series.append("类别 D", 10)
        
        # 遍历每个扇叶，显示类别和数值，并设置字体颜色
        colors = [QColor("#ff9999"), QColor("#99ff99"), QColor("#9999ff"), QColor("#ffcc99")]  # 自定义颜色
        for index, slice in enumerate(self.series.slices()):
            value = slice.value()  # 获取数值
            slice.setLabel(f"{slice.label()} {int(value)}")  # 设置标签为 "类别 名称 + 数值"
            slice.setLabelVisible(True)  # 显示标签
            slice.setLabelColor(Qt.white)  # 设置标签颜色
            slice.setLabelPosition(QtCharts.QPieSlice.LabelInsideHorizontal)  # 标签显示在扇叶内侧
            
            # 设置扇叶颜色
            brush = QBrush(colors[index])
            slice.setBrush(brush)
        
        
        # 创建图表并添加数据系列
        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("设备分布")  # 图表标题
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)  # 设置动画

        # 创建 QChartView 以显示图表
        self.chart_view = QtCharts.QChartView(self.chart)

        
        # 将图表视图添加到布局中
        self.layout.addWidget(self.chart_view)

if __name__ == "__main__":
    app = QApplication([])
    window = PieChartWindow()
    window.show()
    app.exec_()
