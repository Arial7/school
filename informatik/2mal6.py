#!/usr/bin/python3

from random import *

i = 0 #Wie oft eine 6 gewürfelt wurde
k = 0 #Wie oft gewürfelt wurde
durchschnitt = 0 # Wie viele Versuche im Durchschnitt benötigt wurden

tests = 100

# Erhöht k um eins, gibt eine zufällige Zahl zurück
def wuerfeln():
    global k
    k += 1
    return randint(1,6)

# Überprüft, ob zwei mal eine 6 gewürfelt wurde
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

# Führt `tests` Versuche durch
def versuchsreihe():
    for i in range(tests):
        zweiMal()
    print("Im Durchschnitt muss", durchschnitt / tests, "mal gewürfelt werden");

versuchsreihe()
