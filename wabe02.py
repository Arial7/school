
from turtle import*

def wabe():
	begin_fill()
	fd(50)
	rt(60)
	fd(50)
	rt(60)
	fd(50)
	rt(60)
	fd(50)
	rt(60)
	fd(50)
	rt(60)
	fd(50)
	end_fill()

pensize(5)
pencolor("brown")
fillcolor("yellow")

#1
wabe()
lt(60)
fillcolor("orange")
#2
wabe()
lt(60)
#3
wabe()
rt(60)
fd(50)
lt(60)
#4
wabe()
rt(60)
fd(50)
lt(60)
#5
wabe()
rt(60)
fd(50)
lt(60)
#6
wabe()
rt(60)
fd(50)
lt(60)
#7
wabe()



#infinte loop
try:
	while True:
		a = 0 
except KeyboardInterrupt:
	exit()
