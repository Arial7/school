#!/usr/bin/python3

frage = "Welche Programmiersprache lernst du gerade? "
loesung = "python"

antwort = input(frage)
if antwort.lower() == loesung:

    print ("Richtig!")
else:
    print ("Falsch!")
