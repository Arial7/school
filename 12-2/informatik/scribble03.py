#!/usr/bin/python3

from turtle import Screen, Turtle
from time import sleep
import sys

sys.setrecursionlimit(20000)

screen = Screen()
screen.clear()
stift = Turtle()
stift.speed(0)
stift.shape("circle")
stift.shapesize(0.4, 0.4, 3)
stift.pensize(3)

stift.fillcolor("black")

def togglefill(x, y):
    if stift.filling(): 
        stift.end_fill()
    else: 
        stift.begin_fill()

screen.onclick(togglefill)
stift.ondrag(stift.goto)

def jump(x, y):
    stift.pu()
    stift.goto(x, y)
    stift.pd()

screen.onclick(jump, 3)

stift.getscreen()._root.mainloop()
