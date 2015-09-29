# quadrat07.py: 6 verschieden grosse Quadrate 
# neu: seite = seite - 10
from turtle import *
from math import *

reset()
pensize(5)
speed(0)

right(45)                  

startseite = numinput("Seitenlänge", "Wie lange soll die erste Seite sein?")
seite = startseite
aenderung = numinput("Änderung", "Wie groß soll die Änderung sein?")
quadratAnzahl = numinput("Anzahl der Quadrate", "Wie viele Quadrate sollen gezeichnet werden?", 4, 2, 360)
winkel = 360 / quadratAnzahl
colors = ["red","green","blue","yellow","brown", "pink"]

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
while(i < quadratAnzahl):
	fillcolor(colors[i % 6])
	quadrat_fill()
	i += 1

if quadratAnzahl > 4:
	seite = startseite
	fillcolor(colors[0])
	begin_fill()
	forward(seite)
	left(90)
	forward(seite)
	end_fill()

hideturtle()
	
try:
	while True:
		a = 0
except KeyboardInterrupt:
	exit()