from turtle import *

pensize(2)

def dreieck(length):
    fd(length)
    rt(120)
    fd(length)
    rt(120)
    fd(length)
    lt(120)

    
def fuelle_dreieck(length, color):
    fillcolor(color)
    begin_fill()
    dreieck(length)
    end_fill()


    
fuelle_dreieck(110, "blue")
fuelle_dreieck(80, "green")
fuelle_dreieck(50, "red")   

##INFITE LOOP
try:
    while(1):
        never_used_variable_name_that_is_super_awesome_and_never_used = 0
except KeyboardInterrupt:
    exit()


