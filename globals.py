#!/usr/bin/python3

x = 999
y = 4

def noGlobal():
	x = 2 * y

def useGlobal():
	#use the globally defined x
	global x
	x = 2 * y

noGlobal()
print(x)
useGlobal()
print(x)
