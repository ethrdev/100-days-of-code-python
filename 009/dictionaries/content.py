## =====================================================
##             Einführung in Dictionaries
## =====================================================
# Ein Dictionary in Python funktioniert ähnlich wie ein Wörterbuch im echten Leben.
# Es ist eine data structure, die es ermöglicht, einen key mit einem value zu verknüpfen.
# Dadurch können zusammengehörige Daten als Paar gespeichert werden.

# =====================================================
#             Erzeugung eines Dictionaries
# =====================================================
# So erstellt man ein Dictionary in Python:
'''
{Key: Value}
'''

# Ein Beispiel-Dictionary
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}

# =====================================================
#             Zugriff auf Dictionary-Elemente
# =====================================================

# In einem Dictionary werden die Elemente durch ihren key identifiziert.
# So greifst Du auf ein Element zu:
# Syntax: dictionary_name[key]
print(colours["pear"])  # Gibt "green" aus

# Der key wird verwendet, um den zugehörigen value abzurufen.
# Achtung: Existiert der angefragte key nicht, führt dies zu einem KeyError.
# Verwende stets den korrekten Datentyp, z.B. "pear" (als String) statt pear (als Variable).

# =====================================================
#             Erzeugung eines leeren Dictionaries
# =====================================================

# So erzeugst Du ein leeres Dictionary:
# Syntax: dictionary_name = {}
my_empty_dictionary = {}

# =====================================================
#             Hinzufügen und Ändern von Elementen
# =====================================================

# So fügst Du einem existierenden Dictionary ein neues Element hinzu:
# Syntax: dictionary_name[key] = value
colours["peach"] = "pink"

# Ebenso änderst Du einen bestehenden value:
# Syntax: dictionary_name[key] = new_value
colours["apple"] = "green"
# Hier wird das Element mit dem key "apple" gesucht und dessen value auf "green" geändert.

# =====================================================
#             Iteration durch ein Dictionary
# =====================================================

# So iterierst Du durch ein Dictionary und gibst alle keys aus:
# Syntax: for key in dictionary_name:
for key in colours:
    print(key)  # Gibt nacheinander "apple", "pear", "banana", "peach" aus
# Die Schleife durchläuft das Dictionary und gibt jeden key aus.

# Möchtest Du die values ausgeben, kannst Du den key verwenden:
# Syntax: dictionary_name[key]
for key in colours:
    print(colours[key])  # Gibt nacheinander "red", "green", "yellow", "pink" aus

# Um sowohl key als auch value auszugeben, verwende die Methode items():
# Syntax: for key, value in dictionary_name.items():
for key, value in colours.items():
    print(key, value)  # Gibt "apple red", "pear green", "banana yellow", "peach pink" aus

# =====================================================
#             Alternative Iterationsmethode (Kommentiert)
# =====================================================

# Dieser Codeblock zeigt eine alternative Methode zur Ausgabe der values.
'''
for key in colours:
    print(colours[key])
'''

# =====================================================
#             Löschen eines Dictionaries
# =====================================================

# So setzt Du ein Dictionary zurück:
# Syntax: dictionary_name = {}
colours = {}

# =====================================================
#             Praxisbeispiel: Programming Dictionary
# =====================================================

## Try it out:
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
# Der letzte Eintrag in einem Dictionary benötigt kein Komma am Ende.
}

print(programming_dictionary["Bug"])  # Gibt den value zu "Bug" aus

# Hinzufügen eines neuen Eintrags
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Ändern eines existierenden Eintrags
programming_dictionary["Function"] = "This entry was edited"
print(programming_dictionary)

# Löschen des gesamten Dictionaries
programming_dictionary = {}
print(programming_dictionary)