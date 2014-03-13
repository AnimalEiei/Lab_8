'''
from turtle import *

class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*1.5, 2) # square-->rectangle
        self.fillcolor(n/6., 0, 1-n/6.)
        self.st()

class Tower(list):
    print("Hanoi tower, a subclass of built-in type list")
    def __init__(self, x):
        #"create an empty tower. x is x-position of peg"
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)

def play():
    onkey(None,"space")
    clear()
    hanoi(6, t1, t2, t3)
    write("press STOP button to exit",
          align="center", font=("Courier", 16, "bold"))

def main():
    global t1, t2, t3
    ht(); penup(); goto(0, -225)   # writer turtle
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # make tower of 6 discs
    for i in range(6,0,-1):
        t1.push(Disc(i))
    # prepare spartanic user interface ;-)
    write("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))
    onkey(play, "space")
    listen()
    return "EVENTLOOP"

if __name__=="__main__":
    msg = main()
    print (msg)
    mainloop()
 '''

def Move(src, dest):
     dest.append(src.pop())

def Hanoi(nDisks, src, dest, temp):
    numDiskMoved = 0

    while numDiskMoved < nDisks:                
            if len(dest) == 0:   #dest is empty, go ahead and move
                              Move(src, dest)
                              numDiskMoved += 1

            elif dest[-1] > src[-1]:  #dest disk is bigger than src Disk. Still a valid move
                                    Move(src, dest)
                                    numDiskMoved += 1

            else:  #situation where dest disk is smaller than src disk
                 newNDisks = len(dest) #move all of current dest disks to temp
                 Hanoi(newNDisks, dest, temp, src)
                 Move(src, dest)
                 numDiskMoved += 1
                 Hanoi(newNDisks, temp, dest, src)

a = [3, 2, 1]
b = []
c = []

Hanoi(len(src), a, c, b)
print(c)