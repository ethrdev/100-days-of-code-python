## =====================================================
##                        Hangman
## =====================================================

import random

## =====================================================
##             Modul-Import und Datenvorbereitung
## =====================================================

# Importiere die 'word_list' aus der Datei hangman_words.py, die alle m�glichen W�rter enth�lt.
from hangman_words import word_list
# Importiere 'stages' (Grafiken) und 'logo' (Spiel-Logo) aus der Datei hangman_art.py.
from hangman_art import stages, logo

lives = 6  # Setzt die Anzahl der verf�gbaren lives auf 6.

## =====================================================
##  Spielstart: Anzeige des Logos und Auswahl des Wortes
## =====================================================

# Zeige das Logo des Spiels an.
print(logo)

# Wähle zufällig ein Wort aus der word_list aus.
chosen_word = random.choice(word_list)
print(chosen_word)  # Zeigt das gewählte Wort an.

# Erzeuge einen Placeholder für das zu erratende Wort, bestehend aus Unterstrichen.
placeholder = ""

# Erhalte die Länge des gewählten Wortes und füge für jeden Buchstaben einen Unterstrich hinzu.
word_length = len(chosen_word)

# Iteriere über jeden Buchstaben im gewählten Wort und füge einen Unterstrich hinzu.
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False  # Flag, das angibt, ob das Spiel beendet ist.
correct_letters = []  # Liste zur Speicherung bereits korrekt erratener Buchstaben.

## =====================================================
##             Hauptspielschleife
## =====================================================

while not game_over:

    ## =====================================================
    ##             Benutzerinformation und Eingabe
    ## =====================================================
    
    # Informiere den Spieler über die verbleibenden lives.
    print(f"**** {lives} lives left ****")
    # Fordere den Spieler auf, einen Buchstaben zu raten und konvertiere die Eingabe in Kleinbuchstaben.
    guess = input("Guess a letter: ").lower()

    ## =====================================================
    ##             Überprüfung auf wiederholte Eingabe
    ## =====================================================
    
    # Prüfe, ob der eingegebene Buchstabe bereits als korrekt erraten gespeichert wurde.
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        continue  # Überspringt den Rest des aktuellen Schleifendurchlaufs, wenn der Buchstabe bereits geraten wurde.

    display = ""  # Initialisiere die Anzeige für den aktuellen Stand des zu erratenden Wortes.

    ## =====================================================
    ##             Aktualisierung der Wortanzeige
    ## =====================================================
    
    # Iteriere über jeden Buchstaben im gewählten Wort.
    for letter in chosen_word:
        if letter == guess:
            display += letter  # Ersetze den Placeholder durch den korrekten Buchstaben.
            correct_letters.append(guess)  # Füge den korrekten Buchstaben der Liste hinzu.
        elif letter in correct_letters:
            display += letter  # Zeige bereits erratene Buchstaben.
        else:
            display += "_"  # Behalte den Placeholder für nicht erratene Buchstaben bei.

    print("Word to guess: " + display)

    ## =====================================================
    ##             Überprüfung der Richtigkeit der Eingabe
    ## =====================================================
    
    # Falls der geratene Buchstabe nicht im gewählten Wort enthalten ist:
    if guess not in chosen_word:
        lives -= 1  # Ziehe ein life ab.
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        
        # Falls keine lives mehr übrig sind, wird das Spiel beendet.
        if lives == 0:
            game_over = True

            ## =====================================================
            ##             Spielende: Niederlage
            ## =====================================================
            
            # Informiere den Spieler über das Spielende und zeige das korrekte Wort an.
            print(f"***********************YOU LOSE**********************\n"
                  f"Word to guess was: {chosen_word}")

    ## =====================================================
    ##             Gewinnbedingung
    ## =====================================================
    
    # Falls keine Placeholder mehr in der Anzeige vorhanden sind, hat der Spieler das Wort vollständig erraten.
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    ## =====================================================
    ##             Anzeige der Hangman-Stages
    ## =====================================================
    # Zeige die aktuelle grafische Darstellung (Stage) des Hangman-Spiels an.
    print(stages[lives])
