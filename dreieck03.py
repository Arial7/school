#!/usr/bin/python3

from turtle import *
from time import *

speed(0)
#draws one triangle
def triangle(length):
    fd(length)
    rt(120)
    fd(length)
    rt(120)
    fd(length)
    rt(240)
#draws one square
def square(length):
    fd(length)
    rt(90)
    fd(length)
    rt(90)
    fd(length)
    rt(90)
    fd(length)
    rt(90)
#fills one triangle
def fill_Triangle(length, fillColor, penColor):
    pencolor(penColor)
    fillcolor(fillColor)
    begin_fill()
    triangle(length)
    end_fill()
#fills one square
def fill_Square(length, fillColor, penColor):
    pencolor(penColor)
    fillcolor(fillColor)
    begin_fill()
    square(length)
    end_fill()
#draws tree triangles with the given change
def drawThreeTriangles(length, change):
    fill_Triangle(length, "green", "blue")
    length += change
    fill_Triangle(length, "magenta", "green")
    length += change
    fill_Triangle(length, "blue", "magenta")
#decide whether to draw a square or triangle
def draw(form, length):
    if form == "Square":
        fill_Square(length, "green", "blue")
    else:
        fill_Triangle(length, "green", "blue")

getForm = input("Welche Form möchtest du zeichnen?")
getlength = numinput("Input","Welche Seitenlänge soll die Form haben?")
draw(getForm,getlength)

try:
    sleep(999999)
except KeyboardInterrupt:
    exit()
