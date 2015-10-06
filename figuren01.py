from turtle import *
from time import *

pensize(2)

def triangle(length, penColor, fillColor):
    pencolor(penColor)
    fillcolor(fillColor)
    begin_fill()
    fd(length)
    rt(120)
    fd(length)
    rt(120)
    fd(length)
    lt(120)
    end_fill()

def square(length, penColor, fillColor):
    pencolor(penColor)
    fillcolor(fillColor)
    begin_fill()
    fd(length)
    rt(90)
    fd(length)
    rt(90)
    fd(length)
    rt(90)
    fd(length)
    rt(90)
    end_fill()    

def figure(name, length):
    if name == "square":
        square(length, "yellow", "red")
    elif name == "triangle":
        triangle(length, "red", "yellow")
    else:
        print("wrong figure name")

fig = input("Which figure do you want? (square/triangle) ")
length = numinput("INPUT", "How large should one side be? ")
figure(fig, length)

##INFITE LOOP
try:
    sleep(4294967296)
except KeyboardInterrupt:
    exit()

