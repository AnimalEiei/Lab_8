from turtle import *

class Disk ():
    def __init__ (self, name, pos_x, pos_y, height, width, color) :
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.color = color
        Turtle.__init__(self, shape="square", visible=False)
        self.shapesize(self.width, self.height, 2)
        self.fillcolor(self.color)
    def showdisk (self) :
        self.st()        
        '''
        pu()
        goto(self.pos_x,self.pos_y)
        pd()
        seth(0)
        fill_color()
        pencolor(self.color)
        fillcolor(self.color)
        fd(self.width/2)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width/2)
        end_fill()
        '''
    def newpos(self,newx,newy):
        self.pos_x = newx
        self.pos_y = newy
        pu()
        goto(self.pos_x,self.pos_y)
        pd()
       
    def cleardisk(): 
        self.ht()
        '''
        for i in range(12):
            undo()
        '''



class Hanoi (object):
    def __init__ (self, n = 3, start = "A", workspace = "B", destination = "C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()

        for i in range (n):
            self.startp.pushdisk(Disk("d" + str(i), 0, i * 150, 20, (n - i) * 30))

    def move_disk (self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower (self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n - 1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n - 1, w, d, s)

    def solve (self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)




h = Hanoi()
h.solve()