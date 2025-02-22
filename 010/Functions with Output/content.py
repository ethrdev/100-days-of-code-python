## =====================================================
##             Funktionen mit Ausgabe (Output)
## =====================================================

# In diesem Abschnitt werden Funktionen vorgestellt, die Eingaben verarbeiten und einen Rückgabewert (Output) liefern.
# Wir haben bereits Funktionen ohne Rückgabewert und Funktionen mit variablen Eingaben kennengelernt – hier ergänzen wir dies durch Funktionen, die ein Ergebnis zurückliefern.

## =====================================================
##             Syntax für Funktionen mit Output
## =====================================================

# Beispiel-Syntax:
'''
def function_name(input_parameter):
    <body of function that uses input_argument>
    return output
'''
# Diese Syntax zeigt, wie man eine Funktion mit Eingabeparametern und einem Rückgabewert definiert.

## =====================================================
##             Funktion: format_name
## =====================================================

# Erstelle eine Funktion format_name(), die zwei Eingabeparameter (f_name und l_name) entgegennimmt.
def format_name(f_name, l_name):
    # Verwende die Methode title(), um die Eingabeparameter f_name und l_name in Title Case umzuwandeln.
    # Die formatierten Namen werden in den Variablen formated_f_name und formated_l_name gespeichert.
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()  
    
    # Der formatierte String wird als Rückgabewert der Funktion zurückgegeben.
    return f"{formated_f_name} {formated_l_name}"

## =====================================================
##             Aufruf der Funktion format_name
## =====================================================

# Hier wird der Funktionsaufruf demonstriert. Der Rückgabewert ersetzt den Funktionsaufruf.
# Beispiel:
# format_name(f_name = "etHer", l_name = "DeV") # Ergibt "Ether Dev"
formated_string = format_name(f_name = "etHer", l_name = "DeV")    
print(formated_string)
# Alternativ kann der Funktionsaufruf direkt in print() eingebettet werden:
print(format_name(f_name = "etHer", l_name = "DeV"))

## =====================================================
##             Beispiele bekannter Funktionen mit Ausgabe
## =====================================================

# Die built-in Funktion len() gibt die Länge eines Objekts zurück.
# Beispiel: Der Rückgabewert von len("Hello") ersetzt den Funktionsaufruf und wird in der Variable output gespeichert.
output = len("Hello")

## =====================================================
##             Print vs. Output
## =====================================================

# Unterschied zwischen return und print:
# - return: Gibt einen Wert aus der Funktion zurück, der später weiterverwendet werden kann.
# - print: Zeigt einen Wert in der Konsole an, dient hauptsächlich zur Ausgabe für den Programmierer.

## =====================================================
##             Funktionen: function_1 und function_2
## =====================================================

def function_1(text):
    # Diese Funktion verdoppelt den übergebenen Text.
    return text + text  # Beispiel: "hello" -> "hellohello"

def function_2(text):
    # Diese Funktion gibt den übergebenen Text in Title Case zurück.
    return text.title()  # Beispiel: "hello" -> "Hello"

## =====================================================
##             Verkettung von Funktionen
## =====================================================

# Hier wird gezeigt, wie der Rückgabewert einer Funktion als Eingabe für eine andere Funktion verwendet werden kann.
# Der Output von function_1 ("hellohello") wird als Input in function_2 übergeben, um den Text zu formatieren.
output = function_2(function_1("hello"))
print(output)  # Ausgabe: "Hellohello"

## =====================================================
##             Mehrere Rückgabewerte (Multiple return values)
## =====================================================

# Eine Funktion beendet ihre Ausführung, sobald der return-Befehl erreicht wird.
# Jeglicher Code nach einem return wird nicht ausgeführt.
# Durch Kontrollfluss (if/else) können mehrere return-Anweisungen innerhalb einer Funktion vorhanden sein.

## =====================================================
##             Bedingte Rückgaben (Conditional Returns)
## =====================================================

# Diese Funktion prüft, ob eine Person alkoholische Getränke kaufen darf.
# Je nach Alter wird True (Erlaubnis) oder False (keine Erlaubnis) zurückgegeben.
def canBuyAlcohol(age):
    if age >= 18:
        return True
    else:
        return False

## =====================================================
##             Leere Rückgaben (Empty Returns)
## =====================================================

# In dieser Variante der Funktion wird zusätzlich geprüft, ob der Eingabeparameter age vom Typ int ist.
# Ist dies nicht der Fall, beendet return ohne einen Wert zurückzugeben.
def canBuyAlcohol(age):
    # Überprüfe den Datentyp des Parameters age; wenn nicht int, wird die Funktion beendet.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False
    
## =====================================================
##             Challenge: Überprüfung von Schaltjahren
## =====================================================

def is_leap_year(year):
    # Ein Jahr, das durch 400 teilbar ist, ist immer ein leap year.
    if year % 400 == 0:  
        return True
    # Ein Jahr, das durch 100 teilbar ist, aber nicht durch 400, ist kein leap year.
    if year % 100 == 0:  
        return False
    # Ein Jahr, das durch 4 teilbar ist, ist ein leap year.
    if year % 4 == 0:  
        return True
    # Alle anderen Jahre sind keine leap years.
    return False
        
# Testfälle:
print(is_leap_year(2022))  # Erwartete Ausgabe: False
print(is_leap_year(2020))  # Erwartete Ausgabe: True
print(is_leap_year(2000))  # Erwartete Ausgabe: True
print(is_leap_year(1900))  # Erwartete Ausgabe: False

## =====================================================
##             Docstrings zur Dokumentation von Funktionen
## =====================================================

# Docstrings ermöglichen mehrzeilige Kommentare, die direkt unterhalb der Funktionsdefinition stehen und zur Dokumentation genutzt werden.
# Sie erscheinen beispielsweise, wenn man mit der Maus über einen Funktionsaufruf fährt.

## Syntax:
# Schreibe deinen Kommentar zwischen dreifachen Anführungszeichen.
""" 
My 
Multiline 
Comment 
"""

## Documenting Functions:
# Ein Beispiel für die Verwendung eines Docstrings zur Beschreibung einer Funktion:
def my_function(num):
    """Multiplies a number by itself."""
    return num * num