#####################################
## Project: Tip Calculator
#####################################

## Begrüßung des Nutzers
print("Welcome to the tip calculator!")

## Eingabe des Gesamtbetrags, Umwandlung in Float
bill = float(input("What was the total bill? $"))
## Eingabe des gewünschten Trinkgeld-Prozentsatzes, Umwandlung in Integer
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
## Eingabe der Anzahl der Personen, Umwandlung in Integer
people = int(input("How many people to split the bill? "))

## Umrechnung des Prozentsatzes in eine Dezimalzahl
tip_as_decimal = tip / 100  
## Berechnung des Gesamtbetrags inklusive Trinkgeld
bill_with_tip = tip_as_decimal * bill + bill  
## Berechnung des Anteils pro Person
bill_per_person = bill_with_tip / people  
## Rundung des Anteils auf 2 Dezimalstellen
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")