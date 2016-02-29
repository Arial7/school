#!/usr/bin/python3

from turtle import Screen, Turtle
from time import sleep
import sys

sys.setrecursionlimit(20000)

screen = Screen()
screen.clear()
pen = Turtle()
pen.speed(0)
pen.shape("circle")
pen.shapesize(0.4, 0.4, 3)
pen.pensize(3)

pen.fillcolor("black")

def togglefill(x, y):
    if pen.filling(): 
        pen.end_fill()
    else: 
        pen.begin_fill()

screen.onkeypress(pen.undo, "BackSpace")
screen.onkeypress(pen.clear, "x")

for c in "123456789":
    def setpensize(ps=int(c)):
        pen.pensize(ps)
    screen.onkeypress(setpensize, c)



screen.onclick(togglefill)
pen.ondrag(pen.goto)

def jump(x, y):
    pen.pu()
    pen.goto(x, y)
    pen.pd()

screen.onclick(jump, 3)

screen.listen()
pen.getscreen()._root.mainloop()
