## =====================================================
##             Funktionen mit Eingaben
## =====================================================

# In diesem Abschnitt lernen wir, wie man Funktionen in Python definiert und verwendet.
# Eine Funktion fasst einen Codeblock zusammen, der mehrfach ausgeführt werden kann.

## TODO: Erstelle eine Funktion namens greet().
# Schreibe drei print-Anweisungen innerhalb der Funktion.
# Rufe anschließend die Funktion greet() auf und führe den Code aus.
def greet():
        print("Hello")
        print("How do you do?")
        print("Isn't the weather nice today?")
greet()

## =====================================================
##             Funktionen mit Parametern
## =====================================================

# Hier wird gezeigt, wie Funktionen Eingaben (Inputs) entgegennehmen können.
# Durch die Angabe eines Variablennamens in den Klammern beim Definieren der Funktion
# können wir der Funktion Daten übergeben, die ihr Verhalten steuern.
# Vergleich: Der Computer (Funktion) kann unterschiedliche "USB-Sticks" (Inputs) lesen und dementsprechend handeln.

# Funktion mit einem Parameter erstellen
def greet_with_name(name):
    print(f"Hey! {name}")
# Funktion mit Argument aufrufen
greet_with_name("ethR") 
# Ausgabe: "Hey! ethR"

## =====================================================
##             Parameter und Argumente
## =====================================================

# Beim Definieren einer Funktion wird der Parameter als Platzhalter für den übergebenen Wert verwendet.
# Beim Aufrufen der Funktion wird der tatsächliche Wert, also das Argument, übergeben.
# Beispiel: In der Funktion this_function wird der Parameter "something" mit dem Wert 123 gefüllt.
def this_function(something):
    print(something)
this_function(123) # Ausgabe: 123

## =====================================================
##             Positional vs. Keyword Arguments
## =====================================================

# Funktionen können mehrere Eingaben (Parameter) haben, die durch Kommas getrennt werden.
# Es gibt zwei Methoden, um Argumente an Funktionen zu übergeben:
#   - Positional Arguments: Werte werden in der Reihenfolge übergeben, wie die Parameter definiert wurden.
#   - Keyword Arguments: Werte werden explizit den jeweiligen Parametern zugewiesen.
# Dies reduziert Verwechslungen, besonders bei Funktionen mit mehreren Parametern.

## TODO: Erstelle eine Funktion mit mehreren Eingaben und passe sie so an, dass die erwarteten Werte ausgegeben werden.
def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")
greet_with("ethR", "Berlin") # Ausgabe: Hello ethR. What is it like in Berlin?

# Beim Vertauschen der Argumentreihenfolge ändert sich die Ausgabe, da immer der erste übergebene Wert als erster Parameter dient.
greet_with("Berlin", "ethR") # Ausgabe: Hello Berlin. What is it like in ethR?

## =====================================================
##             Positional Arguments
## =====================================================

# Standardmäßig werden Argumente in der Reihenfolge zugeordnet, in der sie in der Funktionsdefinition erscheinen.
def my_function(a, b, c):
  print(a, b, c)
  
my_function(1, 2, 3) # Ausgabe: 1 2 3
my_function(3, 2, 1) # Ausgabe: 3 2 1
my_function(2, 3, 1) # Ausgabe: 2 3 1

## =====================================================
##             Keyword Arguments
## =====================================================

# Mit Keyword Arguments können wir beim Funktionsaufruf explizit festlegen, welcher Wert welchem Parameter zugeordnet wird.
# Dadurch spielt die Reihenfolge der Argumente keine Rolle.
my_function(a=1, b=2, c=3) # Ausgabe: 1 2 3
my_function(c=3, b=2, a=1) # Ausgabe: 1 2 3
my_function(b=2, c=3, a=1) # Ausgabe: 1 2 3

## TODO: Rufe die Funktion greet_with() mithilfe von Keyword Arguments auf.
greet_with(name="ethR", location="Berlin") # Ausgabe: Hello ethR. What is it like in Berlin?

## =====================================================
##             Beispiel: Love Score Berechnung
## =====================================================

# Diese Funktion berechnet einen "Love Score" basierend auf den Buchstaben in zwei Namen.
# Vorgehen:
#   1. Beide Namen werden in Großbuchstaben umgewandelt und aneinandergereiht.
#   2. Es werden die Vorkommen der Buchstaben aus "TRUE" gezählt.
#   3. Ebenso werden die Vorkommen der Buchstaben aus "LOVE" gezählt.
#   4. Der Love Score wird als Kombination der beiden Zählwerte (als String) ausgegeben.

def calculate_love_score(first_name, second_name):
    both_names = first_name.upper() + second_name.upper()
    true_count = 0
    love_count = 0
    
    for true_letter in both_names:
        if true_letter in "TRUE":
            true_count += 1
    
    for love_letter in both_names:
        if love_letter in "LOVE":
            love_count += 1
    
    love_score = str(true_count) + str(love_count)
    print(love_score)
            
calculate_love_score(first_name="EthR", second_name="Angela Bauer")