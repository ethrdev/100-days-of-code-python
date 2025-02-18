#### Demo: Secret Auction Program
## Solution by ethR

## =====================================================
##             Programmbeschreibung
## =====================================================

# The goal is to build a blind auction program.
# Ziel des Programms ist es, eine anonyme (blind) auction zu realisieren,
# bei der Teilnehmer ihren Namen und ihr Gebot eingeben und der Höchstbietende ermittelt wird.

## =====================================================
##             Initialisierung der Variablen
## =====================================================

# Boolean-Variable, um zu steuern, ob die Auktion fortgesetzt wird.
auction_to_continue = True

# Dictionary zur Speicherung der Gebote.
# Jeder key repräsentiert den Namen eines Bieters (in Kleinbuchstaben), 
# und jeder value das zugehörige Gebot.
auction_dictionary = {}

## =====================================================
##             Haupt-Auktionsloop
## =====================================================

while auction_to_continue:
    # Eingabe des Namens des Bieters und Umwandlung in Kleinbuchstaben
    user_name = input("What is your name? ").lower()
    # Eingabe des Gebots und Konvertierung in einen Integer
    user_bid = int(input("What's your bid? €"))
    # Speicherung des Namens und Gebots im Dictionary
    auction_dictionary[user_name] = user_bid
    
    # Abfrage, ob weitere Bieter vorhanden sind
    other_bidders_exist = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if other_bidders_exist == "yes":
        # Falls weitere Bieter teilnehmen, wird der Loop fortgesetzt
        auction_to_continue = True
        # Clear the output: Simuliert das Leeren des Bildschirms durch viele Leerzeilen
        print("\n" * 100)
    elif other_bidders_exist == "no":
        # Falls keine weiteren Bieter vorhanden sind, wird der Loop beendet
        auction_to_continue = False

## =====================================================
##             Ausgabe der gesammelten Gebote
## =====================================================

# Ausgabe des gesamten Dictionary mit allen Bieterdaten
print(auction_dictionary)

## =====================================================
##             Ermittlung des Höchstbietenden
## =====================================================

# Initialisierung der Variablen für das höchste Gebot und den entsprechenden Bieter
highest_bid = int(0)
highest_bidder = ""

# Iteration über das Dictionary, um den Bieter mit dem höchsten Gebot zu finden
for key in auction_dictionary:
    # Wenn das aktuelle Gebot größer oder gleich dem bisherigen höchsten Gebot ist,
    # wird das höchste Gebot aktualisiert und der entsprechende Bieter gespeichert.
    if auction_dictionary[key] >= highest_bid:
        highest_bid = int(auction_dictionary[key])
        highest_bidder = str(key)

# Ausgabe des Gewinners und des höchsten Gebots
print(f"The winner is {highest_bidder} with a bid of €{highest_bid}.")
