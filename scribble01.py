#!/usr/bin/python3

from turtle import Screen, Turtle
from time import sleep


screen = Screen()
screen.clear()
stift = Turtle()
stift.speed(0)
stift.shape("circle")
stift.shapesize(0.4, 0.4, 3)
stift.pensize(3)
screen.onclick(stift.goto)


stift.getscreen()._root.mainloop()
