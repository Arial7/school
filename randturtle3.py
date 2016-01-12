#!/usr/bin/python3

from turtle import *
from random import *

winkel = numinput(0, 10, 40)
laenge = numinput(1, 3, 15)
schritte = numinput(1, 5, 50)

def zufallsschritt(wink, laen):
    rt(randint(winkel * -1, winkel))
    fd(randint(1, laenge))

def zufallsweg(schritt, wink, laen):
    for i in range(0, int(schritt)):
        zufallsschritt(wink, laen)

zufallsweg(schritte, winkel, laenge)

while True:
    a = 0
