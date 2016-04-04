#!/usr/bin/python3

from turtle import *
from random import *

speed(9)

setup(800, 800)

start = position()

schritte = 0
durchschnitt = 0
anzahl = 0

def zufallsschritt():
    rt(randint(1,4) * 90)
    fd(10)
    
def zufallsweg():
    global schritte
    global durchschnitt
    while distance(start) < 350:
        zufallsschritt()
        schritte += 1
    stamp()
    print("Schritte", schritte)
    durchschnitt += schritte
    schritte = 0

tracer(False)

for i in range(10):
    global anzahl
    zufallsweg()
    anzahl += 1
    pu()
    home()
    pd()

print("Durchschnitt", (durchschnitt / anzahl))

tracer(True)

while True:
    a = 0
