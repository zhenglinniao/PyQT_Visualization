################################################################################
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

## ==> GUI FILE
from main import *
from ColorChangeWindow import *

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1

class UIFunctions(MainWindow):

    ## ==> GLOBALS
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True

    ########################################################################
    ## START - GUI FUNCTIONS
    ########################################################################

    ## ==> MAXIMIZE/RESTORE
    ########################################################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()

    ## ==> RETURN STATUS
    def returStatus():
        return GLOBAL_STATE

    ## ==> SET STATUS
    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    ## ==> ENABLE MAXIMUM SIZE
    ########################################################################
    def enableMaximumSize(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()


    ## ==> TOGGLE MENU
    ########################################################################
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    ## ==> SET TITLE BAR
    ########################################################################
    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    ## ==> HEADER TEXTS
    ########################################################################
    # LABEL TITLE
    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    # LABEL DESCRIPTION
    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    ## ==> DYNAMIC MENUS
    ########################################################################
    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton(str(count),self)
        button.setObjectName(objName)
# 创建一个QSizePolicy对象，设置水平和垂直方向的大小策略分别为Expanding和Fixed
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)


    ## 自定义面板颜色
    def setPanelColor(self, objName):
        self.ColorChange = ColorChangeWindow()
        self.ColorChange.setObjectName(objName)
        self.ui.ColorChange_Hlayout.addWidget(self.ColorChange)
        self.ColorChange.color_changed.connect(self.changeColor)
        



    def selectMenu(getStyle):
        # 添加边框样式
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(44, 49, 60); }")
        # print("select:", select)
        return select

    ## ==> DESELECT
    def deselectMenu(getStyle):
        # 移除边框样式
        deselect = getStyle.replace("QPushButton { border-right: 7px solid rgb(44, 49, 60); }", "")

        return deselect

    ## ==> START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    ## ==> RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    ## ==> CHANGE PAGE LABEL TEXT
    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)

    ## ==> USER ICON
    ########################################################################
    def userIcon(self, initialsTooltip, icon, showHide):
        if showHide:
            # SET TEXT
            self.ui.label_user_icon.setText(initialsTooltip)

            # SET ICON
            if icon:
                style = self.ui.label_user_icon.styleSheet()
                setIcon = "QLabel { background-image: " + icon + "; }"
                self.ui.label_user_icon.setStyleSheet(style + setIcon)
                self.ui.label_user_icon.setText('')
                self.ui.label_user_icon.setToolTip(initialsTooltip)
        else:
            self.ui.label_user_icon.hide()

    ########################################################################
    ## END - GUI FUNCTIONS
    ########################################################################


    ########################################################################
    ## START - GUI DEFINITIONS
    ########################################################################

    ## ==> UI DEFINITIONS
    ########################################################################
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # 如果鼠标双击事件类型为QtCore.QEvent.MouseButtonDblClick
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                # 单次定时器，延迟250毫秒后执行UIFunctions.maximize_restore(self)
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        # 如果全局标题栏为真
        if GLOBAL_TITLE_BAR:
            # 设置窗口标志为无框架窗口
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            # 设置窗口背景透明
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            # 将鼠标双击事件绑定到dobleClickMaximizeRestore函数
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        else:
            # 设置水平布局的边距为0
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            # 设置顶部按钮框架的边距为8,0,0,5
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            # 设置顶部按钮框架的最小高度为42
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            # 隐藏顶部图标框架
            self.ui.frame_icon_top_bar.hide()
            # 隐藏右侧按钮框架
            self.ui.frame_btns_right.hide()
            # 隐藏大小调整框架
            self.ui.frame_size_grip.hide()
        # 设置阴影效果
        self.shadow = QGraphicsDropShadowEffect(self)
        # 设置阴影模糊半径为17
        self.shadow.setBlurRadius(17)
        # 设置阴影X轴偏移量为0
        self.shadow.setXOffset(0)
        # 设置阴影Y轴偏移量为0
        self.shadow.setYOffset(0)
        # 设置阴影颜色为黑色，透明度为150
        self.shadow.setColor(QColor(0, 0, 0, 150))
        # 将阴影效果应用到主框架上
        self.ui.frame_main.setGraphicsEffect(self.shadow)
        # 设置大小调整控件
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        # 设置大小调整控件的样式
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")
        # 将最小化按钮的点击事件绑定到showMinimized函数
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        # 将最大化/恢复按钮的点击事件绑定到UIFunctions.maximize_restore(self)函数
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        # 将关闭按钮的点击事件绑定到close函数
        self.ui.btn_close.clicked.connect(lambda: self.close())

