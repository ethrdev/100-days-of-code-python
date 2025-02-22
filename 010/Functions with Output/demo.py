## =====================================================
##             Calculator
## =====================================================
#  First try version by ethr
#  Analyse am Dateiende

# Importiere das Logo aus dem art-Modul, um es später im Programm anzuzeigen.
from art import logo

# Ausgabe des Logos in der Konsole.
print(logo)

## =====================================================
##             Funktionen als Variablen speichern
## =====================================================

# Definiert die Funktion 'add', die zwei Zahlen addiert.
def add(n1, n2):
    return n1 + n2

# Speichere die Funktion 'add' als Variable, um sie später flexibel aufzurufen.
my_favourite_calculation = add
my_favourite_calculation(3, 5)  # Liefert 8

## =====================================================
##             Definition weiterer mathematischer Funktionen
## =====================================================

# Definiert die Funktion 'subtract', die zwei Zahlen subtrahiert.
def subtract(n1, n2):
    return n1 - n2

# Definiert die Funktion 'multiply', die zwei Zahlen multipliziert.
def multiply(n1, n2):
    return n1 * n2

# Definiert die Funktion 'divide', die zwei Zahlen dividiert.
def divide(n1, n2):
    return n1 / n2

## =====================================================
##             Zuordnung der Operationen in einem Dictionary
## =====================================================

# Erstelle ein leeres Dictionary, in dem die Operatoren als Schlüssel und die zugehörigen Funktionen als Werte gespeichert werden.
arithmetic_methods = {}
arithmetic_methods["+"] = add
arithmetic_methods["-"] = subtract
arithmetic_methods["*"] = multiply
arithmetic_methods["/"] = divide

# Ausgabe des Dictionaries zur Kontrolle der Zuordnung.
print(arithmetic_methods)

# Beispiel: Verwende den Dictionary-Zugriff, um 4 * 8 zu berechnen.
print(arithmetic_methods["*"](4, 8))

## =====================================================
##             Initialisierung von Variablen für die Berechnungen
## =====================================================

# Flag, ob mit dem aktuellen Ergebnis weitergerechnet werden soll.
calc_to_continue = True
# Variable für den Startwert (wird hier nicht direkt genutzt).
number_to_begin_with = 0
# Variable zur Speicherung des aktuellen Ergebnisses.
result = 0
# Flag, ob die Anwendung weiterläuft.
app_runs = True

## =====================================================
##             Interaktive Berechnungsschleife
## =====================================================

while app_runs:
    # Fordere den Benutzer auf, die erste Zahl einzugeben.
    first_chosen_number = float(input("Please type your first number: "))

    # Fordere den Benutzer auf, einen mathematischen Operator ('+', '-', '*' oder '/') auszuwählen.
    chosen_operator = str(input("Choose your operation... '+', '-', '*' or '/': "))

    # Fordere den Benutzer auf, die zweite Zahl einzugeben.
    second_chosen_number = float(input("Please type your second number: "))

    # Berechne das Ergebnis basierend auf der gewählten Operation und gebe es aus.
    result = float(arithmetic_methods[chosen_operator](first_chosen_number, second_chosen_number))
    print(result)

    # Frage den Benutzer, ob er mit dem bisherigen Ergebnis weiterrechnen möchte.
    user_want_to_continue = str(input("Do you want to continue with the privious result? Type 'y' for yes and 'n' for no: "))
    
    if user_want_to_continue == "y" or user_want_to_continue == "yes":
        calc_to_continue = True
        
    # Falls der Benutzer fortfahren möchte, starte eine Schleife, um mit dem bisherigen Ergebnis weiterzurechnen.
    while calc_to_continue:
        # Fordere erneut den mathematischen Operator ab.
        chosen_operator = input("Choose your operation... '+', '-', '*' or '/': ")
        # Fordere die nächste Zahl ab.
        next_chosen_number = float(input("Please type your next number: "))
        # Berechne das neue Ergebnis basierend auf dem aktuellen Ergebnis und der neuen Zahl.
        result = float(arithmetic_methods[chosen_operator](result, next_chosen_number))
        print(result)
        # Frage den Benutzer, ob er weiterhin mit dem aktuellen Ergebnis rechnen möchte.
        user_want_to_continue = str(input("Do you want to continue with the previous result? Type 'y' for yes and 'n' for no: "))
    
        # Falls der Benutzer nicht weitermachen möchte, verlasse die innere Schleife und starte von vorn.
        if user_want_to_continue == "n" or user_want_to_continue == "no":
                calc_to_continue = False


## =====================================================
##         Code Review und Vergleich zu project.py
## =====================================================

# Ich habe einen Loop statt Rekursion um eine stabilere Programmausführung sicherzustellen.

### Issues

# Keine Validierung von Eingaben.
# Division durch Null ist nicht abgefangen.
# Das Dictionary arithmetic_methods wird unnötig nachträglich gefüllt: Direkte Initialisierung wäre übersichtlicher.
# Die doppelte Abfrage, ob der Nutzer weiterrechnen möchte (while calc_to_continue) könnte eleganter gelöst werden
# Unklare Variablennamen: calc_to_continue, app_runs, number_to_begin_with sind nicht intuitiv.