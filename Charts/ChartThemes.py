#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Createon : 2024年9月24日
@author: kid
@contact: zhenglinniao1417@gamil.com
@file: LineStack.py
@desc: 图表展示
"""

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

class ThemeWidget(QWidget):
    def __init__(self, parent=None):
        super(ThemeWidget, self).__init__(parent)
        self.setupUi()  # 调用 setupUi 方法

    def setupUi(self):
        # 创建一个空列表，用于存储图表
        self.m_charts = []
        # 设置列表数量为3
        self.m_listCount = 3
        # 设置最大值为10
        self.m_valueMax = 10
        # 设置值数量为7
        self.m_valueCount = 7
        # 生成随机数据
        self.m_dataTable = self.generateRandomData(self.m_listCount,
                                                   self.m_valueMax, self.m_valueCount)
        # 创建主题下拉框
        self.m_themeComboBox = self.createThemeBox()

        # 创建动画下拉框
        self.m_animatedComboBox = self.createAnimationBox()
        # 创建图例下拉框
        self.m_legendComboBox = self.createLegendBox()
        # 连接信号
        self.connectSignals()
        # 创建内容区域
        # Create the layout.

        self.frame = QFrame(self)
        self.frame.setObjectName("mainFrame")
        # self.frame.setStyleSheet("#mainFrame { background-color: #f0f0f0; }")
        baseLayout = QGridLayout(self.frame)
    
        settingsLayout = QHBoxLayout()
        settingsLayout.addWidget(QLabel("Theme:"))
        settingsLayout.addWidget(self.m_themeComboBox)
        settingsLayout.addWidget(QLabel("Animation:"))
        settingsLayout.addWidget(self.m_animatedComboBox)
        settingsLayout.addWidget(QLabel("Legend:"))
        settingsLayout.addWidget(self.m_legendComboBox)

        # 添加一个拉伸组件，用于填充空白区域
        settingsLayout.addStretch()
        # 将设置布局添加到主布局中，位置为第0行第0列，占据1行3列
        baseLayout.addLayout(settingsLayout, 0, 0, 1, 3)

        # Create the charts.
        # 创建一个区域图，并将其添加到布局中
        chartView = QChartView(self.createAreaChart())
        chartView.setStyleSheet("background: transparent; border: none;")  # 设置无边框和透明背景
        baseLayout.addWidget(chartView, 1, 0)
        self.m_charts.append(chartView)

        # 创建一个柱状图，并将其添加到布局中
        chartView = QChartView(self.createBarChart(self.m_valueCount))
        chartView.setStyleSheet("background: transparent; border: none;")  # 设置无边框和透明背景
        baseLayout.addWidget(chartView, 1, 1)
        self.m_charts.append(chartView)

        # 创建一个折线图，并将其添加到布局中
        chartView = QChartView(self.createLineChart())
        chartView.setStyleSheet("background: transparent; border: none;")  # 设置无边框和透明背景
        baseLayout.addWidget(chartView, 1, 2)
        self.m_charts.append(chartView)

        # 创建一个饼图，并将其添加到布局中
        chartView = QChartView(self.createPieChart())
        chartView.setStyleSheet("background: transparent; border: none;")  # 设置无边框和透明背景
        # 如果饼图的切片标签不适应屏幕，会有奇怪的事情发生...
        # 设置chartView的大小策略为忽略
        chartView.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        # 将chartView添加到baseLayout中，位置为第2行第0列
        baseLayout.addWidget(chartView, 2, 0)
        # 将chartView添加到m_charts列表中
        self.m_charts.append(chartView)

        # 创建一个曲线图，并将其添加到布局中
        chartView = QChartView(self.createSplineChart())
        chartView.setStyleSheet("background: transparent; border: none;")  # 设置无边框和透明背景
        baseLayout.addWidget(chartView, 2, 1)
        self.m_charts.append(chartView)

        # 创建一个散点图，并将其添加到布局中
        chartView = QChartView(self.createScatterChart())
        chartView.setStyleSheet("background: transparent; border: none;")  # 设置无边框和透明背景
        baseLayout.addWidget(chartView, 2, 2)
        self.m_charts.append(chartView)

        # 设置布局
        # self.setLayout(baseLayout)
        main_layout = QGridLayout(self)  # 创建主窗口的布局
        main_layout.addWidget(self.frame)  # 将 QFrame 添加到主布局中
        self.setLayout(main_layout)  # 设置主窗口的布局
        # Set the defaults.
        # 设置默认值


        self.updateUI()
#触发器
    def connectSignals(self):
        self.m_themeComboBox.currentIndexChanged.connect(self.updateUI)
        self.m_animatedComboBox.currentIndexChanged.connect(self.updateUI)
        self.m_legendComboBox.currentIndexChanged.connect(self.updateUI)

#随机生成数据
    def generateRandomData(self, listCount, valueMax, valueCount):
        # 设置随机数种子
        random.seed()

        # 创建一个空的数据表
        dataTable = []

        # 循环listCount次
        for i in range(listCount):
            # 创建一个空的数据列表
            dataList = []
            # 初始化y值为0.0
            yValue = 0.0
            # 将valueCount转换为浮点数
            f_valueCount = float(valueCount)

            # 循环valueCount次    
            for j in range(valueCount):
                # 将y值加上一个0到valueMax之间的随机数除以f_valueCount
                yValue += random.uniform(0, valueMax) / f_valueCount
                # 创建一个QPointF对象，x值为j加上一个0到self.m_valueMax之间的随机数除以f_valueCount，y值为yValue
                value = QPointF(
                    j + random.random() * self.m_valueMax / f_valueCount,
                    yValue)
                # print(j + random.random() * self.m_valueMax / f_valueCount)
                # print("-------------\n")
                # print(yValue)
                # 创建一个标签，格式为"Slice i:j"
                label = "Slice " + str(i) + ":" + str(j)
                # 将(value, label)添加到dataList中
                dataList.append((value, label))
            # print("!!!!!!!!!!!!!!!!!!!!!!!!!")
            # 将dataList添加到dataTable中
            dataTable.append(dataList)


        # print(dataTable)
        # 返回dataTable
        return dataTable

#主题下拉框
    def createThemeBox(self):
        themeComboBox = QComboBox()

        themeComboBox.addItem("Light", QChart.ChartThemeLight)
        themeComboBox.addItem("Blue Cerulean", QChart.ChartThemeBlueCerulean)
        themeComboBox.addItem("Dark", QChart.ChartThemeDark)
        themeComboBox.addItem("Brown Sand", QChart.ChartThemeBrownSand)
        themeComboBox.addItem("Blue NCS", QChart.ChartThemeBlueNcs)
        themeComboBox.addItem("High Contrast", QChart.ChartThemeHighContrast)
        themeComboBox.addItem("Blue Icy", QChart.ChartThemeBlueIcy)

        return themeComboBox
#动画下拉框
    def createAnimationBox(self):
        animationComboBox = QComboBox()

        animationComboBox.addItem("No Animations", QChart.NoAnimation)
        animationComboBox.addItem("GridAxis Animations", QChart.GridAxisAnimations)
        animationComboBox.addItem("Series Animations", QChart.SeriesAnimations)
        animationComboBox.addItem("All Animations", QChart.AllAnimations)

        return animationComboBox
# 创建图例下拉框
    def createLegendBox(self):
        legendComboBox = QComboBox()

        legendComboBox.addItem("No Legend ", 0)
# 添加一个选项到legendComboBox中，选项内容为"Legend Top"，选项值设置为Qt.AlignTop
        legendComboBox.addItem("Legend Top", Qt.AlignTop)
# 添加一个选项到legendComboBox中，选项内容为"Legend Bottom"，选项值设置为Qt.AlignBottom
        legendComboBox.addItem("Legend Bottom", Qt.AlignBottom)
# 添加一个选项到legendComboBox中，选项内容为"Legend Left"，选项值设置为Qt.AlignLeft
        legendComboBox.addItem("Legend Left", Qt.AlignLeft)
# 添加一个选项到legendComboBox中，选项内容为"Legend Right"，选项值设置为Qt.AlignRight
        legendComboBox.addItem("Legend Right", Qt.AlignRight)

        return legendComboBox
#区域图
    def createAreaChart(self):
        chart = QChart()
        chart.setTitle("Area chart")

        # The lower series is initialized to zero values.
        lowerSeries = None
        y_points = []

# 遍历self.m_dataTable中的每一项
        for i, data_list in enumerate(self.m_dataTable):
            
    # 打印data_list
    # 创建一个QLineSeries对象，用于存储上边界数据
            upperSeries = QLineSeries(chart)
    # 遍历data_list中的每一项
            for j, (value, _) in enumerate(data_list):
        # 获取y值
                y = value.y()
                # print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy---------:",y)
                

        # 如果lowerSeries为空，则将y值添加到upperSeries中，并将y值添加到y_points中
                if lowerSeries is None:
                    upperSeries.append(QPointF(j, y))
                    # print("j = %d, y = %f"%(j, y))
                    y_points.append(y)
        # 否则，将y值与y_points中的对应值相加，并将结果添加到upperSeries中，并将结果添加到y_points中
                else:
                    new_y = y_points[i] + y
                    # print("y_points[i] = %f, y = %f"%(y_points[i], y))
                    upperSeries.append(QPointF(j, new_y))
                    # print("j = %d, neww_y = %f"%(j, new_y))
                    y_points[j] += new_y

    # 创建一个QAreaSeries对象，用于存储上边界和下边界数据
            area = QAreaSeries(upperSeries, lowerSeries)
    # 设置area的名称
            area.setName("Series " + str(i))
    # 将area添加到chart中
            chart.addSeries(area)
    # 将upperSeries赋值给lowerSeries，用于下一次循环
            lowerSeries = upperSeries

        chart.createDefaultAxes()

        return chart
# 创建一个柱状图，并将其添加到布局中
    def createBarChart(self, valueCount):
        chart = QChart()
        chart.setTitle("Bar chart")

        series = QStackedBarSeries(chart)

        for i, data_list in enumerate(self.m_dataTable):
            set = QBarSet("Bar set " + str(i))
            for value, _ in data_list:
                set << value.y()

            series.append(set)

        chart.addSeries(series)
        chart.createDefaultAxes()
        return chart
# 创建一个折线图，并将其添加到布局中
    def createLineChart(self):
        chart = QChart()
        chart.setTitle("Line chart")

        for i, data_list in enumerate(self.m_dataTable):
            series = QLineSeries(chart)
            for value, _ in data_list:
                series.append(value)

            series.setName("Series " + str(i))
            chart.addSeries(series)

        chart.createDefaultAxes()

        return chart
 # 创建一个饼图，并将其添加到布局中
    def createPieChart(self):
        chart = QChart()
        chart.setTitle("Pie chart")

        pieSize = 1.0 / len(self.m_dataTable)

        for i, data_list in enumerate(self.m_dataTable):
            series = QPieSeries(chart)
            for value, label in data_list:
                slice = series.append(label, value.y())
                if series.count() == 1:
                    slice.setLabelVisible()
                    slice.setExploded()

            hPos = (pieSize / 2) + (i / float(len(self.m_dataTable)))
            series.setPieSize(pieSize)
            series.setHorizontalPosition(hPos)
            series.setVerticalPosition(0.5)

            chart.addSeries(series)

        return chart
# 创建一个曲线图，并将其添加到布局中
    def createSplineChart(self):
        chart = QChart()
        chart.setTitle("Spline chart")

        for i, data_list in enumerate(self.m_dataTable):
            series = QSplineSeries(chart)
            for value, _ in data_list:
                series.append(value)

            series.setName("Series " + str(i))
            chart.addSeries(series)

        chart.createDefaultAxes()

        return chart
# 创建一个散点图，并将其添加到布局中
    def createScatterChart(self):
        chart = QChart()
        chart.setTitle("Scatter chart")

        for i, data_list in enumerate(self.m_dataTable):
            series = QScatterSeries(chart)
            for value, _ in data_list:
                series.append(value)

            series.setName("Series " + str(i))
            chart.addSeries(series)

        chart.createDefaultAxes()

        return chart

    @pyqtSlot()
    def updateUI(self):
        # 获取当前主题
        theme = self.m_themeComboBox.itemData(
            self.m_themeComboBox.currentIndex())
        # 如果当前图表的主题与选择的主题不同，则更新所有图表的主题
        
        if self.m_charts[0].chart().theme() != theme:
            for chartView in self.m_charts:
# 设置图表视图的主题
                chartView.chart().setTheme(QChart.ChartTheme(theme))
                #设置反锯齿
                chartView.chart().setAntialiasing(True)

            # 获取窗口的调色板
            pal = self.window().palette()
    
        
            if theme == QChart.ChartThemeLight:
                pal.setColor(QPalette.Window, QColor(0xf0f0f0))
                self.frame.setStyleSheet("background-color: #f0f0f0")
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif theme == QChart.ChartThemeDark:
                pal.setColor(QPalette.Window, QColor(0x121218))
                self.frame.setStyleSheet("background-color: #121218")
                pal.setColor(QPalette.WindowText, QColor(0xd6d6d6))
            elif theme == QChart.ChartThemeBlueCerulean:
                pal.setColor(QPalette.Window, QColor(0x40434a))
                self.frame.setStyleSheet("background-color: #40434a")
                pal.setColor(QPalette.WindowText, QColor(0xd6d6d6))
            elif theme == QChart.ChartThemeBrownSand:
                pal.setColor(QPalette.Window, QColor(0x9e8965))
                self.frame.setStyleSheet("background-color: #9e8965")
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif theme == QChart.ChartThemeBlueNcs:
                pal.setColor(QPalette.Window, QColor(0x018bba))
                self.frame.setStyleSheet("background-color: #018bba")
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif theme == QChart.ChartThemeHighContrast:
                pal.setColor(QPalette.Window, QColor(0xffab03))
                self.frame.setStyleSheet("background-color: #ffab03")
                pal.setColor(QPalette.WindowText, QColor(0x181818))
            elif theme == QChart.ChartThemeBlueIcy:
                pal.setColor(QPalette.Window, QColor(0xcee7f0)) 
                self.frame.setStyleSheet("background-color: #cee7f0")
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            else: 
                pal.setColor(QPalette.Window, QColor(0xf0f0f0))
                self.frame.setStyleSheet("background-color: #f0f0f0")
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            self.window().setPalette(pal)
# 获取动画选项
        options = QChart.AnimationOptions(
            self.m_animatedComboBox.itemData(
                self.m_animatedComboBox.currentIndex()))
# 如果第一个图表视图的动画选项与获取的动画选项不同
        if self.m_charts[0].chart().animationOptions() != options:
    # 遍历所有图表视图
            for chartView in self.m_charts:
        # 设置图表视图的动画选项
                chartView.chart().setAnimationOptions(options)
# 获取图例对齐方式
# 获取图例组合框中当前项的数据
        alignment = self.m_legendComboBox.itemData(
            self.m_legendComboBox.currentIndex())
# 遍历所有图表视图
        for chartView in self.m_charts:
    # 获取当前图表的图例
            legend = chartView.chart().legend()
    # 如果图例组合框中当前项的数据为0，则隐藏图例
            if alignment == 0:
                legend.hide()
    # 否则，设置图例的对齐方式，并显示图例
            else:
                legend.setAlignment(Qt.Alignment(alignment))
                legend.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    # window = QMainWindow()
    # window.setStyleSheet("QMainWindow{background-color: #ff0}")
    widget = ThemeWidget()
    widget.show()
    # window.setCentralWidget(widget)
    widget.resize(900, 600)
    # window.show()

    sys.exit(app.exec_())

