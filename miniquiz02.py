#!/usr/bin/python3

# Neues: if-Anweisungen
punkte = 0

name = input("Sag mir deinen Name bitte: ")

#Dictionary -> not learned yet
frageAntwort = {
	"Welche Programmiersprache lernst du gerade? " : "python",
	"Mit welchem reservierten Wort beginnt eine Funktionsdefinition? " : "def",
	"Wie viele reservierten Worte hat Python? " : "33",
	"Welcher Wochentag ist heute? " : "dienstag"
}

for frage in frageAntwort:
	antwort = input(frage)
	if antwort.lower() == frageAntwort[frage]:
		print("Richtig!")
		punkte += 1
	else:
		print("Falsch!")
if punkte == 0:
    print("Du bist dumm!")
elif punkte > 0 and punkte < len(frageAntwort):
	print("Wow, bist du toll!!! ", punkte, " Punkte!!!")
else:
    print("Alle Antorten richtig!!!")

print("Tschüss, ", name)
