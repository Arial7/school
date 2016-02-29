#!/usr/bin/python3

from turtle import Screen, Turtle
from time import sleep
import sys

sys.setrecursionlimit(20000)

screen = Screen()
screen.setup(800, 800)
screen.clear()
pen = Turtle()
pen.speed(0)
pen.shape("circle")
pen.shapesize(0.4, 0.4, 3)
pen.pensize(3)

pen.fillcolor("black")

def setblue(x, y):
    pen.pencolor("blue")
def setred(x, y):
    pen.pencolor("red")

blueButton = Turtle()
blueButton.shape("square")
blueButton.shapesize(1, 1, 3)
blueButton.pu()
blueButton.setpos(-300, 280)
blueButton.onclick(setblue)
blueButton.color("blue", "blue")

redButton = Turtle()
redButton.shape("square")
redButton.shapesize(1, 1, 3)
redButton.pu()
redButton.setpos(-300, 260)
redButton.onclick(setred)
redButton.color("red", "red")

def togglefill(x, y):
    if pen.filling(): 
        pen.end_fill()
    else: 
        pen.begin_fill()

screen.onkeypress(pen.undo, "BackSpace")
screen.onkeypress(pen.clear, "x")

for c in "123456789":
    def setpensize(ps=int(c)):
        pen.pensize(ps)
    screen.onkeypress(setpensize, c)



screen.onclick(togglefill)
pen.ondrag(pen.goto)

def jump(x, y):
    pen.pu()
    pen.goto(x, y)
    pen.pd()

screen.onclick(jump, 3)

screen.listen()
pen.getscreen()._root.mainloop()
