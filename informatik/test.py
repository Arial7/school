name = input("Wie ist dein Name? ")
age = int(input("Wie alt bist du? "))
weekday = input("Welcher Wochentag ist heute? ")

def checkWeekday(weekday):
    if weekday.lower() == "montag":
        print("Tut mir leid, " + name + "! Das sind leider noch 4 Tage bis zum Wochenende.")
    if weekday.lower() == "dienstag":
        print("Immerhin nur noch drei Tage bis zum Wochenende!")
    if weekday.lower() == "mittwoch":
        print("Kopf hoch! In zwei Tagen ist es so weit.")
    if weekday.lower() == "donnerstag":
        print("Du hast's schon bald geschafft. Nur noch 1 Tag bis zum Wochenende!")
    if weekday.lower() == "freitag" or "samstag" or "sonntag":
        print("Hoch die Hände Wochenende!")

checkWeekday(weekday)
