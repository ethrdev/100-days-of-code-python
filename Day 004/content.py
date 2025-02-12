## =====================================================
##             Randomisation and Python Lists
## =====================================================

# Hinweis: Computer erzeugen keine echten Zufallszahlen, da sie deterministisch arbeiten.
# Zufälligkeit ist jedoch entscheidend – beispielsweise in Spielen, um unvorhersehbare Abläufe zu ermöglichen.
# Würde jede Aktion im Spiel vorbestimmt sein, wäre das Spiel schnell langweilig.

## =====================================================
##             Pseudorandom number generators
## =====================================================

# Da Computer deterministisch sind, werden pseudorandom number generators (PRNGs) verwendet,
# um scheinbar zufällige Zahlen zu erzeugen.
# Beispiele hierfür sind der Mersenne Twister.
# Weitere Informationen: https://en.wikipedia.org/wiki/Mersenne_Twister
# Video-Erklärung: https://www.youtube.com/watch?v=GtOt7EBNEwQ&ab_channel=KhanAcademyLabs

## =====================================================
##             Random Module
## =====================================================

# Das Python random Modul enthält zahlreiche Funktionen zur Erzeugung von Zufallszahlen.
# Dokumentation: https://docs.python.org/3/library/random.html
# Zur Verwendung des Moduls muss es zunächst importiert werden:
import random

## =====================================================
##             Random Whole Numbers within a range
## =====================================================

# Mit random.randint(a, b) wird eine zufällige Ganzzahl N erzeugt, so dass a <= N <= b.
# Beispiel: Erzeugt eine Zufallszahl zwischen 1 und 10 (einschließlich):
random_integer = random.randint(1, 10)
print(random_integer)

## =====================================================
##             Modules
## =====================================================

# In Python können Module dazu verwendet werden, Code in verschiedene Dateien zu organisieren.
# Dadurch können Funktionen und Variablen in unterschiedlichen Dateien wiederverwendet werden,
# was zu einer besseren Strukturierung und Modularisierung des Codes führt.

## =====================================================
##             Random Floats with random.random()
## =====================================================

# Mit random.random() wird eine Zufalls-Float im Bereich [0.0, 1.0) erzeugt.
# Auch wenn der Funktionsaufruf keine Parameter benötigt, müssen die leeren Klammern dennoch stehen.
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

# Durch Multiplikation kann der Wertebereich erweitert werden, z.B.:
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

## =====================================================
##             Random Floats with uniform()
## =====================================================

# Die Funktion random.uniform(a, b) gibt eine Zufalls-Float N zurück, sodass:
# a <= N <= b (bzw. b <= N <= a, wenn b < a).
# Hinweis: Die obere Grenze kann aufgrund von Rundungsfehlern eventuell nicht exakt erreicht werden.
random_float = random.uniform(1, 10)
print(random_float)

# Je nachdem, ob du die obere Grenze einbeziehen möchtest, wählst du zwischen random.random() (mit Multiplikation)
# oder random.uniform().

## =====================================================
##             Demo: Heads or Tails
## =====================================================

# Diese Demo simuliert einen Münzwurf, bei dem 0 für "Heads" und 1 für "Tails" steht.
coin_flip_number = random.randint(0, 1)

if coin_flip_number == 0:
    print("Heads")
else:
    print("Tails")

## =====================================================
##             Listen in Python
## =====================================================

# Eine List ist eine grundlegende Datenstruktur in Python, die geordnete Sammlungen von Elementen speichert.
# Sie ermöglicht es, mehrere Daten (auch verschiedener Typen) zusammenzufassen und ihre Reihenfolge beizubehalten.

## =====================================================
##             Syntax von Listen
## =====================================================

# Listen werden in eckigen Klammern definiert, z.B.:
# [item1, item2]

# Eine Liste kann einer Variablen zugewiesen werden, wie im folgenden Beispiel:
fruits = ["Cherry", "Apple", "Pear"]

# Anstatt jeden US-Bundesstaat einzeln als Variable zu definieren, werden alle in einer Liste gespeichert:
state1 = "Delaware"
state2 = "Pennsylvania"
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina",
                     "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio",
                     "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida",
                     "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska",
                     "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
                     "Arizona", "Alaska", "Hawaii"]

## =====================================================
##             Zugriff und Reihenfolge in Listen
## =====================================================

# Der Index bestimmt die Reihenfolge der Elemente in einer Liste. In Python beginnt die Zählung bei 0.
print(states_of_america[0])  # Ausgabe: Delaware
print(states_of_america[1])  # Ausgabe: Pennsylvania
print(states_of_america[4])  # Ausgabe: Connecticut

## =====================================================
##             Negative Indices in Listen
## =====================================================

# Mit negativen Indizes kann man Elemente von hinten aus einer Liste abrufen.
print(states_of_america[-1])  # Ausgabe: Hawaii (letztes Element)
print(states_of_america[-2])  # Ausgabe: Alaska
print(states_of_america[-8])  # Ausgabe: Idaho

## =====================================================
##             Elemente in Listen modifizieren
## =====================================================

# Durch direkten Zugriff über den Index können Elemente in einer Liste auch verändert werden.
states_of_america[0] = "Telawere"
print(states_of_america)  # Ausgabe: Die Liste beginnt nun mit "Telawere" statt "Delaware"

## =====================================================
##             Hinzufügen von Elementen zu Listen
## =====================================================

# Mit der Methode append() wird ein einzelnes Element an das Ende einer Liste angehängt.
states_of_america.append("New State")
print(states_of_america)  # "New State" wird der Liste hinzugefügt

# Mit extend() können mehrere Elemente (als Liste) an die bestehende Liste angehängt werden:
states_of_america.extend(["New List State 1", "New List State 2", "New List State 3"])
print(states_of_america)

# Hinweis: Es ist nicht erforderlich, sich alle Methoden zu merken – in der Dokumentation findest du alle Möglichkeiten
# und kannst sie bei Bedarf nachschlagen.

## =====================================================
##             Demo: Banker Roulette
## =====================================================

# In dieser Demo wird ein Spiel simuliert, bei dem per Zufall bestimmt wird, wer die Rechnung zahlt.
# Alle Teilnehmer (Freunde) werden in einer Liste gespeichert und per Zufall wird ein Name ausgewählt.
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

## 1st Option
# Generiert einen zufälligen Index zwischen 0 und 4 und gibt den entsprechenden Namen aus:
get_integer_from_0_to_4 = random.randint(0, 4)
print(friends[get_integer_from_0_to_4])

## 2nd Option
# Mit choice() wird direkt ein zufälliges Element aus der Liste ausgewählt.
# Diese Methode demonstriert einen wichtigen Programmieransatz: Selbstständiges Recherchieren.
get_random_from_list = random.choice(friends)
print(get_random_from_list)

## =====================================================
##             Arbeiten mit Listenlängen und IndexErrors
## =====================================================

# Mit len() erhält man die Anzahl der Elemente in einer Liste (oder Zeichen in einem String).
# Dokumentation: https://docs.python.org/3/library/functions.html#len
print(len(states_of_america))  # Ausgabe: 50

## =====================================================
##             IndexError
## =====================================================

# Ein IndexError tritt auf, wenn versucht wird, auf ein Element außerhalb des gültigen Indexbereichs zuzugreifen.
print(states_of_america)

# Das letzte Element hat den Index 49:
print(states_of_america[49])  # Ausgabe: Hawaii

# Der Zugriff auf einen nicht vorhandenen Index (z.B. 50) würde zu einem IndexError führen.
# Zum Zugriff auf das letzte Element empfiehlt es sich, den negativen Index -1 zu verwenden:
print(states_of_america[-1])

## =====================================================
##             Verschachtelte Listen (Nested Lists)
## =====================================================

# Listen können auch andere Listen enthalten, was als verschachtelte (2D) Liste bezeichnet wird.
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]

fruits_and_veg = [fruits, veg]
print(fruits_and_veg)  # Ausgabe: [['Cherry', 'Apple', 'Pear'], ['Cucumber', 'Kale', 'Spinnach']]

# Alternativ kann die verschachtelte Struktur auch visuell so dargestellt werden:
# ["Cherry", "Apple", "Pear"]
# ["Cucumber", "Kale", "Spinnach"]

## =====================================================
##             Ausgabe verschachtelter Listen
## =====================================================

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen)       # Ausgabe: Gesamte verschachtelte Liste
print(dirty_dozen[0])    # Ausgabe: Liste der Fruits
print(dirty_dozen[1])    # Ausgabe: Liste der Vegetables
print(dirty_dozen[1][2]) # Ausgabe: Tomatoes (3. Element in der Vegetables-Liste)
print(dirty_dozen[1][3]) # Ausgabe: Celery (4. Element in der Vegetables-Liste)

