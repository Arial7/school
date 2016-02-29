#!/usr/bin/python3

from random import *

i = 0 #Wie oft eine 6 gewürfelt wurde
k = 0 #Wie oft gewürfelt wurde
durchschnitt = 0

tests = 100

def wuerfeln():
    global k
    k += 1
    return randint(1,6)


def zweiMal():
    global i
    global k
    global durchschnitt
    while i < 2:
        ergebnis = wuerfeln()
        if ergebnis == 6:
            i += 1
    print("Es wurde", k, "mal gewürfelt")   
    durchschnitt += k
    k = 0
    i = 0

def versuchsreihe():
    for i in range(tests):
        zweiMal()
    print("Im Durchschnitt muss", durchschnitt / tests, "mal gewürfelt werden");

versuchsreihe()
