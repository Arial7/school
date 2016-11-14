#!/usr/bin/python3

#uses a for loop to draw some triangles

from turtle import *
from time import *

pensize(2)
speed(6)
colorPairs = (("red", "red"), ("green", "green"), ("blue", "blue"), ("yellow", "yellow"), ("brown", "brown"))

def triangle(length):
    for i in range(3):
        fd(length)
        rt(120)
    #rt(120)

def multipack(length, colorPairs):
    #draw as many triangles as there are color pairs
    count = len(colorPairs)
    #assign the variables
    for pen, fill in colorPairs:
        fill_triangle(length, pen, fill)
        lt(360 / count)

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

multipack(150, colorPairs)
