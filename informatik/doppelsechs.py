#!/usr/bin/python3

from random import randint 

wurfsumme = 0
anzahlspiele = 100000

for i in range(anzahlspiele):
    wurf1 = randint(1, 6)
    wurf2 = randint(1, 6)
    wuerfe = 2

    while not wurf1 == wurf2 == 6:
        wurf1 = wurf2
        wurf2 = randint(1,6)
        wuerfe += 1
    wurfsumme += wuerfe

print()
print("Versuchsreihe mit", anzahlspiele, "Spielen:")
print("Durchschnitt für zwei Sechser hintereinander:", end=" ")
print(wurfsumme / anzahlspiele)
print()
