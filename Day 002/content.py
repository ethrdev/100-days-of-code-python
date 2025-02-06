#####################################
## Python Primitive Data Types und Grundlagen
#####################################

## --- Subscripting (Indexierung von Strings) ---
## Mit Subscripting können wir einzelne Zeichen eines Strings abrufen.
## Dabei entspricht der Index 0 dem ersten Zeichen.
print("Hello"[0])  # Ausgabe: 'H'

## Abrufen des zweiten Zeichens:
print("Hello"[1])  # Ausgabe: 'e'

## Abrufen des fünften Zeichens:
print("Hello"[4])  # Ausgabe: 'o'

## Negative Indizes erlauben den Zugriff von hinten:
## -1 greift auf das letzte Zeichen zu.
print("Hello"[-1])  # Ausgabe: 'o'
## -2 greift auf das vorletzte Zeichen zu.
print("Hello"[-2])  # Ausgabe: 'l'


## --- Zahlen (Integers, Floats, Boolean) ---
## Integers sind ganze Zahlen.
print(123 + 345)  # Addition von zwei Integers

## Große Zahlen können zur besseren Lesbarkeit mit '_' getrennt werden.
print(123_456_789)  # Python ignoriert '_' in Integern.

## Float = Gleitkommazahl (Kommazahl)
print(3.14159)

## Boolean-Werte sind entweder True oder False.
print(True)
print(False)


## --- Type Errors und Type Checking ---
## Fehler bei ungültigen Datentypoperationen, z.B.:
## print(len(12345))  # Würde einen TypeError erzeugen

## Mit type() lässt sich der Datentyp eines Wertes ermitteln:
print(type("Hello"))   # Ausgabe: <class 'str'>
print(type(12345))     # Ausgabe: <class 'int'>
print(type(123.45))    # Ausgabe: <class 'float'>
print(type(True))      # Ausgabe: <class 'bool'>


## --- Type Conversion (Typumwandlung / Casting) ---
## Strings können durch Verkettung zusammengefügt werden:
print("123" + "456")   # Ausgabe: '123456'

## Um numerische Berechnungen durchzuführen, konvertiere die Strings:
print(int("123") + int("456"))  # Ausgabe: 579

## Hinweis: Bei ungültigen Umwandlungen (z.B. Buchstaben) entsteht ein ValueError:
## print(int("abc") + int("456"))

## Folgende Funktionen werden zur Typumwandlung genutzt:
## int(), float(), str(), bool()


## --- Lösung zur Fehlerbehebung bei String-Concatenation mit int ---
## Problem: "TypeError: can only concatenate str (not 'int') to str"
name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

# Überprüfe die Datentypen
print(type("Number of letters in your name: "))  # <class 'str'>
print(type(length_of_name))                        # <class 'int'>

# Um den Integer zu einem String zu machen, wird str() verwendet:
print("Number of letters in your name: " + str(length_of_name))

# Alternativ in einer Zeile:
print("Number of letters in your name: " + str(len(input("Enter your name"))))


## --- Mathematische Operatoren ---
## Addition, Subtraktion und Multiplikation:
print(123 + 456)  # Addition
print(7 - 3)      # Subtraktion
print(3 * 2)      # Multiplikation

## Division führt aufgrund von implizitem Type Casting immer zu einem Float:
print(6 / 3)      # Ausgabe: 2.0
print(type(6 / 3))  # <class 'float'>

## Ganzzahlige Division (Floor Division) entfernt Nachkommastellen:
print(5 // 3)     # Ausgabe: 1
print(type(5 // 3))  # <class 'int'>

## Potenzieren (Exponents)
print(2**2)  # 4
print(2**3)  # 8
print(2**4)  # 16

## PEMDAS-Regel (Reihenfolge der Operationen):
## Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print(3 * 3 + 3 / 3 - 3)    # Ohne Klammern, Ergebnis: 7.0
print(3 * (3 + 3) / 3 - 3)  # Mit Klammern, Ergebnis: 3.0


## --- Number Manipulation, Flooring und Rounding ---
## Beispiel: Berechnung des BMI
bmi = 84 / 1.65 ** 2
print(bmi)

## Flooring: Entfernt alle Dezimalstellen durch int()-Konvertierung.
print(int(3.738492))  # Ausgabe: 3

## Rounding: Rundet Zahlen. Bei .5 wird aufgerundet, darunter abgerundet.
print(round(3.738492))       # Ausgabe: 4
print(round(3.14159))        # Ausgabe: 3
print(round(3.14159, 2))     # Ausgabe: 3.14

print(int(bmi))              # Ausgabe: Ganzzahliger BMI (z.B. 30)
print(round(bmi))            # Gerundeter BMI (z.B. 31)
print(round(bmi, 2))         # Auf 2 Dezimalstellen gerundet (z.B. 30.85)
print(round(bmi, 5))         # Auf 5 Dezimalstellen gerundet (z.B. 30.85399)


## --- Assignment Operators (Zuweisungsoperatoren) ---
## Erlaubt es, den aktuellen Wert einer Variable direkt zu modifizieren.
score = 2
score += 1  # Entspricht: score = score + 1  --> score ist jetzt 3
score -= 1  # score = score - 1  --> score ist jetzt 2
score *= 1  # score = score * 1  --> score bleibt 2
score /= 1  # score = score / 1  --> score wird zu 2.0


## --- f-Strings ---
## f-Strings ermöglichen das direkte Einfügen von Variablen oder Ausdrücken in einen String.
print("Your score is " + str(score))        # Mit String-Konkatenation
print(f"Your score is {score}")              # Mit f-String, einfacher und übersichtlicher

## f-Strings unterstützen auch mehrere Datentypen:
score = 0
height = 1.8
is_winning = True
print(f"Your score is {score}, your height is {height}. You are winning is {is_winning}.")


