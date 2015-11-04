from turtle import *
from time import *

speed(0)

def triangle(lenght):
    fd(lenght)
    rt(120)
    fd(lenght)
    rt(120)
    fd(lenght)
    rt(240)

def square(lenght):
    fd(lenght)
    rt(90)
    fd(lenght)
    rt(90)
    fd(lenght)
    rt(90)
    fd(lenght)
    rt(90)

def fill_Triangle(lenght, fillColor, penColor):
    pencolor(penColor)
    fillcolor(fillColor)
    begin_fill()
    triangle(lenght)
    end_fill()

def fill_Square(lenght, fillColor, penColor):
    pencolor(penColor)
    fillcolor(fillColor)
    begin_fill()
    square(lenght)
    end_fill()

def drawThreeTriangles(lenght, change):
    fill_Triangle(lenght, "green", "blue")
    lenght += change
    fill_Triangle(lenght, "magenta", "green")
    lenght += change
    fill_Triangle(lenght, "blue", "magenta")

def draw(form, lenght):
    if form == "Square":
        fill_Square(lenght, "green", "blue")
    else:
        fill_Triangle(lenght, "green", "blue")

#def jump(distance, angle):
#    pu()
#    rt(angle)
#    fd(distance)
#    lt(angle)
#    pd()
#    drawThreeTriangles(100, 0)

getForm = input("Welche Form möchtest du zeichnen?")
getLenght = numinput("Input","Welche Seitenlänge soll die Form haben?")
draw(getForm,getLenght)

try:
    sleep(999999)
except Keyboardinterupt:
    exit()
