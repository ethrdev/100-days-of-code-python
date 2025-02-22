## =====================================================
##             Calculator
## =====================================================
# Written by Dr. Angela Yu

# Importiere das Modul "art", welches z.B. ein ASCII-Art Logo für den Calculator enthält.
import art

## =====================================================
##             Funktion add (Addition)
## =====================================================

# Diese Funktion berechnet die Summe von n1 und n2.
def add(n1, n2):
    return n1 + n2
        
# Funktionen sind in Python "first class citizens".
# Das heißt, man kann sie als Variablen speichern und später aufrufen.
my_favourite_calculation = add
my_favourite_calculation(3, 5)  # Liefert 8 zurück

## =====================================================
##             Weitere mathematische Operationen
## =====================================================

# In der Ausgangsdatei wird ein Dictionary verwendet, das jedem mathematischen Operator
# die entsprechende Funktion zuweist.
# Hier werden zusätzlich die Funktionen für Subtraktion, Multiplikation und Division definiert.

# Subtraktion: Berechnet die Differenz zwischen n1 und n2.
def substract(n1, n2):
    return n1 - n2

# Multiplikation: Berechnet das Produkt von n1 und n2.
def multiply(n1, n2):
    return n1 * n2

# Division: Berechnet den Quotienten von n1 und n2.
def divide(n1, n2):
    return n1 / n2

## =====================================================
##             Dictionary der Operationen
## =====================================================

# Das Dictionary "operations" ordnet jedem mathematischen Operator die entsprechende Funktion zu.
# Die Schlüssel sind die Operator-Symbole als Strings, die Werte sind die Funktionsreferenzen.
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

# Mit dem Dictionary können Berechnungen durchgeführt werden.
# Beispiel: Multiplikation von 4 * 8
# print(operations["*"](4, 8))

## =====================================================
##             Funktion calculator (Hauptprogramm)
## =====================================================

# Diese Funktion realisiert einen einfachen Taschenrechner.
def calculator():
    # Zeige das ASCII-Art Logo an, das im art Modul definiert ist.
    print(art.logo)
    
    # Flag, das steuert, ob mit dem aktuellen Ergebnis weitergerechnet werden soll.
    should_accumulate = True

    # Fordere den Benutzer auf, die erste Zahl einzugeben.
    num1 = float(input("What is the first number?: "))
        
    while should_accumulate:
        # Zeige alle verfügbaren Operationen (Operator-Symbole) an.
        for symbol in operations:
            print(symbol)

        # Lese den gewünschten mathematischen Operator vom Benutzer ein.
        operation_symbol = input("Pick an operation: ")

        # Fordere den Benutzer auf, die nächste Zahl einzugeben.
        num2 = float(input("What is the next number? "))

        # Berechne das Ergebnis, indem die entsprechende Funktion aus dem Dictionary aufgerufen wird.
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Frage, ob mit dem aktuellen Ergebnis weitergerechnet werden soll.
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation")

        # Wenn der Benutzer "y" eingibt, wird das Ergebnis als neue Ausgangszahl verwendet.
        if choice == "y":
            num1 = answer
        else:
            # Falls nicht, beenden wir die aktuelle Berechnungsschleife,
            # leeren den Bildschirm (durch mehrere Zeilenumbrüche)
            # und starten den Taschenrechner rekursiv neu.
            should_accumulate = False
            print("\n" * 20) 
            calculator()  # Rekursion wird verwendet, um den Rechner neu zu starten.
        
    # Nach Verlassen der while-Schleife (bei "n") wird der Benutzer erneut aufgefordert,
    # eine neue Berechnung zu starten (durch den rekursiven Aufruf der Funktion).

# Starte den Taschenrechner.
calculator()