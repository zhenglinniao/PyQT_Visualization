from PySide2 import QtCore, QtGui, QtWidgets
import random
import sys
from PySide2.QtWidgets import QApplication, QWidget, QFrame, QGridLayout, QLabel
try:
    from PySide2.QtChart import (QAreaSeries, QBarSet, QChart, QChartView,
                               QLineSeries, QPieSeries, QScatterSeries, QSplineSeries,
                               QStackedBarSeries)
    from PySide2.QtCore import pyqtSlot, QPointF, Qt
    from PySide2.QtGui import QColor, QPainter, QPalette
    from PySide2.QtWidgets import QApplication, QMainWindow, QCheckBox, QComboBox, QGridLayout, QHBoxLayout, \
        QLabel, QSizePolicy, QWidget
except ImportError:
    from PySide2.QtCore import Slot as pyqtSlot, QPointF, Qt
    from PySide2.QtGui import QColor, QPainter, QPalette
    from PySide2.QtWidgets import QApplication, QMainWindow, QCheckBox, QComboBox, QGridLayout, QHBoxLayout, \
        QLabel, QSizePolicy, QWidget
    from PySide2.QtCharts import QtCharts

    QChartView = QtCharts.QChartView
    QChart = QtCharts.QChart
    QAreaSeries = QtCharts.QAreaSeries
    QBarSet = QtCharts.QBarSet
    QLineSeries = QtCharts.QLineSeries
    QPieSeries = QtCharts.QPieSeries
    QScatterSeries = QtCharts.QScatterSeries
    QSplineSeries = QtCharts.QSplineSeries
    QStackedBarSeries = QtCharts.QStackedBarSeries
    QCategoryAxis = QtCharts.QCategoryAxis


class ChartView(QChartView):
    def __init__(self, parent=None):
        super(ChartView, self).__init__(parent)
        self._chart = QChart()
        self.setChart(self._chart)

        # 创建线型图数据序列
        series = QLineSeries()
        # 添加数据，假设这是每天的数据
        series.append(0, 23)
        series.append(1, 16)
        series.append(2, 5)
        series.append(3, 33)
        series.append(4, 18)
        series.append(5, 29)
        series.append(6, 25)

        self._chart.addSeries(series)
        self._chart.createDefaultAxes()

        # 创建 QCategoryAxis 作为 X 轴，设置星期作为标签
        axis_x = QCategoryAxis(self._chart, labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue)
        axis_x.append("星期一", 0)
        axis_x.append("星期二", 1)
        axis_x.append("星期三", 2)
        axis_x.append("星期四", 3)
        axis_x.append("星期五", 4)
        axis_x.append("星期六", 5)
        axis_x.append("星期日", 6)

        # 设置 X 轴的范围
        axis_x.setRange(0, 6)
        
        # 将 X 轴应用到图表
        self._chart.setAxisX(axis_x, series)


        

        # 设置图表标题和样式
        self._chart.setTitle("每周数据线型图")
        self.setRenderHint(QPainter.Antialiasing)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chart_view = ChartView()
    chart_view.show()
    sys.exit(app.exec_())
