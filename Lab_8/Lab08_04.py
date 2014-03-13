import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Disk:
    def __init__(self, width, height):
        self.pos_x = 0
        self.pos_y = 0
        self.width = width
        self.height = height
    def draw(self, painter):
        painter.drawRect(self.pos_x, self.pos_y, self.width, self.height)

class Pole:
    def __init__(self, x, height):
        self.height = height
        self.width = 5
        self.top = 0
        self.pos_x = x
        self.pos_y = 0
        self.stack = list()

    def pushdisk(self, disk):
        self.stack.append(disk)

    def popdisk(self):
        disk = self.stack.pop()
        return disk

    def draw(self, painter):
        painter.drawRect(self.pos_x, self.pos_y, self.width, self.height)

class Hanoi:
    def __init__(self):
        pass
