name = input("Dein name: ")
fach = input("Welches Fach? ")



grade1 = float(input("Note " + str(1) + ":"))
grade2 = float(input("Note " + str(2) + ":"))
grade3 = float(input("Note " + str(3) + ":"))
grade4 = float(input("Note " + str(4) + ":"))

print (name, ", dein Durschnitt in", fach, "ist", round((grade1 + grade2 + grade3 + grade4)/ 4, 2))
