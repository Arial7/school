# Neues: if-Anweisungen

frage = "Welche Programmiersprache lernst du gerade? "
loesung = "python"

antwort = input(frage)
if antwort.lower() == loesung:
	print("Richtig!")
	exit()
else:
	print("Leider falsch!")