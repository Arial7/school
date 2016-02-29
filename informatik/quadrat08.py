
# quadrat05.py: 6 verschieden grosse Quadrate 
# neu: seite = seite - 10

from turtle import *

reset()
pensize(5)

right(45)                  
seite = 100


def draw():
	global seite
	begin_fill()
	forward(seite)
	left(90)
	forward(seite)
	left(90)
	forward(seite)
	left(90)
	forward(seite)
	left(90)
	end_fill()

	right(60)

color("red", "cyan")
draw()

color("green", "magenta")
draw()

color("blue", "yellow")
draw()

color("cyan", "red")
draw()

color("green", "cyan")
draw()

color("yellow", "blue")
draw()

try:
	while True:
		a = 0
except KeyboardInterrupt:
	exit()

