#!/usr/bin/python3

from turtle import *
from random import *

# Macht die Turtle ein bisschen schneller
speed(9)
# Fenstergröße auf 800x800 Pixel ändern
setup(800, 800)

# Die Startposition der Turtle wird gespeichert
start = position()

schritte = 0
durchschnitt = 0
anzahl = 0

# Dreht sich um einen zufälligen Winkel und geht dann 10 pixel vorwärts
def zufallsschritt():
    rt(randint(1,4) * 90)
    fd(10)

def zufallsweg():
    global schritte
    global durchschnitt
    # Geht so viele Schritte, bis die Distanz zum Startpunkt mehr als 360 ist.
    while distance(start) < 350:
        zufallsschritt()
        schritte += 1
    # Nachdem genügend Schritte gemacht wurden, einen Abdruck hinterlassen
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
    # Zurück nach hause
    home()
    pd()

print("Durchschnitt", (durchschnitt / anzahl))

tracer(True)

# Das Fenster offen lassen, braucht ihr in euren Programmen nicht
while True:
    a = 0
