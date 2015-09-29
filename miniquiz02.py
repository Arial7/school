# Neues: if-Anweisungen
punkte = 0

frageAntwort = {
	"Welche Programmiersprache lernst du gerade? ":"python",
	"Mit welchem reservierten Wort beginnt eine Funktionsdefinition? ":"def",
	"Wie viele reservierten Worte hat Python? ":"33",
	"Welcher Wochentag ist heute? ":"dienstag"
}

for frage in frageAntwort:
	antwort = input(frage)
	if antwort.lower() == frageAntwort[frage]:
		print("Richtig!")
		punkte += 1	
	else:
		print("Falsch!")
if punkte == 1:
    print("Du hast einen Punkt erreicht!")
else:
    print("Du hast", punkte, "Punkte erreicht!")