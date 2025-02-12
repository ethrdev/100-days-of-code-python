# Die Funktion print() gibt den übergebenen Inhalt in der Konsole aus.
print("Hello world!")

# --- Strings und Syntax ---
# Strings in Python werden in Anführungszeichen (z. B. "Double quotes") eingeschlossen.
# Werden die Anführungszeichen nicht korrekt geschlossen, führt dies zu einem Syntax-Fehler.
# Beispiel (auskommentiert, da es einen Fehler verursacht):
# print("Hello world!)
# Moderne Editoren unterstützen Syntax-Highlighting, um solche Fehler frühzeitig zu erkennen.

# Mit "\n" wird ein Zeilenumbruch in einem String eingefügt.
print("Hello world!\nHello world!\nHello world!")

# --- String Concatenation und Bedeutung von Leerzeichen ---
# String Concatenation bedeutet, mehrere Strings zu einem neuen String zu verbinden.
# Der '+' Operator wird dazu genutzt. Hier wird "Hello" mit einem Leerzeichen und "Angela" verbunden.
print("Hello" + " " + "Angela")
# Hinweis: In Python sind Leerzeichen für die Einrückung wichtig. Fehlerhafte Einrückungen können zu Indentation Errors führen.

# --- Benutzereingaben mit input() ---
# Mit input() wird der Benutzer zur Eingabe aufgefordert.
# Der im Parameter angegebene Text dient als Prompt, der in der Konsole angezeigt wird.
print("Hello " + input("What is your name?") + "!")
# Beispiel: Gibt der Benutzer "Stefan" ein, lautet die Ausgabe "Hello Stefan!".

# --- Variablen in Python ---
# Eine Variable speichert einen Wert unter einem Namen, sodass man diesen später wiederverwenden kann.
name = input("What is your name?")
print(name)
# Vergleich: In einem Telefonbuch hilft die Zuordnung von Telefonnummern zu Namen, um die Informationen zu strukturieren.

# Variablen können ihren Inhalt ändern:
name = "Jack"
print(name)

name = "Angela"
print(name)
# Hier wird zuerst "Jack" und dann "Angela" ausgegeben, da der Wert der Variablen überschrieben wurde.

# --- Länge eines Strings ermitteln ---
# Mit len() wird die Anzahl der Zeichen eines Strings berechnet.
# Der Ablauf:
# 1. Benutzer gibt einen Namen ein.
# 2. len() berechnet die Länge des eingegebenen Strings.
# 3. Das Ergebnis wird in der Konsole ausgegeben.
print(len(input("Whats your name?")))
# Beispiel: Bei der Eingabe "Stefan" wird die Zahl 6 ausgegeben.

# --- Verwendung von Variablen zur Verbesserung der Lesbarkeit ---
username = input("Whats your name?")
length = len(username)
print(length)

# Eine gut benannte Variable erhöht die Verständlichkeit des Codes.
username_of_this_person = "Angela"
length = len(username_of_this_person)
print(length)

# --- Regeln zur Benennung von Variablen in Python ---
# 1. Wähle einen beschreibenden Namen, der den Inhalt oder Zweck der Variablen wiedergibt.
# 2. Verwende keine Leerzeichen innerhalb des Variablennamens.
# 3. Variablennamen dürfen nicht mit einer Zahl beginnen.
# 4. Nutze keine reservierten Schlüsselwörter (wie input oder print).
# 5. Bevorzuge einfache Wörter, um Tippfehler zu vermeiden.
# 6. Beachte gegebenenfalls interne Richtlinien (Company Guidelines).

