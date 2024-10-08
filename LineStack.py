#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Createon : 2024年9月24日
@author: kid
@contact: zhenglinniao1417@gamil.com
@file: LineStack.py
@desc: 图表展示
"""


from PySide2.QtWidgets import QApplication, QWidget, QFrame, QGridLayout, QLabel
import sys
from PySide2.QtGui import QColor
try:
    from PySide2.QtChart import QChartView, QChart, QLineSeries, QLegend, \
        QCategoryAxis
    from PySide2.QtCore import Qt, QPointF, QRectF, QPoint
    from PySide2.QtGui import QPainter, QPen
    from PySide2.QtWidgets import QApplication, QGraphicsLineItem, QWidget, \
        QHBoxLayout, QLabel, QVBoxLayout, QGraphicsProxyWidget
except ImportError:
    from PySide2.QtCore import Qt, QPointF, QRectF, QPoint
    from PySide2.QtGui import QPainter, QPen
    from PySide2.QtWidgets import QApplication, QGraphicsLineItem, QWidget, \
        QHBoxLayout, QLabel, QVBoxLayout, QGraphicsProxyWidget
    from PySide2.QtCharts import QtCharts

    QChartView = QtCharts.QChartView
    QChart = QtCharts.QChart
    QLineSeries = QtCharts.QLineSeries
    QLegend = QtCharts.QLegend
    QCategoryAxis = QtCharts.QCategoryAxis

#当鼠标移动显示的视图
class ToolTipItem(QWidget):

    def __init__(self, color, text, parent=None):
        super(ToolTipItem, self).__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        clabel = QLabel(self)
        clabel.setMinimumSize(12, 12)
        clabel.setMaximumSize(12, 12)
        clabel.setStyleSheet("border-radius:6px;background: rgba(%s,%s,%s,%s);" % (
            color.red(), color.green(), color.blue(), color.alpha()))
        layout.addWidget(clabel)
        self.textLabel = QLabel(text, self, styleSheet="color:white;")
        layout.addWidget(self.textLabel)

    def setText(self, text):
        self.textLabel.setText(text)


class ToolTipWidget(QWidget):
    Cache = {}

    def __init__(self, *args, **kwargs):
        super(ToolTipWidget, self).__init__(*args, **kwargs)
# 设置窗口的背景样式
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            "ToolTipWidget{background: rgba(50, 50, 50, 100);}")
        layout = QVBoxLayout(self)
        self.titleLabel = QLabel(self, styleSheet="color:white;")
        layout.addWidget(self.titleLabel)

    def updateUi(self, title, points):
        print("title:", title)
        self.titleLabel.setText(title)
        for serie, point in points:
            if serie not in self.Cache:
                item = ToolTipItem(
                    serie.color(),
                    (serie.name() or "-") + ":" + str(point.y()), self)
                self.layout().addWidget(item)
                print("serie:",serie)
                self.Cache[serie] = item
            else:
                self.Cache[serie].setText(
                    (serie.name() or "-") + ":" + str(point.y()))

            self.Cache[serie].setVisible(serie.isVisible()) #设置数据可见性 如果数据被隐藏则不会显示该数据的小窗口
        self.adjustSize()  # 自动随窗口调整大小


class GraphicsProxyWidget(QGraphicsProxyWidget):

    def __init__(self, *args, **kwargs):
        super(GraphicsProxyWidget, self).__init__(*args, **kwargs)
        self.setZValue(999)
        self.tipWidget = ToolTipWidget()
        self.setWidget(self.tipWidget)
        self.hide()

    def width(self):
        return self.size().width()

    def height(self):
        return self.size().height()

    def show(self, title, points, pos):
        self.setGeometry(QRectF(pos, self.size()))
        self.tipWidget.updateUi(title, points)
        super(GraphicsProxyWidget, self).show()


class ChartView(QChartView):

    def __init__(self, *args, **kwargs):
        super(ChartView, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        # 自定义x轴label
        self.category = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        self.initChart()

        # 提示widget
        self.toolTipWidget = GraphicsProxyWidget(self._chart)

        # line
        self.lineItem = QGraphicsLineItem(self._chart)
        # 设置画笔颜色为灰色
        pen = QPen(Qt.gray)
        # 设置画笔宽度为1
        pen.setWidth(1)
        # 设置lineItem的画笔
        self.lineItem.setPen(pen)
        # 设置lineItem的z值，使其在图表上方显示
        self.lineItem.setZValue(998)
        # 隐藏lineItem
        self.lineItem.hide()

        # 一些固定计算，减少mouseMoveEvent中的计算量
        # 获取x和y轴的最小最大值
        axisX, axisY = self._chart.axisX(), self._chart.axisY()
        print("axisX:",axisX, axisY)
        self.min_x, self.max_x = axisX.min(), axisX.max()
        print("min_x:",self.min_x, self.max_x)
        self.min_y, self.max_y = axisY.min(), axisY.max()
        print()

    def resizeEvent(self, event):
        super(ChartView, self).resizeEvent(event)
        # 当窗口大小改变时需要重新计算
        # 坐标系中左上角顶点
        self.point_top = self._chart.mapToPosition(
            QPointF(self.min_x, self.max_y))
        # 坐标原点坐标
        self.point_bottom = self._chart.mapToPosition(
            QPointF(self.min_x, self.min_y))
        self.step_x = (self.max_x - self.min_x) / \
                      (self._chart.axisX().tickCount() - 1)

    def mouseMoveEvent(self, event):
        super(ChartView, self).mouseMoveEvent(event)
        pos = event.pos()
        # 把鼠标位置所在点转换为对应的xy值
        x = self._chart.mapToValue(pos).x()
        y = self._chart.mapToValue(pos).y()
        index = round((x - self.min_x) / self.step_x)
        # 得到在坐标系中的所有正常显示的series的类型和点
        points = [(serie, serie.at(index))
                  for serie in self._chart.series()
                  if self.min_x <= x <= self.max_x and
                  self.min_y <= y <= self.max_y]
        if points:
            pos_x = self._chart.mapToPosition(
                QPointF(index * self.step_x + self.min_x, self.min_y))
            self.lineItem.setLine(pos_x.x(), self.point_top.y(),
                                  pos_x.x(), self.point_bottom.y())
            self.lineItem.show()
            try:
                title = self.category[index]
            except:
                title = ""
            t_width = self.toolTipWidget.width()
            t_height = self.toolTipWidget.height()
            # 如果鼠标位置离右侧的距离小于tip宽度
            x = pos.x() - t_width if self.width() - \
                                     pos.x() - 20 < t_width else pos.x()
            # 如果鼠标位置离底部的高度小于tip高度
            y = pos.y() - t_height if self.height() - \
                                      pos.y() - 20 < t_height else pos.y()
            self.toolTipWidget.show(
                title, points, QPoint(x, y))
        else:
            self.toolTipWidget.hide()
            self.lineItem.hide()
   
    #鼠标点击消失
    def handleMarkerClicked(self):
        marker = self.sender()  # 信号发送者
        if not marker:
            return
        visible = not marker.series().isVisible()
        #         # 隐藏或显示series
        marker.series().setVisible(visible)
        marker.setVisible(True)  # 要保证marker一直显示
        # 透明度
        alpha = 1.0 if visible else 0.4
        # 设置label的透明度
        brush = marker.labelBrush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setLabelBrush(brush)
        # 设置marker的透明度
        brush = marker.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setBrush(brush)
        # 设置画笔透明度
        pen = marker.pen()
        color = pen.color()
        color.setAlphaF(alpha)
        pen.setColor(color)
        marker.setPen(pen)
    #鼠标点击加粗
    def handleMarkerHovered(self, status):
        # 设置series的画笔宽度
        marker = self.sender()  # 信号发送者
        if not marker:
            return
        series = marker.series()
        if not series:
            return
        pen = series.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        series.setPen(pen)
    #鼠标点击消失
    def handleSeriesHoverd(self, point, state):
        # 设置series的画笔宽度
        series = self.sender()  # 信号发送者
        pen = series.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if state else -1))
        series.setPen(pen)

    def initChart(self):
        self._chart = QChart(title="折线图堆叠")
        self._chart.setAcceptHoverEvents(True)
        # Series动画
        self._chart.setAnimationOptions(QChart.SeriesAnimations)
        dataTable = [
            ["tip1", [120, 132, 101, 134, 90, 230, 210]],
            ["tip2", [220, 182, 191, 234, 290, 330, 310]],
            ["tip3", [150, 232, 201, 154, 190, 330, 410]],
            ["tip4", [320, 332, 301, 334, 390, 330, 320]],
            ["tip4", [820, 932, 901, 934, 1290, 1330, 1320]]
        ]
        for series_name, data_list in dataTable:
            series = QLineSeries(self._chart)
            for j, v in enumerate(data_list):
                series.append(j, v)
            series.setName(series_name)
            series.setPointsVisible(True)  # 显示圆点
            series.hovered.connect(self.handleSeriesHoverd)  # 鼠标悬停
            self._chart.addSeries(series)
        self._chart.createDefaultAxes()  # 创建默认的轴
        axisX = self._chart.axisX()  # x轴
        axisX.setTickCount(7)  # x轴设置7个刻度
        axisX.setGridLineVisible(False)  # 隐藏从x轴往上的线条
        axisY = self._chart.axisY()
        axisY.setTickCount(7)  # y轴设置7个刻度
        axisY.setRange(0, 1500)  # 设置y轴范围
        # 自定义x轴
        axis_x = QCategoryAxis(
            self._chart, labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue)
        axis_x.setTickCount(7)
        axis_x.setGridLineVisible(False)
        min_x = axisX.min()
        max_x = axisX.max()
        step = (max_x - min_x) / (7 - 1)  # 7个tick
        for i in range(0, 7):
            axis_x.append(self.category[i], min_x + i * step)
        self._chart.setAxisX(axis_x, self._chart.series()[-1])
        # chart的图例
        legend = self._chart.legend()
        # 设置图例由Series来决定样式
        legend.setMarkerShape(QLegend.MarkerShapeFromSeries)
        # 遍历图例上的标记并绑定信号
        for marker in legend.markers():
            # 点击事件
            marker.clicked.connect(self.handleMarkerClicked)
            # 鼠标悬停事件
            marker.hovered.connect(self.handleMarkerHovered)
        self.setChart(self._chart)


class content_charts(QWidget):
    def __init__(self):
        super().__init__()
        self.frame = QFrame(self)
        self.QV_layout = QVBoxLayout(self.frame)
        self.QH_layout_1 = QHBoxLayout(self.frame)
        self.QH_layout_2 = QHBoxLayout(self.frame)

        self.chart1 = ChartView()
        self.chart2 = ChartView()
        self.chart3 = ChartView()
        self.chart4 = ChartView()

        self.QH_layout_1.addWidget(self.chart1)
        self.QH_layout_1.addWidget(self.chart2)
        self.QH_layout_2.addWidget(self.chart3)
        self.QH_layout_2.addWidget(self.chart4)

        self.QV_layout.addLayout(self.QH_layout_1)
        self.QV_layout.addLayout(self.QH_layout_2)

        # 设置主布局
        main_layout = QVBoxLayout(self)  # 创建主布局
        main_layout.addWidget(self.frame)  # 将框架添加到主布局

        # 设置 ContentCharts 的布局
        self.setLayout(main_layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    color = QColor(255, 100, 50)
    view = content_charts()
    
    # 显示视图
    view.show()
    sys.exit(app.exec_())
