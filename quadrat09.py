
# quadrat07.py: 6 verschieden grosse Quadrate 
# neu: seite = seite - 10
from tkinter import *
from turtle import *
from math import *

reset()
pensize(5)

right(45)                  

seite = 100
aenderung = -10


def quadrat():
	global seite

	forward(seite)
	left(90)
	forward(seite)
	left(90)
	forward(seite)
	left(90)
	forward(seite)
	left(30)

	seite = seite + aenderung

def quadrat_fill():
	begin_fill()
	quadrat()
	end_fill()

pencolor("red")
fillcolor("cyan")
quadrat_fill()

pencolor("green")
fillcolor("magenta")
quadrat_fill()

pencolor("blue")
fillcolor("yellow")
quadrat_fill()

pencolor("cyan")
fillcolor("red")
quadrat_fill()


pencolor("green")
fillcolor("cyan")
quadrat_fill()
pencolor("yellow")
fillcolor("blue")
quadrat_fill()
pencolor("red")
fillcolor("cyan")
quadrat_fill()


try:
	while True:
		a = 0
except KeyboardInterrupt:
	exit()

