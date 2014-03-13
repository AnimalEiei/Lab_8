import sys
from PySide.QtCore import *
from PySide.QtGui import *

class PaintWidget(QWidget):
    WINDOW_WIDTH = 300
    WINDOW_HEIGHT = 300
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUI()
        self.pointList = set()

    def setupUI(self):
        self.setFixedSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

    def clearAllPoint(self):
        self.pointList.clear()

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(Qt.red)
        painter.setPen(Qt.red)
        for i in self.pointList:
            painter.drawEllipse(i, 5, 5)
            #painter.drawPoint(i)
        painter.end()
        self.update()

    def mouseMoveEvent(self, e):
        super().mouseMoveEvent(e)
        self.pointList.add(e.pos())
        
        

class SimplePaintProgram(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUI()
        self.clearBt.clicked.connect(self.paintArea.clearAllPoint)
        #self.clearBt.clicked.connect(self.clear)


    def setupUI(self):
        self.setWindowTitle("A Simple Paint Program")

        layout = QVBoxLayout()
        
        self.paintArea = PaintWidget()
        label = QLabel("Drag the mouse to draw")
        label.setAlignment(Qt.AlignHCenter)
        self.clearBt = QPushButton("Clear")
        
        
        layout.addWidget(self.paintArea)
        layout.addWidget(label)
        layout.addWidget(self.clearBt)

        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    w = SimplePaintProgram()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())