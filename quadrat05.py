
# quadrat05.py: 6 verschieden grosse Quadrate 
# neu: seite = seite - 10

from turtle import *

reset()
pensize(5)

right(45)                  

seite = 100
change = -75

pencolor("red")
fillcolor("cyan")
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
seite = seite + change

pencolor("green")
fillcolor("magenta")
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
seite = seite + change

pencolor("blue")
fillcolor("yellow")
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

seite = seite + change
pencolor("cyan")
fillcolor("red")
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

seite = seite + change
pencolor("green")
fillcolor("cyan")
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

seite = seite + change
pencolor("yellow")
fillcolor("blue")
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
