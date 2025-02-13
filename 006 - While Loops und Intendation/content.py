## =====================================================
##         Code Blocks, Functions & While Loops
## =====================================================

## =====================================================
##             Functions
## =====================================================

# Eine Funktion in Python ist ein benannter Block von Code, der zusammengefasste Anweisungen enthält.
# Beim Aufruf der Funktion wird der gesamte Code im Funktionsblock ausgeführt.
# Funktionen dienen zur Wiederverwendung von Code, reduzieren Redundanz und verbessern die Übersichtlichkeit.
#
# Wichtige Punkte:
# - Funktionen werden mit dem Keyword def definiert.
# - Nach dem Funktionsnamen folgen immer Klammern (parentheses) und ein Doppelpunkt.
# - Der Funktionskörper wird durch Einrückung (Indentation) definiert.
# - Eine Funktion muss explizit aufgerufen werden, um ausgeführt zu werden.

## Definieren einer neuen Funktion

# Beispielhafte Syntax:
#
#   def <function_name>():
#       print("Hello")
#       # Weitere Befehle
#
# Hinweis: Klammern sind obligatorisch, auch wenn keine Parameter übergeben werden.

## Aufruf einer Funktion

# Der Funktionsaufruf (call) bewirkt, dass der zuvor definierte Codeblock ausgeführt wird.
# Beispiel: <function_name>()

# Beispiel: Definieren und Aufrufen einer Funktion
def get_user_name():
    name = input("What is your name? ")
    print("Hello, " + name)
    # Innerhalb der Funktion: Verarbeitung der Benutzereingabe und Ausgabe einer Begrüßung

# Aufruf der Funktion außerhalb der Definition
print("Hello")
get_user_name() # Funktionsaufruf

# Erwartete Ausgabe:
# Hello
# What is your name?    # (Benutzer gibt z. B. "Angela" ein)
# Hello, Angela


## =====================================================
##             Hurdle Game
## =====================================================

# Dieses Beispiel (hier auskommentiert) demonstriert, wie man mit Funktionen ein kleines Spiel (Hurdle Game) umsetzt.
# Die Funktion turn_right() zeigt, wie man eine Funktion durch mehrmaliges Aufrufen einer anderen Funktion (turn_left())
# implementieren kann, um eine Drehung um 90° nach rechts zu realisieren.
#
# Die Funktion jump_hurdle() kombiniert mehrere Bewegungen (move, turn_left, turn_right), um das Überspringen eines Hindernisses zu simulieren.
#
# Der Loop for wiederholt den Sprungvorgang über eine festgelegte Anzahl von Hindernissen.
#
# Interaktive Demo (externe Umgebung): 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump_hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for jump in range(1, 7):
#     jump_hurdle()


## =====================================================
##             Indentation in Python
## =====================================================

# Die Einrückung (Indentation) in Python definiert Codeblöcke und ist essentiell für die korrekte Ausführung.
# Der PEP 8 Style Guide gibt detaillierte Empfehlungen zur Formatierung des Codes.
# Weitere Informationen: https://peps.python.org/pep-0008/
#
# Beispiel: Beide print()-Anweisungen in my_function() sind eingerückt und gehören somit zur Funktion.
def my_function():
    # Der gesamte Code in diesem Block gehört zur Funktion
    print("Hello")
    print("World")

# Beispiel: Bei my_second_function() wird "Hello" als Teil der Funktion ausgegeben;
# "World" liegt außerhalb der Funktion und wird immer ausgeführt.
def my_second_function():
    print("Hello")
print("World")


## =====================================================
##             Continuation Lines & Hanging Indents
## =====================================================

# Beim Überschreiten der Zeilenlänge sollten Codezeilen sinnvoll umgebrochen werden.
# Es gibt zwei gebräuchliche Methoden:
#
# 1. Vertikale Ausrichtung innerhalb von () , [] oder {}:
#    foo = long_function_name(var_one, var_two,
#                             var_three, var_four)
#
# 2. Verwendung eines hängenden Einzugs (hanging indent), bei dem alle Fortsetzungszeilen zusätzlich eingerückt werden:
#    def long_function_name(
#            var_one, var_two, var_three,
#            var_four):
#        print(var_one)
#
# Wichtig ist, dass die Einrückung konsistent erfolgt, um die Lesbarkeit zu gewährleisten.
#
# Falsche Einrückung kann zu Syntaxfehlern führen.

# Korrektes Beispiel (vertikale Ausrichtung):
# foo = long_function_name(var_one, var_two,
#                          var_three, var_four)

# Korrektes Beispiel (hängender Einzug):
# foo = long_function_name(
#     var_one, var_two,
#     var_three, var_four)


## =====================================================
##             Spaces vs. Tabs
## =====================================================

# Zur Einrückung in Python können sowohl Tabs als auch Spaces verwendet werden.
# Der PEP 8 Style Guide empfiehlt jedoch ausdrücklich die Verwendung von Spaces.
# Pro Einrückungsebene sollten 4 Spaces verwendet werden.
#
# Hinweise:
# - Tabs sollten nur verwendet werden, um bestehenden Code beizubehalten, der bereits Tabs nutzt,
#   oder wenn die IDE so konfiguriert ist, dass 1 Tab = 4 Spaces entspricht.
# - Eine Mischung aus Tabs und Spaces innerhalb eines Projekts kann zu unerwartetem Verhalten führen.
#
# Weitere Details: https://peps.python.org/pep-0008/


### =====================================================
##             While Loop
## ======================================================

# Ein While Loop (Schleife) führt einen Codeblock wiederholt aus, solange eine bestimmte Bedingung erfüllt ist.
# Er eignet sich besonders für Fälle, in denen die Anzahl der Wiederholungen nicht von vornherein bekannt ist.
# Achtung: Wenn die Bedingung niemals falsch wird, entsteht eine Infinite Loop (Endlosschleife).

## =====================================================
##             For Loop vs. While Loop
## =====================================================

# For Loop:
# - Iteriert über eine Sequenz (z.B. Liste, Range) und ist ideal, wenn die Anzahl der Wiederholungen bekannt ist.
a = 3
b = 5
for number in range(a, b):
    print(number)

# While Loop:
# - Wiederholt den Code, solange eine bestimmte Bedingung wahr ist.
# - Geeignet für Fälle, bei denen die Anzahl der Iterationen variabel ist.
#
# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1
#
# Alternativ:
# while not at_goal():
#     jump()

# Weitere Beispiele:
fruits = ["Apple", "Pear", "Orange"]
for fruit in range(6):
    print(fruit)

for n in range(1, 6):
    print(n)

# Hinweise:
# - For Loops enden nach der vordefinierten Iterationsanzahl und sind daher in der Regel sicherer.
# - While Loops sollten sorgfältig verwendet werden, da falsche Bedingungen zu unendlichen Loops führen können.
#   Beispiel einer Infinite Loop:

#   while 5 > 3:
#       do something


## =====================================================
##             TODO: Hurdles III
## =====================================================
# Dieses Beispiel (auskommentiert) erweitert das Hurdle Game um verschachtelte Loops:
# - Die äußere While Loop prüft, ob das Ziel erreicht ist.
# - Die innere While Loop sorgt dafür, dass sich die Figur bewegt, solange der Weg frei ist.
# - Wenn der Weg blockiert ist, wird die Funktion jump() aufgerufen.
#
# Interaktive Demo: 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# while not at_goal():
#     while front_is_clear():
#         move()
#     if not front_is_clear():
#         jump()


