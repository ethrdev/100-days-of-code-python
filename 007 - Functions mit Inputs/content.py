## =====================================================
##             Step 1: Erste Spielmechaniken
## =====================================================

# Ziel: Erstellung eines einfachen Hangman-Spiels zur Anwendung der bisher erlernten Python-Grundlagen.
# Hinweis: Das zugehörige Flowchart (siehe separate Datei) veranschaulicht den Programmablauf des Hangman-Projekts.

word_list = ["aardvark", "baboon", "camel"]

## TODO Wähle zufällig ein Wort aus der word_list und speichere es in der Variable chosen_word. Anschließend wird es ausgegeben.

import random
# Verwende random.choice() um ein zufälliges Wort aus der word_list auszuwählen
chosen_word = random.choice(word_list)
print(chosen_word)

## TODO Frage den Benutzer nach einem Buchstaben und speichere die Eingabe in der Variable guess.
# Die Eingabe wird in Kleinbuchstaben umgewandelt, um die Vergleichbarkeit zu gewährleisten.
guess = input("Guess a letter: ").lower()
print(guess)

## TODO Überprüfe, ob der vom Benutzer eingegebene Buchstabe (guess) im chosen_word enthalten ist.
# Falls ja, wird "Right" ausgegeben, andernfalls "Wrong".

# Iteriere über jeden Buchstaben im chosen_word:
for letter in chosen_word:
    # Ist der aktuelle Buchstabe gleich dem eingegebenen Buchstaben?
    if letter == guess:
        print("Right")
    # Andernfalls:
    else:
        print("Wrong")


## =====================================================
##             Step 2: Platzhalter und Anzeige
## =====================================================

import random
word_list = ["aardvark", "baboon", "camel"]

# Wähle ein zufälliges Wort aus der Liste und gebe es aus (nur zu Demonstrationszwecken)
chosen_word = random.choice(word_list)
print(chosen_word)

## TODO Erstelle einen "placeholder" String, der so viele Unterstriche (_) enthält wie Buchstaben im chosen_word.
# Dies dient als visuelle Hilfe, um die Anzahl der zu erratenden Buchstaben darzustellen.

# Initialisiere einen leeren String für den placeholder
placeholder = ""

# Option 1 (auskommentiert): Iteration basierend auf der Länge des Wortes
# word_length = len(chosen_word)
# for position in range(word_length):
#    placeholder += "_"

# Option 2 (bessere Methode): Iteriere über jeden Buchstaben im chosen_word und füge einen Unterstrich hinzu
for letter in chosen_word:
    placeholder += "_"

# Zeige den placeholder als Hinweis an
print(placeholder)

# Frage den Benutzer nach einem Buchstaben und wandle die Eingabe in Kleinbuchstaben um
guess = input("Guess a letter: ").lower()

## TODO Erstelle eine "display" Variable, die den geratenen Buchstaben an der richtigen Stelle zeigt und an den übrigen Stellen einen Unterstrich.
# Durchlaufe jeden Buchstaben in chosen_word:
# - Wenn der Buchstabe der Eingabe entspricht, füge ihn zu display hinzu.
# - Andernfalls füge einen Unterstrich hinzu.
# Beispiel: Bei chosen_word = "apple" und guess = "p" sollte display "_pp__" ergeben.

# Initialisiere einen leeren String für die Anzeige
display = ""

# Iteriere über jeden Buchstaben im chosen_word:
for letter in chosen_word:
    # Falls der Buchstabe dem geratenen Buchstaben entspricht:
    if letter == guess:
        display += letter
    # Andernfalls:
    else:
        display += "_"

# Ausgabe der aktuellen Anzeige
print(display)


## =====================================================
##             Step 3: Infinitive Loop und Fortschrittsanzeige
## =====================================================

import random
word_list = ["aardvark", "baboon", "camel"]

# Wähle ein zufälliges Wort aus der Liste
chosen_word = random.choice(word_list)
print(chosen_word)

# Erstelle einen placeholder String, der die Länge des chosen_word mit Unterstrichen darstellt
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

## TODO Implementiere ein while-Loop, die den Benutzer wiederholt nach Buchstaben fragen lässt.
# Der Loop soll erst enden, wenn der Benutzer alle Buchstaben des chosen_word erraten hat.
# Sobald display keine Unterstriche mehr enthält, wird der Benutzer als Gewinner benachrichtigt.

## TODO Aktualisiere den for-Loop, sodass frühere korrekte Eingaben beibehalten werden.
# Aktuell wird bei jeder neuen Eingabe der vorherige Fortschritt durch "_" ersetzt. Dies soll vermieden werden.

# Setze display zunächst auf den placeholder, der alle Buchstaben als Unterstriche zeigt
display = placeholder

# Erstelle eine Liste, um alle korrekt geratenen Buchstaben zu speichern.
# Diese Liste wird verwendet, um in der Anzeige (display) bereits erratene Buchstaben zu erhalten.
guessed_letters = []

# Definiere eine Variable game_over, die angibt, wann das Spiel beendet werden soll.
game_over = False

# Solange das Spiel nicht beendet ist:
while not game_over:
    # Setze display zurück, um den aktuellen Fortschritt neu aufzubauen
    display = ""
    # Frage den Benutzer nach einem Buchstaben und wandle die Eingabe in Kleinbuchstaben um
    guess = input("Guess a letter: ").lower()
    # Iteriere über jeden Buchstaben im chosen_word:
    for letter in chosen_word:
        # Falls der Buchstabe dem geratenen Buchstaben entspricht:
        if letter == guess:
            # Füge den Buchstaben zur Liste der erratenen Buchstaben hinzu
            guessed_letters.append(letter)
            # Zeige den Buchstaben in der Anzeige an
            display += letter
        # Falls der Buchstabe bereits in guessed_letters enthalten ist:
        elif letter in guessed_letters:
            # Zeige den bereits erratenen Buchstaben in der Anzeige an
            display += letter
        # Andernfalls:
        else:
            # Zeige einen Unterstrich an
            display += "_"

    # Ausgabe des aktuellen Fortschritts
    print(display)

    # Wenn keine Unterstriche mehr in der Anzeige vorhanden sind, wurde das Wort vollständig erraten
    if "_" not in display:
        game_over = True
        print("You have won!")