# quadrat09.py: 6 verschieden grosse Quadrate 
# neu: funktionen

from tkinter import *
from turtle import *
from math import *

reset()
pensize(5)

right(45)                  

seite = numinput("Seitenlänge", "Wie lange soll die erste Seite sein? ") 
aenderung = numinput("Änderung", "Wie soll die Änderung sein? ")

anzahl = numinput("Anzahl", "Wie viele Quadrate sollen gezeichnet werden? ")

winkel = 360.0 / anzahl

print(winkel)

def quadrat():
        global seite
        
        forward(seite)
        left(90)
        forward(seite)
        left(90)
        forward(seite)
        left(90)
        forward(seite)
        left(90)
        left(winkel)

        seite = seite + aenderung

def quadrat_fill():
	begin_fill()
	quadrat()
	end_fill()

i = 0
while(i < anzahl):
    quadrat_fill()
    i += 1

#Endlosschleife
try:
	while True:
		a = 0
except KeyboardInterrupt:
	exit()

