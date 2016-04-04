
# quadrat07.py: 6 verschieden grosse Quadrate 
# neu: seite = seite - 10
from tkinter import *
from turtle import *
from math import *

reset()
pensize(5)

right(45)                  

seite = 50
change = 0

orig_seite = seite

def quadrat():
	forward(seite)
	left(90)
	forward(seite)
	left(90)
	forward(seite)
	left(90)
	forward(seite)
	left(90)

def quadrat_fill():
	begin_fill()
	quadrat()
	end_fill()

pencolor("red")
fillcolor("cyan")




pencolor("green")
fillcolor("magenta")

pencolor("blue")
fillcolor("yellow")


pencolor("cyan")
fillcolor("red")



pencolor("green")
fillcolor("cyan")

pencolor("yellow")
fillcolor("blue")

pencolor("red")
fillcolor("cyan")


try:
	while True:
		a = 0
except KeyboardInterrupt:
	exit()

