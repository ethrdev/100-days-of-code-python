## =====================================================
##             Bedingte Anweisungen (Conditional Statements)
## =====================================================
## Mit bedingten Anweisungen (Conditionals) in Python überprüfst Du
## bestimmte Bedingungen und bestimmst, welche Codeblöcke ausgeführt werden.
## Beispiel:
## if condition:
##     do this

## =====================================================
##             If-Else Struktur
## =====================================================
## Mit der if/else-Struktur wird ein Codeblock ausgeführt, wenn die if-Bedingung wahr ist,
## andernfalls wird der else-Codeblock ausgeführt.
## Beispiel:
## if condition:
##     do this
## else:
##     do this

## =====================================================
##             Einrückung in Python
## =====================================================
## In Python ist die Einrückung (Indentation) essenziell, da sie die Zugehörigkeit
## von Codeblöcken bestimmt. Eine falsche Einrückung führt zu einem Indentation Error.
## Beispiel:
## if condition:
##     do this   # Dieser Block gehört zur if-Bedingung

## =====================================================
##             Vergleichsoperatoren
## =====================================================
## Folgende Vergleichsoperatoren werden in Python genutzt:
##   >   Greater than (größer als)
##   <   Less than (kleiner als)
##   >=  Greater than or equal to (größer oder gleich)
##   <=  Less than or equal to (kleiner oder gleich)
##   ==  Equal to (gleich)
##   !=  Not equal to (ungleich)

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

## =====================================================
##             Überprüfung der Mindestgröße
## =====================================================
## Überprüft, ob die eingegebene Höhe größer als 120 cm ist.
if height > 120:
    ## Der folgende Codeblock wird ausgeführt, wenn die Bedingung wahr ist.
    print("You can ride the rollercoaster.")
 ## Dieser else-Block wird ausgeführt, falls die Bedingung nicht erfüllt ist.
else:
    ## Hier wird ausgegeben, dass die Mindestgröße nicht erreicht wurde.
    print("Sorry you have to grow taller before you can ride.")
    

## =====================================================
##             Modulo Operator (%)
## =====================================================
## Der Modulo Operator % liefert den Rest einer Division.
## Beispiele:
##   6 % 2 gibt 0 zurück (6 ist durch 2 ohne Rest teilbar)
##   6 % 5 gibt 1 zurück
##   6 % 4 gibt 2 zurück
print(6 % 2) ## Gibt 0 zurück, da 6 ohne Rest durch 2 teilbar ist.
print(6 % 5) ## Gibt 1 zurück, da der Rest 1 beträgt.
print(6 % 4) ## Gibt 2 zurück.

## =====================================================
##             Test: Gerade oder Ungerade?
## =====================================================
## Überprüft, ob die eingegebene Zahl gerade (Even) oder ungerade (Odd) ist.
number_to_check = int(input("Choose a number."))
if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")

## =====================================================
##             Verschachtelte if/else Strukturen
## =====================================================
## Mit verschachtelten if/else-Strukturen können mehrere Bedingungen
## innerhalb anderer Bedingungen geprüft werden.
## Beispiel:
## if condition:
##    if another condition:
##       do this
##    else:
##       do that
## else:
##     do another thing

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 18:
        print("Please pay 7€.")
    else:
        print("Please pay 12€.")
else:
    print("Sorry you have to grow taller before you can ride.")

## =====================================================
##             if / elif / else Struktur
## =====================================================
## Mit der if / elif / else-Struktur kannst Du mehrere aufeinanderfolgende
## Bedingungen abfragen. Nur der Block der ersten wahren Bedingung wird ausgeführt.
## Beispiel:
## if condition1:
##     do A
## elif condition2:
##     do B
## else:
##     do C
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster ")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay 5€. ")
    elif age <=18:
        print("Please pay 7€. ")
    else:
        print("Please pay 12€. ")
else:
    print("Sorry you have to grow taller before you can ride. ")

## =====================================================
##             Mehrfache if-Anweisungen
## =====================================================
## Mehrere unabhängige if-Anweisungen erlauben die Prüfung einzelner Bedingungen,
## bei denen mehrere Codeblöcke ausgeführt werden können.
## Beispiel:
## if condition1:
##    do A
## if condition2:
##    do B
## if condition3:
##    do C

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want to have a photo taken? Type y for yes and n for No.")
    if wants_photo == "y":
        # Füge dem Ticketpreis 3$ hinzu, falls ein Foto gewünscht ist.
        bill += 3  # bill = bill + 3

    print(f"Your final bill is {bill}$")
else:
    print("Sorry you have to grow taller before you can ride.")


## =====================================================
##             Challenge: Python Pizza
## =====================================================
## Basierend auf den Eingaben des Nutzers wird die finale Rechnung
## für eine Pizza-Bestellung ermittelt.
##
## Preisübersicht:
##   - Small pizza (S): $15
##   - Medium pizza (M): $20
##   - Large pizza (L): $25
##
## Zusätzlich:
##   - Für kleine Pizza: Pepperoni (+$2) falls gewünscht.
##   - Für Medium/Large Pizza: Pepperoni (+$3) falls gewünscht.
##   - Extra cheese für jede Pizza: (+$1) falls gewünscht.
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# TODO: Ermittle den Grundpreis anhand der gewählten Pizzagröße.
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")

# TODO: Füge den Aufpreis für Pepperoni hinzu, je nach Pizzagröße.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")


## =====================================================
##             Logische Operatoren
## =====================================================
## Mit logischen Operatoren kannst Du mehrere Bedingungen kombinieren:
##   - and: Beide Bedingungen müssen wahr sein.
##   - or: Es reicht, wenn mindestens eine Bedingung wahr ist.
##   - not: Kehrt den Wahrheitswert einer Bedingung um.
##
## Beispiel:
## if condition1 and condition2:
##     do this
## else:
##     do that
##
## Wahrheitstabellen:
##   - TRUE and TRUE  -> TRUE
##   - TRUE and FALSE -> FALSE
##   - FALSE and TRUE -> FALSE
##   - TRUE or FALSE  -> TRUE
##   - FALSE or FALSE -> FALSE
##   - not FALSE      -> TRUE
##   - not TRUE       -> FALSE

## =====================================================
##             Sonderfall: Freifahrt für Altersgruppe 45-55
## =====================================================
##
## Aktualisiere den Code so, dass Personen im Alter von 45 bis 55 Jahren (inklusive)
## kostenlos fahren. Hierbei wird geprüft, ob das Alter im gewünschten Bereich liegt.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:  # alternativ: elif 45 <= age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
    
