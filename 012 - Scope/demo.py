#### Project: Number Guessing Game
### First try by ethR


import random
from art import logo

print(logo)

#
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


# Diese Funktion überprüft die Benutzereingabe (guessed_num) gegen die zu erratende Zahl (num_to_guess)
# und gibt die verbleibenden Versuche (guesses_left) nach dem Vergleich zurück.
def guess_result(guessed_num, num_to_guess, guesses_left):
    # Überprüfe, ob die geratene Zahl kleiner als die gesuchte Zahl ist.
    if guessed_num < num_to_guess:
        print("Too Low.")
        print("Guess again.")
        # Verringere die verbleibenden Versuche um 1 und gebe den neuen Wert zurück.
        return guesses_left - 1
    # Überprüfe, ob die geratene Zahl größer als die gesuchte Zahl ist.
    elif guessed_num > num_to_guess:
        print("Too high.")
        print("Guess again.")
        # Verringere die verbleibenden Versuche um 1 und gebe den neuen Wert zurück.
        return guesses_left - 1
    # Falls die geratene Zahl der gesuchten Zahl entspricht.
    else:
        print(f"You got it! The answer was {num_to_guess}.")
        # Setze die Versuche auf 0, um das Spiel zu beenden.
        return 0


# Diese Funktion fragt den Spieler, ob er ein neues Spiel starten möchte.
def continuation():
    new_game = input("Do you want to play again? Type 'yes' or 'no': ")
    # Falls der Spieler "yes" eingibt, wird die Hauptspielfunktion erneut aufgerufen.
    if "yes" in new_game:
        number_guesser()
    # Falls der Spieler "no" eingibt, wird das Spiel beendet.
    if "no" in new_game:
        print("Goodbye!")


# Diese Funktion enthält die gesamte Logik des Zahlratespiels.
def number_guesser():
    # Fordere den Spieler auf, einen Schwierigkeitsgrad auszuwählen und wandle die Eingabe in Kleinbuchstaben um.
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    # Setze die Anzahl der Versuche basierend auf der gewählten Schwierigkeit.
    if "hard" in difficulty:
        guesses_left = 5
    elif "easy" in difficulty:
        guesses_left = 10
    else:
        print("Invalid difficulty. Please enter 'easy' or 'hard'.")
        return  # oder erneut number_guesser() aufrufen

    # Generiere eine zufällige Zahl zwischen 1 und 100, die der Spieler erraten muss.
    num_to_guess = random.randint(1, 100)

    # Solange der Spieler noch Versuche übrig hat, wiederhole den Ratevorgang.
    while guesses_left > 0:
        # Fordere den Spieler auf, eine Zahl zu raten. Die Eingabe wird in einen Integer umgewandelt.
        print(f"You have {guesses_left} attempts remaining to guess the number.")
        guessed_num = int(input("Guess a number between 1 and 100: "))
        # Überprüfe die geratene Zahl und aktualisiere die verbleibenden Versuche.
        guesses_left = guess_result(guessed_num, num_to_guess, guesses_left)
    # Falls alle Versuche aufgebraucht sind und die Zahl nicht korrekt erraten wurde,
    # informiere den Spieler über das korrekte Ergebnis.
    if guesses_left == 0 and guessed_num != num_to_guess:
        print(f"Sorry. But you lost. Number to guess was {num_to_guess}.")
    # Frage den Spieler, ob er ein neues Spiel starten möchte.
    continuation()


# Starte das Spiel, indem die Hauptspielfunktion aufgerufen wird.
number_guesser()
