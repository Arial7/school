#!/usr/bin/python3

from turtle import Screen, Turtle
import sys

# Für ausfühlichere Dokumentation bitte in 'dynaspirale02.py' nachschauen.
# Hier ist nur die Klasse CTurtle geändert.

class CTurtle(Turtle):
    # Der Konstruktor nimmt hier zwei optionale Parameter an.
    def __init__(self, angle=0, color="black"):
        Turtle.__init__(self)
        self.rt(angle)
        self.color(color, color)

    def jump(self, x, y):
        self.pu()
        self.setpos(x, y)
        self.pd()
    
    def polystep(self, fwd, ang):
        self.fd(fwd)
        self.lt(ang)

    def drawSpiral(self, size):
        self.rt(30)
        for length in range(size, 0, -5):
            self.fd(length)
            self.lt(120)

screen = Screen()
screen.clear()

# Hier müssen die Parameter übergeben werden, da sie vom Standardwert abweichen
blue = CTurtle(270, "blue")
red = CTurtle(90, "red")
green = CTurtle(180, "green")
# Hier brauch man keine Parameter, da sie identisch mit dem Standard sind.
black = CTurtle()

# ACHTUNG!
# Wollte man eine rote Turtle, die aber dennoch um 0° gedreht ist, müsste man
# auch die 0 übergeben. Ansonsten versucht Python, den String "red" in die
# Variable 'angle' zu schreiben, ihr wurde jedoch vorher durch die 
# Standardzuweisung der Wert 0 also der Typ Integer zugewiesen.
#
# Anders herum ist das kein Problem, wenn man nur die Drehung ändern möchte 
# aber nicht die Farbe, kann man die CTurtle einfach mit
# name = CTurtle(110)
# erstellen, für die Farbe wird dann der Standardwert verwendet.


blue.jump(0, 100)
blue.drawSpiral(150)

red.jump(0, -100)
red.drawSpiral(150)

green.jump(-100, 0)
green.drawSpiral(150)

black.jump(100, 0)
black.drawSpiral(150)


blue.getscreen()._root.mainloop()


