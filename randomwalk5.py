#!/usr/bin/python3

from turtle import *
from random import *

winkel = numinput(0, 10, 40)
laenge = numinput(1, 3, 15)


speed(9)

setup(800, 800)

start = position()

schritte = 0
durchschnitt = 0
anzahl = 0

def zufallsschritt(wink, laen):
    if distance(start) > 225:
        pencolor("green")
    elif distance(start) > 175:
        pencolor("yellow")
    elif distance(start) > 75:
        pencolor("red")
    else:
        pencolor("blue")
    rt(randint(winkel * -1, winkel))
    fd(randint(1, laenge))
    
def zufallsweg(wink, laen):
    global schritte
    global durchschnitt
    while distance(start) < 350:
        zufallsschritt(wink, laen)
        schritte += 1
    stamp()
    print("Schritte", schritte)
    durchschnitt += schritte
    schritte = 0

tracer(False)

for i in range(200):
    global anzahl
    zufallsweg(winkel, laenge)
    anzahl += 1
    pu()
    home()
    pd()

print("Durchschnitt", (durchschnitt / anzahl))

tracer(True)

while True:
    a = 0
