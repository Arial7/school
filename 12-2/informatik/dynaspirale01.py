#!/usr/bin/python3

from turtle import Screen, Turtle
import sys


screen = Screen()
screen.clear()

blue = Turtle()
blue.pu()
blue.color("blue", "blue")
blue.setpos(0, 100)
blue.pd()
blue.lt(90)

red = Turtle()
red.pu()
red.setpos(0, -100)
red.color("red", "red")
red.pd()
red.rt(90)

green = Turtle()
green.pu()
green.setpos(-100, 0)
green.color("green", "green")
green.pd()
green.lt(180)

black = Turtle()
black.pu()
black.setpos(100, 0)
black.color("black", "black")
black.pd()

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

blue.getscreen()._root.mainloop()


