## =====================================================
##             Verschachtelte Listen und Dictionaries
## =====================================================

# In diesem Abschnitt lernst du, wie du verschiedene Datentypen kombinieren kannst,
# um flexible und komplexe Datenstrukturen in Python zu erstellen.
# Dabei werden Listen und Dictionaries miteinander verschachtelt,
# um mehrere Informationen unter einem einzigen Schlüssel zu speichern.

## =====================================================
##             Liste in einem Dictionary verschachteln
## =====================================================

# Anstatt einem Schlüssel einen einfachen String-Wert zuzuweisen, kannst du diesem
# Schlüssel auch eine Liste zuordnen. Dies ermöglicht es, mehrere Werte unter einem
# Schlüssel zu speichern und so die Datenstruktur flexibler zu gestalten.
'''
my_dictionary = {
    key1: [List],
    key2: Value,
    key3: {Dictionary},
}
'''
# Vorteil: Mehrere Informationen lassen sich unter einem einzigen Schlüssel organisieren.

# Überlege, wie du "Lille" aus der verschachtelten Liste travel_log ausgeben kannst.
travel_log = {
    # Hier wird der Schlüssel "France" mit einer Liste von Städten verknüpft.
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Um "Lille" auszugeben, greifst du wie folgt vor:
print(travel_log["France"][1])
# Erklärung:
# - travel_log["France"] liefert die Liste ["Paris", "Lille", "Dijon"].
# - Der Index [1] wählt das zweite Element "Lille" aus.

## =====================================================
##             Listen in anderen Listen verschachteln
## =====================================================

# In Python können Listen auch innerhalb anderer Listen verschachtelt werden.
# So lassen sich mehrdimensionale Datenstrukturen erstellen.

nested_list = ["A", "B", ["C", "D"]]

# Um auf das Element "D" zuzugreifen, wendest du eine doppelte Indizierung an:
print(nested_list[2][1])

# Erklärung:
# - nested_list[2] gibt die verschachtelte Liste ["C", "D"] zurück.
# - nested_list[2][1] wählt das zweite Element "D" aus dieser Liste aus.

## =====================================================
##             Dictionary in einem Dictionary verschachteln
## =====================================================

# Du kannst auch ein Dictionary innerhalb eines anderen Dictionaries verschachteln,
# um strukturierte und hierarchische Daten abzubilden.
'''
my_dictionary = {
    key1: Value,
    key2: {Key: Value, Key: Value},
}
'''

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}

# Um "Stuttgart" auszugeben, gehst du folgendermaßen vor:
print(travel_log["Germany"]["cities_visited"][2])

# Erklärung:
# - travel_log["Germany"] liefert das Dictionary {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}.
# - travel_log["Germany"]["cities_visited"] liefert die Liste ["Berlin", "Hamburg", "Stuttgart"].
# - Der Index [2] wählt den dritten Eintrag "Stuttgart" aus.

## =====================================================
##             Quiz: Verständnisfragen zu Listen und Dictionaries
## =====================================================

# Frage 1:
# Welche Codezeile ändert starting_dictionary so, dass es final_dictionary entspricht?

starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary["c"] = 7
final_dictionary = starting_dictionary

# Erklärung:
# - Mit starting_dictionary["c"] = 7 wird dem Dictionary ein neuer Schlüssel "c" mit dem Wert 7 hinzugefügt.
# - Anschließend wird final_dictionary auf starting_dictionary gesetzt, sodass beide Dictionaries identisch sind.

# Frage 2:
# Welche Codezeile führt zu einem Fehler (KeyError), da versucht wird, auf einen nicht existierenden Schlüssel zuzugreifen?

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

'''
dict["c"] = [1, 2, 3]
'''

'''
for key in dict:    
    dict[key] += 1 
'''

'''
dict[1] = 4 
'''

'''
print(dict[1]) 
'''

# Erklärung:
# - dict[1] versucht, den Schlüssel 1 abzufragen, der nicht existiert. Dies führt zu einem KeyError.
# - Beachte: Bei Listen entspricht [1] dem Index, bei Dictionaries muss der Schlüssel exakt übereinstimmen.

# Frage 3:
# Welche Codezeile gibt "Steak" aus?

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])

# Erklärung:
# - order["main"] liefert das Dictionary {1: ["Burger", "Fries"], 2: ["Steak"]}.
# - order["main"][2] gibt die Liste ["Steak"] zurück.
# - Der Index [0] wählt das erste Element "Steak" aus dieser Liste aus.