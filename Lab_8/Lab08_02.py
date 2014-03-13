import sys
from PySide.QtCore import *
from PySide.QtGui import *

class PaintWidget(QWidget):
    WINDOW_WIDTH = 300
    WINDOW_HEIGHT = 300
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUI()

    def setupUI(self):
        self.setFixedSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

    def paintEvent(self, e):
        painter = QPainter(self)


class SimplePaintProgram(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUI()


    def setupUI(self):
        self.setWindowTitle("A Simple Paint Program")

        layout = QVBoxLayout()
        
        paintArea = PaintWidget()
        label = QLabel("Drag the mouse to draw")
        label.setAlignment(Qt.AlignHCenter)
        clearBt = QPushButton("Clear")
        
        layout.addWidget(paintArea)
        layout.addWidget(label)
        layout.addWidget(clearBt)

        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    w = SimplePaintProgram()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())