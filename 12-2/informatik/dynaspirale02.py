#!/usr/bin/python3

from turtle import Screen, Turtle
import sys

class CTurtle(Turtle):
    def __init__(self):
        Turtle.__init__(self)

    def jump(self, x, y):
        self.pu()
        self.setpos(x, y)
        self.pd()
    
    def polystep(self, fwd, ang):
        self.fd(fwd)
        self.lt(ang)

    def drawSpiral(self, size):
        self.rt(30)
        for length in range(size, 0, -5):
            self.fd(length)
            self.lt(120)

screen = Screen()
screen.clear()

blue = CTurtle()
blue.jump(0, 100)
blue.color("blue", "blue")
blue.lt(90)
blue.drawSpiral(150)

red = CTurtle()
red.jump(0, -100)
red.color("red", "red")
red.rt(90)
red.drawSpiral(150)

green = CTurtle()
green.jump(-100, 0)
green.color("green", "green")
green.lt(180)
green.drawSpiral(150)

black = CTurtle()
black.jump(100, 0)
black.color("black", "black")
black.drawSpiral(150)



blue.getscreen()._root.mainloop()


