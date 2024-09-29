from PyQt5.QtWidgets import QApplication, QScrollBar, QVBoxLayout, QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.scroll_bar = QScrollBar(self)

        # 连接信号到槽函数
        self.scroll_bar.valueChanged.connect(self.on_value_changed)
        self.scroll_bar.sliderPressed.connect(self.on_slider_pressed)
        self.scroll_bar.sliderReleased.connect(self.on_slider_released)
        self.scroll_bar.actionTriggered.connect(self.on_action_triggered)

        layout.addWidget(self.scroll_bar)
        self.setLayout(layout)
        self.setWindowTitle('QScrollBar Example')
        self.show()

    def on_value_changed(self, value):
        print(f"Scroll bar value changed: {value}")

    def on_slider_pressed(self):
        print("Slider pressed")

    def on_slider_released(self):
        print("Slider released")

    def on_action_triggered(self, action):
        print(f"Action triggered: {action}")

if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    app.exec_()
