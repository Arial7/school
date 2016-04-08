#!/usr/bin/python3

from turtle import Screen, Turtle
import sys

# Neues Fenster erstellen und allen Inhalt löschen
screen = Screen()
screen.clear()

# Erstellt die blaue Turtle und setzt sie zu ihrer Startposition
blue = Turtle()
blue.pu()
blue.color("blue", "blue")
blue.setpos(0, 100)
blue.pd()
blue.lt(90)

# Erstellt die rote Turtle und setzt sie zu ihrer Startposition
red = Turtle()
red.pu()
red.setpos(0, -100)
red.color("red", "red")
red.pd()
red.rt(90)

# Erstellt die grüne Turtle und setzt sie zu ihrer Startposition
green = Turtle()
green.pu()
green.setpos(-100, 0)
green.color("green", "green")
green.pd()
green.lt(180)

# Erstellt die schwarze Turtle und setzt sie zu ihrer Startposition
black = Turtle()
black.pu()
black.setpos(100, 0)
black.color("black", "black")
black.pd()

# Zeichnet eine dreickige "Spirale"
# @param turtle {Turtle} - Die Turtle mit der die Spirale gezeichnet werden
# soll
def drawSpiral(turtle):
    turtle.rt(30)
    length = 150
    while length > 0:
        turtle.fd(length)
        turtle.lt(120)
        turtle.fd(length - 5)
        turtle.lt(120)
        turtle.fd(length - 10)
        turtle.lt(120)
        length -= 15


drawSpiral(black)
drawSpiral(green)
drawSpiral(red)
drawSpiral(blue)

# Ist für diese Anwendung wahrscheinlich gar nicht benötigt
blue.getscreen()._root.mainloop()


