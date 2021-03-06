from math import *

def getMax(array):
	maxNum = array[0]
	for currNum in array:
		maxNum = max(currNum, maxNum)
	return maxNum

def solvePQ(p, q):
	x = list()
	x.append((-p/2) + sqrt((p/2)**2 - q))
	x.append((-p/2) - sqrt((p/2)**2 - q))

	return x

def solveABC(a, b, c):
	x = list()	
	x.append(-b + (sqrt(b**2 - 4 * a * c) / (2 * a)))
	x.append(-b - (sqrt(b**2 - 4 * a * c) / (2 * a)))

	return x


def TESTRUN():
	print("getmax returned: ", getMax([0, -15, 5, 100, 312])) 
	x = solvePQ(10, 2)
	print("solvePQ returned: ", x[0])
	x2 = solveABC(1, 10, 2)
	print("solveABC returned: ", x2[0])

TESTRUN()
