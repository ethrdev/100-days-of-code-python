## =====================================================
##             Demo: Password Generator
## =====================================================

# Ziel: Erstelle ein Programm, das vom Benutzer die Anzahl der gewünschten Zeichen (letters, symbols, numbers)
# abfragt und daraus ein zufälliges Passwort generiert.
# Nutze dein Wissen über Python Listen und Loops, um diese Aufgabe zu lösen.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

## =====================================================
##             Simple Version
## =====================================================

# In dieser Version wird das Passwort in fester Reihenfolge erzeugt:
# Zuerst werden die Buchstaben, dann die Symbole und zuletzt die Zahlen angehängt.
# Beispiel: Bei 4 Buchstaben, 2 Symbolen und 3 Zahlen könnte das Passwort so aussehen: fgdx$*924.
# Hinweis: Die einzelnen Zeichentypen werden gruppiert, was das Passwort vorhersehbar machen kann.

# Unser Passwort wird als String aufgebaut.
password = ""

# Erzeuge die Buchstaben für das Passwort:
# Durchlaufe einen Loop von 1 bis (nr_letters + 1) und hänge in jedem Durchlauf
# einen zufällig ausgewählten Buchstaben aus der Liste 'letters' an das Passwort an.

for char in range(1, nr_letters + 1):
    # Wähle zufällig einen Buchstaben und füge ihn per String-Konkatenation hinzu.
    password += random.choice(letters)

# Erzeuge die Symbole für das Passwort:
# Durchlaufe einen Loop für die gewünschte Anzahl der Symbole und füge in jedem Durchlauf
# einen zufällig ausgewählten Symbol aus der Liste 'symbols' an das Passwort an.

for char in range(0, nr_symbols):
    password += random.choice(symbols)

# Erzeuge die Zahlen für das Passwort:
# Durchlaufe einen Loop für die gewünschte Anzahl der Zahlen und füge in jedem Durchlauf
# eine zufällig ausgewählte Zahl aus der Liste 'numbers' an das Passwort an.

for char in range(0, nr_numbers):
    password += random.choice(numbers)

# Ausgabe des ungemischten Passworts.
print(f"Your unshuffled password is: {password}")


## =====================================================
##             Passwort Generator mit gemischter Reihenfolge
## =====================================================

# In dieser Version wird die Reihenfolge der Zeichen zufällig gemischt.
# Dazu werden zunächst alle gewünschten Zeichen in einer Liste gesammelt.
# Anschließend wird diese Liste mit random.shuffle() durcheinander gewürfelt und
# zum Schluss mit join() zu einem String zusammengefügt.

# Erstelle eine leere Liste, in der alle Passwortzeichen gesammelt werden.
password_list = []

# Füge zufällig ausgewählte Buchstaben der Passwortliste hinzu.
# Der Loop läuft so oft, wie der Benutzer Buchstaben wünscht.

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

# Füge zufällig ausgewählte Symbole der Passwortliste hinzu.
# Der Loop läuft so oft, wie der Benutzer Symbole wünscht.

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# Füge zufällig ausgewählte Zahlen der Passwortliste hinzu.
# Der Loop läuft so oft, wie der Benutzer Zahlen wünscht.

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# Mische die Passwortliste, um die Reihenfolge der Zeichen zu randomisieren.
# Dadurch werden die zuvor gruppierten Zeichen (Buchstaben, Symbole, Zahlen) zufällig angeordnet.
random.shuffle(password_list)

# Kombiniere die Elemente der Passwortliste zu einem einzigen String.
# Die Methode join() fügt alle Listenelemente ohne Trennzeichen zusammen.
password = ''.join(password_list)

# Ausgabe des finalen, gemischten Passworts.
print(f"Your shuffled password is: {password}")