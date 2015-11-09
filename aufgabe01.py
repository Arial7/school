#!/usr/bin/python3

#zeichnet 4 dreiecke unterschiedlicher größe

from turtle import *

pensize(4)
pencolor("red")
rt(30)

def dreieck(length):
	rt(30)
	fd(length)
	rt(120)
	fd(length)
	rt(120)
	fd(length)
	lt(180)

dreieck(200)
dreieck(100)
dreieck(200)
dreieck(100)

#Infinite loop
try:
	while True:
		a = 0

except KeyboardInterrupt:
	exit()
