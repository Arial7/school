from turtle import *

pensize(2)

def dreieck(length):
    fd(length)
    rt(120)
    fd(length)
    rt(120)
    fd(length)
    lt(120)

    
def fuelle_dreieck(length, penColor, fillColor):
    pencolor(penColor)
    fillcolor(fillColor)
    begin_fill()
    dreieck(length)
    end_fill()


    
fuelle_dreieck(110, "brown" , "blue")
fuelle_dreieck(80, "yellow" , "green")
fuelle_dreieck(50, "lime" , "red")   

##INFITE LOOP
try:
    while(1):
        time.sleep(0.1)
except KeyboardInterrupt:
    exit()


