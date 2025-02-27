## =====================================================
##             Capstone Projekt: Blackjack
## =====================================================
# Dieses Skript implementiert ein einfaches Blackjack-Spiel als Capstone Projekt.
# Das Spiel basiert auf einem unendlichen Kartendeck ohne Joker. 
# Besonderheiten: Jack, Queen und King zählen als 10; Ace (11) kann später ggf. als 1 interpretiert werden.
# Verschiedene Schwierigkeitsgrade sind in den Kommentaren als Hinweise angegeben.

import random
from art import logo

## =====================================================
##             Kartendeck
## =====================================================

# Definieren des Kartendecks als Liste.
# Die Zahl 11 repräsentiert das Ace, während 10 mehrfach vorkommt, um die Werte von 10, Jack, Queen und King abzubilden.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

## =====================================================
##             Funktion: blackjack()
## =====================================================

# Diese Funktion startet das Spiel und steuert den gesamten Ablauf.
def blackjack():
    
    # Ausgabe des Logos (grafische Darstellung des Spiels)
    print(logo)
    
    # Fragt den Benutzer, ob er ein Spiel starten möchte.
    input("Do you want to play a game of Black Jack? Press 'y' for eys or 'n' for no. ")

    ## =====================================================
    ##             Funktion: get_player_card()
    ## =====================================================
    
    # Diese innere Funktion zieht eine zufällige Karte für den Spieler.
    def get_player_card():
        # Ziehe eine zufällige Zahl zwischen 1 und 13, um einen Index für das Kartendeck zu erhalten.
        get_random_card = random.randint(1, 13)
        # Wähle die entsprechende Karte aus dem Deck aus.
        card = int(cards[get_random_card - 1])
        # Füge die gezogene Karte zur Liste der Spieler-Karten hinzu.
        player_cards.append(card)
        
    ## =====================================================
    ##             Initialisierung Spielerhand
    ## =====================================================
    
    # Erstellen einer Liste zur Speicherung der Karten des Spielers.
    player_cards = []

    # Der Spieler zieht initial zwei Karten.
    get_player_card()
    get_player_card()

    # Berechne den aktuellen Punktestand des Spielers.
    player_score = sum(player_cards)

    ## =====================================================
    ##             Initialisierung Dealerhand
    ## =====================================================
    
    # Erstellen einer Liste zur Speicherung der Karten des Dealers.
    dealer_cards = []
    # Diese Funktion zieht eine zufällige Karte für den Dealer.
    def get_dealer_card():
        get_random_card = random.randint(1, 13)
        card = int(cards[get_random_card - 1])
        dealer_cards.append(card)

    # Der Dealer zieht initial eine Karte.
    get_dealer_card()

    ## =====================================================
    ##             Anzeige der ersten Karten
    ## =====================================================
    
    # Zeige die Karten des Spielers und die erste Karte des Dealers an.
    print(f"You cards are {player_cards}, so your current score is {player_score}")
    print(f"Dealer's first hand is {dealer_cards[0]}")

    # Frage den Spieler, ob er eine weitere Karte ziehen möchte.
    add_card = input("Type 'y' to get another card or type 'n' to pass: ") 

    ## =====================================================
    ##             Spieler-Zug (Hit/Stand)
    ## =====================================================
    
    # Solange der Spieler 'y' eingibt, wird eine weitere Karte gezogen.
    while add_card == "y":
        print("\n")
        get_player_card()
        player_score = sum(player_cards)
        
        # Aktualisierte Anzeige der Spieler-Karten und des Punktestands.
        print(f"You cards are {player_cards}, so your current score is {player_score}")
        print(f"Dealer's first hand is {dealer_cards[0]}")
        
        # Überprüfe, ob der Spieler mehr als 21 Punkte hat (Bust).
        if player_score > 21:
            print(f"You cards are {player_cards}, so your current score is {player_score}")
            print(f"Dealer's first hand is {dealer_cards[0]}")
            print("You went over. You lose 😭")
            # Bei Überschreitung des Punktestandes wird das Spiel neu gestartet.
            blackjack()
        
        # Erneute Abfrage, ob der Spieler eine weitere Karte ziehen möchte.
        add_card = input("Type 'y' to get another card or type 'n' to pass: ") 
            
    ## =====================================================
    ##             Dealer-Zug
    ## =====================================================
    
    # Nachdem der Spieler fertig ist, zieht der Dealer eine weitere Karte.
    get_dealer_card()
    dealer_score = sum(dealer_cards)
    
    dealers_turn = True
    
    # Der Dealer zieht solange Karten, bis sein Punktestand mindestens 17 erreicht.
    while dealers_turn:
        while dealer_score < 17:
            get_dealer_card()
            dealer_score = sum(dealer_cards)
            
        # Anzeige der finalen Hände und Punktestände von Spieler und Dealer.
        print(f"You final hand is {player_cards} with a final score of {player_score}.")
        print(f"Dealer's final hand is {dealer_cards} with a final score of {dealer_score}.")
        
        # Vergleich der Punktestände zur Ermittlung des Gewinners.
        if dealer_score > 21:
            print("Dealer busted")
            dealers_turn = False
        elif dealer_score == player_score:
            print("Draw")
            dealers_turn = False
        elif dealer_score > player_score:
            print("Dealer wins")
            dealers_turn = False
        elif dealer_score < player_score:
            print("You win")
            dealers_turn = False
        else:
            print("Unknown Error")  
            dealers_turn = False
    
# Spielstart
blackjack()       

## =====================================================
##             Hinweise und Optimierung
## =====================================================
'''
- Statt separate, unabhängige Funktionen zu nutzen, sind einige Hilfsfunktionen (z. B. get_player_card() und get_dealer_card()) als innere Funktionen 
innerhalb von blackjack() definiert. Das kann die Wiederverwendbarkeit und Testbarkeit einschränken.
- Es wird nicht überprüft, ob der Spieler bereits gewonnen hat, bevor der Dealer seinen Zug macht.
- Bei einem Bust wird blackjack() rekursiv aufgerufen, um das Spiel neu zu starten. Dies kann bei wiederholtem Busten zu einem wachsenden Rekursionsstapel 
führen und ist aus Sicht der Robustheit eher problematisch.
- Statt random.choice(cards) wird random.randint(1, 13) verwendet, um einen Index im Karten-Deck zu bestimmen. Das ist weniger elegant und birgt das Risiko, 
falsche Indizes zu erzeugen, wenn sich das Deck ändert.
'''