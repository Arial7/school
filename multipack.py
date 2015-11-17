from turtle import *
from time import *

pensize(2)
speed(0.5)

farbenpaare = (("red", "blue"), ("green", "yellow"), ("brown", "cyan"), ("red", "green"))

def dreieck(length):
    for i in range(3):
        fd(length)
        rt(120)

def fuelle_dreieck(length, penColor, fillColor):
    pencolor(penColor)
    fillcolor(fillColor)
    begin_fill()
    dreieck(length)
    end_fill()

def multipack(length, farbenpaare):
    count = len(farbenpaare)
    for pen, fill in farbenpaare:
        fuelle_dreieck(length, pen, fill)
        rt(360 / count)


def dreierpack(length, change, farbenpaare):
    for paar in farbenpaare:
        print(paar)
        pen, fill = paar
        fuelle_dreieck(length, pen, fill)
        rt(120) 

multipack(150, farbenpaare)

##INFITE LOOP
try:
    sleep(4294967296)
except KeyboardInterrupt:
    exit()

