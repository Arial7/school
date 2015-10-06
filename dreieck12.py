from turtle import *
from time import *

pensize(2)
speed(0.5)
pu()
pd()

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


def dreierpack(length, change):
    fuelle_dreieck(length, "brown" , "blue")
    fuelle_dreieck(length - change, "yellow" , "green")
    fuelle_dreieck(length - change * 2, "lime" , "red")   
    
def jump(dist, angle):
    pu()
    rt(angle)    
    fd(dist)
    lt(angle) 
    pd()


angle = 10
while 1:
    dreierpack(75, 10)
    jump(50, angle)
    angle += 50

##INFITE LOOP
try:
    sleep(4294967296)
except KeyboardInterrupt:
    exit()

