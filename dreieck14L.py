#!/usr/bin/python3

#uses a for loop to draw some triangles

from turtle import *
from time import *

pensize(2)
speed(0.5)
colorPairs = (("red", "red"), ("green", "green"), ("blue", "blue"))

def triangle(length):
    for i in range(3):
        fd(length)
        rt(120)
    rt(120)

def multipack(length, colorPairs):
    #draw as many triangles as there are color pairs
    count = len(colorPairs)
    #assign the variables
    for pen, fill in colorPairs:
        fill_triangle(length, pen, fill)
        rt(360 / count)

def fill_triangle(length, penColor, fillColor):
    pencolor(penColor)
    fillcolor(fillColor)
    begin_fill()
    triangle(length)
    end_fill()


def dreierpack(length, change, colorPairs):
    #assign vars
    for pen, fill in colorPairs:
        fill_triangle(length, pen, fill)

def jump(dist, angle):
    pu()
    rt(angle)
    fd(dist)
    lt(angle)
    pd()

angle = 10
while 1:
    multipack(150, colorPairs)
    jump(50, angle)
    angle += 50
