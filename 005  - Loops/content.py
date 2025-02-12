## =====================================================
##                      Loops
## =====================================================

# Loops erlauben es, dem Computer Anweisungen zur Wiederholung zu geben,
# ohne den Code mehrfach manuell schreiben zu müssen.
# Zum Beispiel: Um die Zahlen 1 bis 100 auszugeben, wäre es sehr aufwändig,
# für jede Zahl einen print-Befehl zu schreiben.
# Mit einem Loop definierst Du eine Regel, der der Computer folgt.

## =====================================================
##             For Loops - Wiederholung über Listen
## =====================================================

# Syntax eines For Loops:
# for item in list_of_items:
#   # Führe eine Aktion für jedes Element aus
#
# Im folgenden Beispiel iterieren wir über die Liste "fruits":
fruits = ["Apple", "Peach", "Pear"]

# Hier wird jedes Element der Liste "fruits" der Variable "fruit" zugewiesen.
# Das Schlüsselwort "in" gibt an, aus welcher Liste das Element entnommen wird.
# Beim ersten Durchlauf ist fruit = "Apple", beim zweiten "Peach" usw.

for fruit in fruits:
    # Gibt das aktuelle Element in der Konsole aus.
    print(fruit) # Ausgabe: Apple, Peach, Pear
    # Zusätzlich wird für jedes Element ein weiterer String ausgegeben.
    print(fruit + " pie")

## =====================================================
##             Bedeutung der Einrückung (Indentation)
## =====================================================

# In Python ist die Einrückung (Indentation) entscheidend, da sie
# den Code in Blöcke strukturiert. Jeder Code-Block, der nach einem Doppelpunkt (:) folgt,
# muss korrekt eingerückt werden.
# Das folgende Beispiel zeigt, wie die Position der Einrückung das Verhalten verändert.
fruits = ["Banana", "Kiwi", "Strawberry"]
for fruit in fruits:
    print(fruit)
    print("Hello")

# Aus diesem Code-Beispiel:
fruits = ["Banana", "Kiwi", "Strawberry"]
for fruit in fruits:
    print(fruit)
print("Hello")
# wird "Hello" nur einmal ausgegeben, da es nicht zur Schleife gehört.

## =====================================================
##             Berechnung der Summe (Sum)
## =====================================================

# Python bietet viele eingebaute Funktionen für die Arbeit mit Zahlen.
# Die Funktion sum() berechnet die Summe aller Elemente einer Liste.
student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores) # total_score = 1146

# Aber wie funktioniert sum() im Hintergrund?
# Der folgende Code zeigt einen möglichen Weg, wie sum() implementiert sein könnte:
sum = 0
for score in student_scores:
    sum += score

print(sum)

## =====================================================
##             Bestimmung des Maximums (Max)
## =====================================================

# Python stellt die Funktionen max() und min() bereit, um das größte oder kleinste Element einer Liste zu ermitteln.
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(max(student_scores)) # Ausgabe: 199

# TODO: Diese Aufgabe ohne die Verwendung von max() lösen.
# Gegeben ist eine Liste von Prüfungswerten. Es soll der höchste Wert ausgegeben werden.
# Hierbei kommen Kenntnisse über Listen, For Loops und Conditionals zum Einsatz.
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

## =====================================================
##             For Loops mit der range() Funktion
## =====================================================

# Die Kombination aus der range() Funktion und einem For Loop ermöglicht es,
# einen Loop für eine bestimmte Anzahl von Wiederholungen auszuführen.
# Anstatt über eine Liste zu iterieren, arbeitet man hier mit einem Zahlenbereich.

## =====================================================
##             Die range() Funktion
## =====================================================

# Die range() Funktion erzeugt einen Zahlenbereich.

# Syntax:
# for number in range(a, b):
#   print(number)

# Dabei gilt: a <= number < b (der Startwert ist inklusive, der Endwert exklusive).
range(1, 10)

# Das folgende Beispiel demonstriert die Verwendung von range() in einem For Loop:
for number in range(1, 10):
    print(number) # Ausgabe: 1 2 3 4 5 6 7 8 9

# Um die Zahlen 1 bis 10 (einschließlich) auszugeben, muss der Endwert um 1 erhöht werden:
for number in range(1, 11):
    print(number) # Ausgabe: 1 2 3 4 5 6 7 8 9 10

# Standardmäßig erhöht range() den Wert um 1.
# Um einen anderen Schrittwert zu verwenden, kann ein dritter Parameter angegeben werden.
# Im folgenden Beispiel wird der Wert um 3 erhöht:
for number in range(1, 11, 3):
    print(number) # Ausgabe: 1 4 7 10

## Gauss Challenge
# Aufgabe: Berechne die Summe aller Zahlen zwischen 1 und 100 (beide inklusive).
total = 0
for number in range(0, 101):
    total += number

print(total)