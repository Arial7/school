#!/usr/bin/python3
# © 2016 - Pascal Riesinger
# License: MIT
# Description: Ein kleines Banksystem

import random
import string
import os

benutzer = list()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Benutzer():
    def __init__(self, name, passwort):
        self.name = name
        self.passwort = passwort
        self.konto = Konto(self)

    def login(self, passwort):
        if self.passwort is passwort:
            return True
        return False

class Konto():
    def __init__(self, inhaber, stand = 0):
        self.inhaber = inhaber
        self.stand = stand
        # Eine zufällige Nummer wird generiert
        self.nummer = ''.join(random.choice(string.digits) for _ in range(10))

    def buchen(self, wert):
        self.stand += wert


class Bildschirm():
    def __init__(self, titel, nachricht):
        self.titel = titel
        self.nachricht = nachricht

    def zeigen(self):
        clear()
        print("\t\t===", self.titel, "===")
        print(self.nachricht)
        return input("\t")

def transaktion(benutzer):
    while True:
        kontoBildschirm = Bildschirm("Willkommen " + benutzer.name,
        """
        Was wollen Sie tun?
        1) Geld abheben
        2) Geld einzahlen
        3) Geld überweisen (Noch nicht verfügbar)
        4) Abmelden
        """)

        wahl = kontoBildschirm.zeigen()
        if wahl is "4":
            break
        elif wahl is "1":
            if benutzer.konto.stand < 0:
                Bildschirm("Transaktion", 
                """
                Sie haben kein Geld... Sie können sich nichts auszahlen lassen
                """).zeigen()
            else:
                summenBildschirm = Bildschirm("Transaktion",
                """
                Wie viel möchten Sie abheben?
                """)
                benutzer.konto.buchen(int("-" + summenBildschirm.zeigen()))
        elif wahl is "2":
            summenBildschirm = Bildschirm("Transaktion",
            """
            Wie viel möchten Sie einzahlen?
            """)
            benutzer.konto.buchen(int(summenBildschirm.zeigen()))


                

     
def login():
    global benutzer
    nameBildschirm = Bildschirm("Login",
        """
        Geben Sie Ihren Namen ein
        """)
    name = nameBildschirm.zeigen()
    passwortBildschirm = Bildschirm("Login",
        """
        Geben Sie Ihr Passwort ein
        """)
    passwort = passwortBildschirm.zeigen()
    aktuellerBenutzer = None
    for b in benutzer:
        if (b.name == name) and (b.passwort == passwort):
            aktuellerBenutzer = b
            break

    if not aktuellerBenutzer is None:
        transaktion(aktuellerBenutzer)
    else:
        Bildschirm("Login",
        """
        Es gibt keinen Benutzer mit diesem Namen, oder das Passwort ist falsch
        """).zeigen()



def neuerBenutzer():
    global benutzer
    nameBildschirm = Bildschirm("Neuer Benutzer", 
        """
        Geben Sie Ihren Namen ein
        """)
    name = nameBildschirm.zeigen()
    passwortBildschirm = Bildschirm("Neuer Benutzer",
        """
        Geben Sie ein Passwort ein
        """)
    passwort = passwortBildschirm.zeigen()
    Bildschirm("Neuer Benutzer", 
        """
        Ein neues Konto wurde erstellt
        """).zeigen()

    benutzer.append(Benutzer(name, passwort))

while True:
    hauptmenu = Bildschirm("Willkommen bei der Heussbank",
        """
        Was wollen Sie tun?
        1) Login
        2) Neuen Benutzer anlegen
        """)

    wahl = hauptmenu.zeigen()

    if wahl is "1":
        login()
    elif wahl is "2":
        neuerBenutzer()
    elif wahl is "q":
        print("\n\n\t\tUnd Tschuess!")
        exit()
        


