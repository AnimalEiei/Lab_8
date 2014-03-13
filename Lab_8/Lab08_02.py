import sys
from PySide.QtCore import *
from PySide.QtGui import *


class SimplePaintProgram(QWidget):
    WINDOW_WIDTH = 300
    WINDOW_HEIGHT = 300
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUI()


    def setupUI(self):
        self.setWindowTitle("A Simple Paint Program")
        self.setFixedSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        layout = 


def main():
    app = QApplication(sys.argv)
    w = SimplePaintProgram()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())