#!/usr/bin/python3

from turtle import Screen, Turtle
import sys

# Subklasse von Turtle welche einige Helfermethoden definiert
class CTurtle(Turtle):
    # Der Konstruktor
    # @param self {CTurtle} - Das erstellte Objekt, wird automatisch 
    # generiert und muss nicht übergeben werden.
    def __init__(self):
        # Ruft den Konstruktor der Superklasse auf, dabei wird das
        # erstellt Objekt übergeben.
        Turtle.__init__(self)

    # Springt zu einer angegebenen x und y Koordinate
    # @param self {CTurtle} - Das Objekt, auf der die Funktion ausgeführt
    # wird. Wird automatisch übergeben.
    # @param x {Integer} - Die x-Koordinate von der Mitte des Fensters
    # @param y {Integer} - Die y-Koordinate von der Mitte des Fensters
    def jump(self, x, y):
        self.pu()
        self.setpos(x, y)
        self.pd()
   
    # Zeichnet eine dreieckige "Spirale"
    # @param self {CTurtle} - Das Objekt, auf der die Funktion ausgeführt
    # wird. Wird automatisch übergeben.
    # @param size {Integer} - Die erste Kantenlänge.
    def drawSpiral(self, size):
        self.rt(30)
        for length in range(size, 0, -5):
            self.fd(length)
            self.lt(120)

screen = Screen()
screen.clear()

# Erstellt ein neues Objekt vom Typ CTurtle.
blue = CTurtle()
# Springt 100px nach oben
blue.jump(0, 100)
blue.color("blue", "blue")
blue.lt(90)
blue.drawSpiral(150)

red = CTurtle()
red.jump(0, -100)
red.color("red", "red")
red.rt(90)
red.drawSpiral(150)

green = CTurtle()
green.jump(-100, 0)
green.color("green", "green")
green.lt(180)
green.drawSpiral(150)

black = CTurtle()
black.jump(100, 0)
black.color("black", "black")
black.drawSpiral(150)


# Wird für dieses Programm wahrscheinlich nicht benötigt.
blue.getscreen()._root.mainloop()


