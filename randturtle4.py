#!/usr/bin/python3

from turtle import *
from random import *

winkel = numinput(0, 10, 40)
laenge = numinput(1, 3, 15)


speed(9)

setup(800, 800)

start = position()

def zufallsschritt(wink, laen):
    rt(randint(winkel * -1, winkel))
    fd(randint(1, laenge))
def zufallsweg(wink, laen):
    while distance(start) < 350:
        zufallsschritt(wink, laen)
    stamp()

tracer(False)

for i in range(200):
    zufallsweg(winkel, laenge)
    home()

tracer(True)

while True:
    a = 0
