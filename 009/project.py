
#### Demo: Secret Auction Program
## Solution by Angela Yu

## =====================================================
##             Programmstart und Initialisierung
## =====================================================

import art
print(art.logo)  # Ausgabe des Logos aus dem art Modul zur optischen Gestaltung des Programms

## =====================================================
##             Datenspeicherung
## =====================================================

# Erzeugt ein Dictionary, um die Gebote der Teilnehmer zu speichern.
# Jeder Schlüssel repräsentiert einen Teilnehmer (Name) und der zugehörige Wert das abgegebene Gebot.
bids = {}
# Boolean-Variable zur Steuerung des Biet-Loops. Solange sie True ist, wird der Loop fortgesetzt.
continue_bidding = True

## =====================================================
##             Funktion zur Ermittlung des Höchstbietenden
## =====================================================

def find_highest_bidder(bidding_dictionary):
    # Initialisiert Variablen: 'winner' speichert den Namen des aktuellen Höchstbietenden,
    # 'highest_bid' hält das höchste bisher abgegebene Gebot.
    winner = ""
    highest_bid = 0
    # Iteriert über das Dictionary, um das höchste Gebot zu ermitteln.
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        # Überprüft, ob das aktuelle Gebot höher ist als das bisher gespeicherte höchste Gebot.
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    # Gibt das Ergebnis der Auktion aus: Name des Gewinners und dessen Gebot.
    print(f"The winner is {winner} with a bid of €{highest_bid}.")

## =====================================================
##             Hauptprogramm: Loop zum Abgeben von Geboten
## =====================================================

# Solange continue_bidding True ist, wird der Ablauf der Auktion fortgesetzt.
while continue_bidding:
    # Abfrage des Namens des aktuellen Bieters
    name = input("What is your name? ")
    # Abfrage des Gebots, Umwandlung des Eingabestrings in einen Integer
    price = int(input("What's your bid? €"))
    # Speichert den Namen und das zugehörige Gebot im bids Dictionary
    bids[name] = price
    # Fragt, ob weitere Teilnehmer ein Gebot abgeben möchten
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    # Wenn keine weiteren Bieter vorhanden sind, wird der Loop beendet und der Gewinner ermittelt.
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    # Wenn weitere Bieter vorhanden sind, wird der Bildschirm "geleert", um die vorherigen Eingaben auszublenden.
    elif should_continue == "yes":
        print("\n" * 100)