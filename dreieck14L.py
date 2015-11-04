from turtle import *
from time import *

pensize(2)
speed(0.5)
farbenpaare = (("red", "red"), ("green", "green"), ("blue", "blue"))

def dreieck(length):
    for i in range(3):
        fd(length)
        rt(120)
    rt(120)

def multipack(length, farbenpaare):
    count = len(farbenpaare)
    for pen, fill in farbenpaare:
        fuelle_dreieck(length, pen, fill)
        rt(360 / count)

def fuelle_dreieck(length, farbe1, farbe2):
    pencolor(farbe1)
    fillcolor(farbe2)
    begin_fill()
    dreieck(length)
    end_fill()


def dreierpack(length, change, farbenpaare):

    for farbe1, farbe2 in farbenPaare:
        fuelle_dreieck(length, farbe1, farbe2)

def jump(dist, angle):
    pu()
    rt(angle)
    fd(dist)
    lt(angle)
    pd()

angle = 10
while 1:
    multipack(150, farbenpaare)
    jump(50, angle)
    angle += 50

##INFITE LOOP
try:
    sleep(4294967296)
except KeyboardInterrupt:
    exit()
