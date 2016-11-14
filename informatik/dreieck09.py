#!/usr/bin/python3

from turtle import *

pensize(2)

def dreieck(length):
    fd(length)
    rt(120)
    fd(length)
    rt(120)
    fd(length)
    lt(120)


def fuelle_dreieck(length, penColor, fillColor):
    pencolor(penColor)
    fillcolor(fillColor)
    begin_fill()
    dreieck(length)
    end_fill()



fuelle_dreieck(110, "brown" , "blue")
fuelle_dreieck(80, "yellow" , "green")
fuelle_dreieck(50, "lime" , "red")

##INFITE LOOP
try:
    time.sleep(999999999)
except KeyboardInterrupt:
    exit()
