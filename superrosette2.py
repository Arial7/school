#!/usr/bin/python3

from turtle import*
reset()

hideturtle()
anzahl=18
laenge=20
bgcolor("black")
a=0
b=1

def neck(anzahl, laenge):
    for i in range(anzahl):
        global a        
        global b
        pencolor(a,0,b)
        forward(laenge)
        left(winkel)
        a=a+(1/18)
        b=b-(1/18)
    for i in range(anzahl):
        global a
        global b
        pencolor(a,0,b)
        forward(laenge)
        left(winkel)
        a=a-(1/18)
        b=b+(1/18)


def rosette(anzahl):
    global winkel
    winkel=360/36
    for i in range(36):
        neck(anzahl, laenge)
        right(winkel)

tracer(False)
rosette(anzahl)
tracer(True)

while True:
    lllll = 0
