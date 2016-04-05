#!/usr/bin/python3

from turtle import Screen, Turtle
from time import sleep
import sys

sys.setrecursionlimit(20000)

screen = Screen()
screen.setup(800, 600)
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
def fillRed(x, y):
    pen.fillcolor("red")
def fillBlue(x, y):
    pen.fillcolor("blue")
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

blueFill = Turtle()
blueFill.shape("square")
blueFill.shapesize(1, 1, 3)
blueFill.pu()
blueFill.setpos(-260, 300)
blueFill.onclick(fillBlue)
blueFill.color("black", "blue")


redFill = Turtle()
redFill.shape("square")
redFill.shapesize(1, 1, 3)
redFill.pu()
redFill.setpos(-260, 280)
redFill.onclick(fillRed)
redFill.color("black", "red")

helperStampID = 0

helper = Turtle()
helper.shape("square")
helper.shapesize(20, 20, 3)
helper.pu()
helper.setpos(0,0)
helper.color("cyan", "red")
helper.hideturtle()

def togglefill(x, y):
    if pen.filling(): 
        pen.end_fill()
    else: 
        pen.begin_fill()

def show_help():
    helperStampID = helper.stamp()
    helper.write("HILFE, ich bin zu dumm, dieses Programm zu benutzen!!!", True, "center")
    helper.showturtle()

def hide_help():
    helper.clearstamp(helperStampID)
    helper.hideturtle()

screen.onkeypress(pen.undo, "BackSpace")
screen.onkeypress(pen.clear, "x")
screen.onkeypress(show_help, "F1")
screen.onkeypress(hide_help, "Escape")


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
