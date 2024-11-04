#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Createon : 2024年9月24日
@author: kid
@contact: zhenglinniao1417@gamil.com
@file: LineStack.py
@desc: 图表展示
"""
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
from SQLAlchemy import *
from PyQt5.QtGui import QFont
class ThemeWidget(QWidget):
    def __init__(self, parent=None):
        super(ThemeWidget, self).__init__(parent)

#触发器
    def connectSignals(self,parent=None):
        if parent is None:
            logging.error("parent is None")
        parent.m_themeComboBox.currentIndexChanged.connect(lambda index: self.updateUI(parent, index))
        parent.m_animatedComboBox.currentIndexChanged.connect(lambda index: self.updateUI(parent, index))
        parent.m_legendComboBox.currentIndexChanged.connect(lambda index: self.updateUI(parent, index))

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
                    j + random.random() * valueMax / f_valueCount,
                    yValue)
                
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
    def createAreaChart(self,m_dataTable):
        chart = QChart()
        chart.setTitle("Area chart")
        chart.setTitleBrush(Qt.white)
        legend = chart.legend()
        legend.setLabelBrush(Qt.white)
       

        # The lower series is initialized to zero values.
        lowerSeries = None
        y_points = []

# 遍历self.m_dataTable中的每一项
        for i, data_list in m_dataTable:
  
            upperSeries = QLineSeries(chart)
    # 遍历data_list中的每一项
            for j, value in enumerate(data_list):
        # 获取y值
                y = value
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
        chart.axisY().setLabelsBrush(Qt.white)
        chart.axisX().setLabelsBrush(Qt.white)

        return chart

        return chart
# 创建一个柱状图，并将其添加到布局中
    def createBarChart(self, m_dataTable):
        chart = QChart()
        chart.setBackgroundBrush(Qt.transparent)
        chart.setTitle("Bar chart")
        chart.setTitleBrush(Qt.white)
        legend = chart.legend()
        legend.setLabelBrush(Qt.white)

        series = QStackedBarSeries(chart)

        for i, (index,data_list) in enumerate(m_dataTable):
            set = QBarSet("Bar set " + index)
            for value in data_list:
                set << value
            series.append(set)
        chart.addSeries(series)

        chart.createDefaultAxes()
        chart.axisY().setLabelsBrush(Qt.white)
        
    # 定义一个包含5个元素的列表
        categories = ["A", "B", "C", "D", "E"]
# 创建一个QCategoryAxis对象
        axisX = QtCharts.QCategoryAxis(labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue)
# 将列表中的元素添加到QCategoryAxis对象中
        for category in categories:
            axisX.append(category, categories.index(category))  
        
        axisX.setLabelsBrush(Qt.white)
# 将QCategoryAxis对象设置为图表的X轴
        chart.setAxisX(axisX, series)
# 将数据集添加到图表中

        
        
        return chart
# 创建一个折线图，并将其添加到布局中
    def createLineChart(self,m_dataTable):
        chart = QChart()
        chart.setBackgroundBrush(Qt.transparent)
        chart.setTitle("Line chart")
        chart.setTitleBrush(Qt.white)
        legend = chart.legend()
        legend.setLabelBrush(Qt.white)
        for i, data_list in m_dataTable:
            series = QLineSeries(chart)
            for index, value in enumerate(data_list):
                
                series.append(index,value)

            series.setName(str(i))
            chart.addSeries(series)

        chart.createDefaultAxes()
        chart.axisY().setLabelsBrush(Qt.white)
        chart.axisX().setLabelsBrush(Qt.white)

        return chart
 # 创建一个饼图，并将其添加到布局中
    def createPieChart(self,m_dataTable):
        chart = QChart()
        chart.setTitle("Pie chart")
        chart.setTitleBrush(Qt.white)
        legend = chart.legend()
        legend.setLabelBrush(Qt.white)

        pieSize = 1.0 / len(m_dataTable)

        for i, (index0,data_list) in enumerate(m_dataTable):
            # print(i,index,data_list)
            series = QPieSeries(chart)
            for index, value in enumerate(data_list):
                label = f"{index0} {index + 1}"  # 生成一个标签，如 "Slice 1", "Slice 2" 等
                slice = series.append(label,value)
                if series.count() == 1:
                    slice.setLabelVisible()
                    slice.setExploded()
# 计算饼图的水平位置
            hPos = (pieSize / 2) + (i / float(len(m_dataTable)))
# 设置饼图的大小
            series.setPieSize(pieSize)
# 设置饼图的水平位置
            series.setHorizontalPosition(hPos)
# 设置饼图的垂直位置
            series.setVerticalPosition(0.5)

            chart.addSeries(series)
        
        return chart
# 创建一个曲线图，并将其添加到布局中
    def createSplineChart(self,m_dataTable):
        chart = QChart()
        chart.setTitle("Spline chart")
        chart.setTitleBrush(Qt.white)
        legend = chart.legend()
        legend.setLabelBrush(Qt.white)

        for i, (index,data_list) in enumerate(m_dataTable):
            series = QSplineSeries(chart)
            for j,value in enumerate(data_list):
                series.append(float(j),float(value))

            series.setName(index)
            chart.addSeries(series)

        chart.createDefaultAxes()
        chart.axisY().setLabelsBrush(Qt.white)
        chart.axisX().setLabelsBrush(Qt.white)
        return chart
# 创建一个散点图，并将其添加到布局中
    def createScatterChart(self,m_dataTable):
        chart = QChart()
        chart.setTitle("Scatter chart")
        chart.setTitleBrush(Qt.white)
        legend = chart.legend()
        legend.setLabelBrush(Qt.white)

        for i, (index,data_list) in enumerate(m_dataTable):
            series = QScatterSeries(chart)
            for j,value in enumerate(data_list):
                series.append(float(j),float(value))
            series.setName("Series " + str(i))
            chart.addSeries(series)
        chart.createDefaultAxes()
        chart.axisY().setLabelsBrush(Qt.white)
        chart.axisX().setLabelsBrush(Qt.white)
        return chart
    @pyqtSlot()
    def updateUI(self,parent,index=None):
        # 获取当前主题
        try:
            result1 = parent.m_themeComboBox.currentIndex() if parent.index1 == ""  else parent.index1
        except:
            result1 = parent.m_themeComboBox.currentIndex()
        theme = parent.m_themeComboBox.itemData(int(result1))
        # 如果当前图表的主题与选择的主题不同，则更新所有图表的主题
        for chartView in parent.m_charts:
            chartView.setRenderHint(QPainter.Antialiasing)  
        if parent.m_charts[0].chart().theme() != theme:
            for chartView in parent.m_charts:
# 设置图表视图的主题
                chartView.chart().setTheme(QChart.ChartTheme(theme))

            # 获取窗口的调色板
            pal = parent.window().palette()
    
        
            if theme == QChart.ChartThemeLight:
                # pal.setColor(QPalette.Window, QColor(0xf0f0f0))
                # parent.frame.setStyleSheet("background-color: #f0f0f0")
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif theme == QChart.ChartThemeDark:
                # pal.setColor(QPalette.Window, QColor(0x121218))
                # parent.frame.setStyleSheet("background-color: #121218")
                pal.setColor(QPalette.WindowText, QColor(0xd6d6d6))
            elif theme == QChart.ChartThemeBlueCerulean:
                # pal.setColor(QPalette.Window, QColor(0x40434a))
                # parent.frame.setStyleSheet("background-color: #40434a")
                pal.setColor(QPalette.WindowText, QColor(0xd6d6d6))
            elif theme == QChart.ChartThemeBrownSand:
                # pal.setColor(QPalette.Window, QColor(0x9e8965))
                # parent.frame.setStyleSheet("background-color: #9e8965")
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif theme == QChart.ChartThemeBlueNcs:
                # pal.setColor(QPalette.Window, QColor(0x018bba))
                # parent.frame.setStyleSheet("background-color: #018bba")
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif theme == QChart.ChartThemeHighContrast:
                # pal.setColor(QPalette.Window, QColor(0xffab03))
                # parent.frame.setStyleSheet("background-color: #ffab03")
                pal.setColor(QPalette.WindowText, QColor(0x181818))
            elif theme == QChart.ChartThemeBlueIcy:
                # pal.setColor(QPalette.Window, QColor(0xcee7f0)) 
                # parent.frame.setStyleSheet("background-color: #cee7f0")
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            else: 
                pal.setColor(QPalette.Window, QColor(0xf0f0f0))
                parent.frame.setStyleSheet("background-color: #f0f0f0")
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            parent.window().setPalette(pal)
# 获取动画选项

        try:
            result2 = parent.m_animatedComboBox.currentIndex() if parent.index2 == ""  else parent.index2
        except:
            result2 = parent.m_animatedComboBox.currentIndex()
        options = QChart.AnimationOptions(parent.m_animatedComboBox.itemData(int(result2)))
# 如果第一个图表视图的动画选项与获取的动画选项不同
        if parent.m_charts[0].chart().animationOptions() != options:
    # 遍历所有图表视图
            for chartView in parent.m_charts:
        # 设置图表视图的动画选项
                chartView.chart().setAnimationOptions(options)
# 获取图例对齐方式
# 获取图例组合框中当前项的数据
        try:
            result3 = parent.m_legendComboBox.currentIndex() if parent.index3 == ""  else parent.index3
        except:
            result3 = parent.m_legendComboBox.currentIndex()
        alignment = parent.m_legendComboBox.itemData(int(result3))
# 遍历所有图表视图
        
        for chartView in parent.m_charts:
    # 获取当前图表的图例
            legend = chartView.chart().legend()
    # 如果图例组合框中当前项的数据为0，则隐藏图例
            if alignment == 0:
                legend.hide()
    # 否则，设置图例的对齐方式，并显示图例
            else:
                legend.setAlignment(Qt.Alignment(alignment))
                legend.show()


class createBar(QWidget):
    def __init__(self, parent=None):
        super(createBar, self).__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = ThemeWidget()
        self.m_charts=[]
        self.m_dataTable = [
            ["tip1", [120, 132, 101, 134, 90, 230, 210,222]],
            ["tip2", [220, 182, 191, 234, 290, 330, 310]],
        ]
        # 创建主题下拉框
        self.m_themeComboBox = self.ui.createThemeBox()

        # 创建动画下拉框
        self.m_animatedComboBox = self.ui.createAnimationBox()
        self.m_legendComboBox = self.ui.createLegendBox()
        self.ui.connectSignals(self)

        self.frame = QFrame(self)
        self.frame.setObjectName("mainFrame")
        baseLayout = QGridLayout(self.frame)
        settingsLayout = QHBoxLayout()
        settingsLayout.addWidget(QLabel("Theme:"))
        settingsLayout.addWidget(self.m_themeComboBox)
        settingsLayout.addWidget(QLabel("Animation:"))
        settingsLayout.addWidget(self.m_animatedComboBox)
        settingsLayout.addWidget(QLabel("Legend:"))
        settingsLayout.addWidget(self.m_legendComboBox)

        settingsLayout.setAlignment(Qt.AlignCenter)
        # 将设置布局添加到主布局中，位置为第0行第0列，占据1行3列
        baseLayout.addLayout(settingsLayout, 0, 0, 1, 3)
        self.chartView = QChartView(self.ui.createBarChart(self.m_dataTable))
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartView.setStyleSheet("background: transparent; border: none;")  # 设置无边框和透明背景
        baseLayout.addWidget(self.chartView, 1, 0)
        self.m_charts.append(self.chartView)


        self.data_fetch_thread = DataFetchThread()
# 当数据被获取时，调用update_labels方法
        self.data_fetch_thread.data_fetched.connect(self.update_labels)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.start_data_fetch)
# 启动定时器，每隔60秒执行一次
        self.timer.start(6 * 1000)



         # 设置布局
        main_layout = QGridLayout(self)  # 创建主窗口的布局
        main_layout.addWidget(self.frame)  # 将 QFrame 添加到主布局中
        self.setLayout(main_layout)  # 设置主窗口的布局


    def start_data_fetch(self):
        # 启动数据获取线程
        self.data_fetch_thread.start()

    def update_labels(self, datas):
        self.m_dataTable = [
            ["zln", [data["Mo_Amount"] for data in datas["data"]]],    
        ]
        if self.chartView:
            # 清除现有的图表
            self.chartView.setChart(self.ui.createBarChart(self.m_dataTable))
            self.ui.updateUI(self,self)
       



class createpie2(QWidget):
    def __init__(self, parent=None):
        super(createpie2, self).__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = ThemeWidget()
        self.m_charts=[]
        self.m_dataTable = [
            ["tip1", [120, 132, 101, 134, 90, 230, 210,222]],
            ["tip2", [220, 182, 191, 234, 290, 330, 310]],
        ]
        # 创建主题下拉框
        self.m_themeComboBox = self.ui.createThemeBox()

        # 创建动画下拉框
        self.m_animatedComboBox = self.ui.createAnimationBox()
        self.m_legendComboBox = self.ui.createLegendBox()
        self.ui.connectSignals(self)
        self.index1 = 1
        self.index2 = ""
        self.index3 = 3

        self.frame = QFrame(self)
        self.frame.setObjectName("mainFrame")
        baseLayout = QGridLayout(self.frame)
        settingsLayout = QHBoxLayout()
        settingsLayout.addWidget(QLabel("Theme:"))
        settingsLayout.addWidget(self.m_themeComboBox)
        settingsLayout.addWidget(QLabel("Animation:"))
        settingsLayout.addWidget(self.m_animatedComboBox)
        settingsLayout.addWidget(QLabel("Legend:"))
        settingsLayout.addWidget(self.m_legendComboBox)

        # 添加一个拉伸组件，用于填充空白区域
        settingsLayout.setAlignment(Qt.AlignCenter)
        # 将设置布局添加到主布局中，位置为第0行第0列，占据1行3列
        baseLayout.addLayout(settingsLayout, 0, 0, 1, 3)
        self.chartView = QChartView(self.ui.createPieChart(self.m_dataTable))
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartView.setStyleSheet("background: transparent; border: none;")  # 设置无边框和透明背景
        baseLayout.addWidget(self.chartView, 1, 0)
        self.m_charts.append(self.chartView)


        self.data_fetch_thread = DataFetchThread()
# 当数据被获取时，调用update_labels方法
        self.data_fetch_thread.data_fetched.connect(self.update_labels)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.start_data_fetch)
# 启动定时器，每隔60秒执行一次
        self.timer.start(6 * 1000)
         # 设置布局
        main_layout = QGridLayout(self)  # 创建主窗口的布局
        main_layout.addWidget(self.frame)  # 将 QFrame 添加到主布局中
        self.setLayout(main_layout)  # 设置主窗口的布局


    def start_data_fetch(self):
        # 启动数据获取线程
        self.data_fetch_thread.start()

    def update_labels(self, datas):
        self.m_dataTable = [
            ["zln", [data["Mo_Amount"] for data in datas["data"]]],    
        ]
        if self.chartView:
            # 清除现有的图表
            self.chartView.setChart(self.ui.createPieChart(self.m_dataTable))
            self.ui.updateUI(self,self)
       
#TODO:没用
class createpie3(QWidget):
    def __init__(self, parent=None):
        super(createpie3, self).__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = ThemeWidget()
        self.m_charts=[]
        self.m_dataTable = [
            ["tip1", [120, 132, 101, 134, 90, 230, 210,222]],
            ["tip2", [220, 182, 191, 234, 290, 330, 310]],
        ]
        # 创建主题下拉框
        self.m_themeComboBox = self.ui.createThemeBox()

        # 创建动画下拉框
        self.m_animatedComboBox = self.ui.createAnimationBox()
        self.m_legendComboBox = self.ui.createLegendBox()
        self.index1 = "1"
        self.index2 = ""
        self.index3 = "3"


        self.ui.connectSignals(self)
        

        self.frame = QFrame(self)
        self.frame.setObjectName("mainFrame")
        baseLayout = QGridLayout(self.frame)
        settingsLayout = QHBoxLayout()
        settingsLayout.addWidget(QLabel("Theme:"))
        settingsLayout.addWidget(self.m_themeComboBox)
        settingsLayout.addWidget(QLabel("Animation:"))
        settingsLayout.addWidget(self.m_animatedComboBox)
        settingsLayout.addWidget(QLabel("Legend:"))
        settingsLayout.addWidget(self.m_legendComboBox)
        # 添加一个拉伸组件，用于填充空白区域
        settingsLayout.setAlignment(Qt.AlignCenter)
        # 将设置布局添加到主布局中，位置为第0行第0列，占据1行3列
        baseLayout.addLayout(settingsLayout, 0, 0, 1, 3)

        self.chartView = QChartView(self.ui.createPieChart(self.m_dataTable))
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartView.setStyleSheet("background: transparent; border: none;")  # 设置无边框和透明背景
        baseLayout.addWidget(self.chartView, 1, 0)
        self.m_charts.append(self.chartView)


        self.data_fetch_thread = DataFetchThread()
# 当数据被获取时，调用update_labels方法
        self.data_fetch_thread.data_fetched.connect(self.update_labels)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.start_data_fetch)
# 启动定时器，每隔60秒执行一次
        self.timer.start(6 * 1000)
         # 设置布局
        main_layout = QGridLayout(self)  # 创建主窗口的布局
        main_layout.addWidget(self.frame)  # 将 QFrame 添加到主布局中
        self.setLayout(main_layout)  # 设置主窗口的布局


    def start_data_fetch(self):
        # 启动数据获取线程
        self.data_fetch_thread.start()

    def update_labels(self, datas):
        self.m_dataTable = [
            ["zln", [data["Mo_Amount"] for data in datas["data"]]],    
        ]
        if self.chartView:
            # 清除现有的图表
            self.chartView.setChart(self.ui.createPieChart(self.m_dataTable))
            self.ui.updateUI(self,self)
    
class createpie4(QWidget):
    def __init__(self, parent=None):
        super(createpie4, self).__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = ThemeWidget()
        self.m_charts=[]
        self.m_dataTable = [
            ["tip1", [120, 132, 101, 134, 90, 230, 210,222]],
        ]
        # 创建主题下拉框
        self.m_themeComboBox = self.ui.createThemeBox()

        # 创建动画下拉框
        self.m_animatedComboBox = self.ui.createAnimationBox()
        self.m_legendComboBox = self.ui.createLegendBox()
        self.index1 = "1"
        self.index2 = ""
        self.index3 = "3"
        self.ui.connectSignals(self)
        self.frame = QFrame(self)
        self.frame.setObjectName("mainFrame")
        baseLayout = QGridLayout(self.frame)
        baseLayout.setContentsMargins(0, 0, 0, 0)
        settingsLayout = QHBoxLayout()
        settingsLayout.addWidget(QLabel("Theme:"))
        settingsLayout.addWidget(self.m_themeComboBox)
        settingsLayout.addWidget(QLabel("Animation:"))
        settingsLayout.addWidget(self.m_animatedComboBox)
        settingsLayout.addWidget(QLabel("Legend:"))
        settingsLayout.addWidget(self.m_legendComboBox)
        # 添加一个拉伸组件，用于填充空白区域
        settingsLayout.setAlignment(Qt.AlignCenter)
        # 将设置布局添加到主布局中，位置为第0行第0列，占据1行3列
        #TODO: 不把菜单栏加入布局就不显示
        # baseLayout.addLayout(settingsLayout, 0, 0, 1, 3)

        self.chartView = QChartView(self.ui.createPieChart(self.m_dataTable))
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartView.setContentsMargins(0, 0, 0, 0)
        self.chartView.setStyleSheet("background: transparent; border: none;")  # 设置无边框和透明背景
        baseLayout.addWidget(self.chartView, 1, 0)
        self.m_charts.append(self.chartView)


        self.data_fetch_thread = DataFetchThread()
# 当数据被获取时，调用update_labels方法
        self.data_fetch_thread.data_fetched.connect(self.update_labels)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.start_data_fetch)
# 启动定时器，每隔60秒执行一次
        self.timer.start(6 * 1000)
         # 设置布局
        main_layout = QGridLayout(self)  # 创建主窗口的布局
        main_layout.addWidget(self.frame)  # 将 QFrame 添加到主布局中
        self.setLayout(main_layout)  # 设置主窗口的布局


    def start_data_fetch(self):
        # 启动数据获取线程
        self.data_fetch_thread.start()

    def update_labels(self, datas):
        self.m_dataTable = [
            ["zln", [data["Mo_Amount"] for data in datas["data"]]],    
        ]
        if self.chartView:
            # 清除现有的图表
            self.chartView.setChart(self.ui.createPieChart(self.m_dataTable))
            self.ui.updateUI(self,self)
      
class createpie5(QWidget):
    def __init__(self, parent=None):
        super(createpie5, self).__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = ThemeWidget()
        self.m_charts=[]
        self.m_dataTable = [
            ["tip1", [120, 132, 101, 134, 90, 230, 210,222]],
        ]
        # 创建主题下拉框
        self.m_themeComboBox = self.ui.createThemeBox()

        # 创建动画下拉框
        self.m_animatedComboBox = self.ui.createAnimationBox()
        self.m_legendComboBox = self.ui.createLegendBox()
        self.index1 = "1"
        self.index2 = ""
        self.index3 = "3"


        self.ui.connectSignals(self)
        

        self.frame = QFrame(self)
        self.frame.setObjectName("mainFrame")
        baseLayout = QGridLayout(self.frame)
        baseLayout.setContentsMargins(0, 0, 0, 0)
        settingsLayout = QHBoxLayout()
        settingsLayout.addWidget(QLabel("Theme:"))
        settingsLayout.addWidget(self.m_themeComboBox)
        settingsLayout.addWidget(QLabel("Animation:"))
        settingsLayout.addWidget(self.m_animatedComboBox)
        settingsLayout.addWidget(QLabel("Legend:"))
        settingsLayout.addWidget(self.m_legendComboBox)
        # 添加一个拉伸组件，用于填充空白区域
        settingsLayout.setAlignment(Qt.AlignCenter)
        # 将设置布局添加到主布局中，位置为第0行第0列，占据1行3列
        #TODO: 不把菜单栏加入布局就不显示
        # baseLayout.addLayout(settingsLayout, 0, 0, 1, 3)

        self.chartView = QChartView(self.ui.createPieChart(self.m_dataTable))
        self.chartView.setContentsMargins(0, 0, 0, 0)
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartView.setStyleSheet("background: transparent; border: none;")  # 设置无边框和透明背景
        baseLayout.addWidget(self.chartView, 1, 0)
        self.m_charts.append(self.chartView)


        self.data_fetch_thread = DataFetchThread()
# 当数据被获取时，调用update_labels方法
        self.data_fetch_thread.data_fetched.connect(self.update_labels)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.start_data_fetch)
# 启动定时器，每隔60秒执行一次
        self.timer.start(6 * 1000)
         # 设置布局
        main_layout = QGridLayout(self)  # 创建主窗口的布局
        main_layout.addWidget(self.frame)  # 将 QFrame 添加到主布局中
        self.setLayout(main_layout)  # 设置主窗口的布局


    def start_data_fetch(self):
        # 启动数据获取线程
        self.data_fetch_thread.start()

    def update_labels(self, datas):
        self.m_dataTable = [
            ["zln", [data["Mo_Amount"] for data in datas["data"]]],    
        ]
        if self.chartView:
            # 清除现有的图表
            self.chartView.setChart(self.ui.createPieChart(self.m_dataTable))
            self.ui.updateUI(self,self)
   

class createBar6(QWidget):
    def __init__(self, parent=None):
        super(createBar6, self).__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = ThemeWidget()
        self.m_charts=[]
        self.m_dataTable = [
            ["tip1", [120, 132, 101, 134, 90, 230, 210,222]],
            ["tip2", [220, 182, 191, 234, 290, 330, 310]],
        ]
        # 创建主题下拉框
        self.m_themeComboBox = self.ui.createThemeBox()

        # 创建动画下拉框
        self.m_animatedComboBox = self.ui.createAnimationBox()
        self.m_legendComboBox = self.ui.createLegendBox()
        self.ui.connectSignals(self)

        self.frame = QFrame(self)
        self.frame.setObjectName("mainFrame")
        baseLayout = QGridLayout(self.frame)
        settingsLayout = QHBoxLayout()
        settingsLayout.addWidget(QLabel("Theme:"))
        settingsLayout.addWidget(self.m_themeComboBox)
        settingsLayout.addWidget(QLabel("Animation:"))
        settingsLayout.addWidget(self.m_animatedComboBox)
        settingsLayout.addWidget(QLabel("Legend:"))
        settingsLayout.addWidget(self.m_legendComboBox)

        settingsLayout.setAlignment(Qt.AlignCenter)
        # 将设置布局添加到主布局中，位置为第0行第0列，占据1行3列
        baseLayout.addLayout(settingsLayout, 0, 0, 1, 3)
        self.chartView = QChartView(self.ui.createBarChart(self.m_dataTable))
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartView.setStyleSheet("background: transparent; border: none;")  # 设置无边框和透明背景
        baseLayout.addWidget(self.chartView, 1, 0)
        self.m_charts.append(self.chartView)


        self.data_fetch_thread = DataFetchThread()
# 当数据被获取时，调用update_labels方法
        self.data_fetch_thread.data_fetched.connect(self.update_labels)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.start_data_fetch)
# 启动定时器，每隔60秒执行一次
        self.timer.start(6 * 1000)



         # 设置布局
        main_layout = QGridLayout(self)  # 创建主窗口的布局
        main_layout.addWidget(self.frame)  # 将 QFrame 添加到主布局中
        self.setLayout(main_layout)  # 设置主窗口的布局


    def start_data_fetch(self):
        # 启动数据获取线程
        self.data_fetch_thread.start()

    def update_labels(self, datas):
        self.m_dataTable = [
            ["zln", [data["Mo_Amount"] for data in datas["data"]]],    
        ]
        if self.chartView:
            # 清除现有的图表
            self.chartView.setChart(self.ui.createBarChart(self.m_dataTable))
            self.ui.updateUI(self,self)
         


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    # window = QMainWindow()
    # window.setStyleSheet("QMainWindow{background-color: #ff0}")
    widget = createBar6()
    widget.show()
    # window.setCentralWidget(widget)
    widget.resize(900, 600)
    # window.show()
    sys.exit(app.exec_())
