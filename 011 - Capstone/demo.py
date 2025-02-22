#### Capstone Projekt: Blackjack
### First try by ethr

### Functionality
# Chose your difficulty
# Normal 😎: Use all Hints below to complete the project.
# Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Expert 🤯: Only use Hint 1 to complete the project.

# I will try it on expert level

## Our Blackjack Game House Rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.

## TODO If score >= 21 Ass == 1
## TODO If score == 12 print "Black Jack!" 
## TODO Refactoring
## TODO Application muss verkapselt werden, sodass Logo immer fixiert


import random
from art import logo

# Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

def blackjack():
    
    print(logo)
    # Ask user if he wants to play a game of black jack
    input("Do you want to play a game of Black Jack? Press 'y' for eys or 'n' for no. ")

    def get_player_card():
        get_random_card = random.randint(1, 13)
        #print(get_random_card)
        card = int(cards[get_random_card -1])
        #print(card)
        player_cards.append(card)
        
    ## List of cards    
    player_cards = []

    get_player_card()
    get_player_card()

    player_score = sum(player_cards)

    dealer_cards = []
    def get_dealer_card():
        get_random_card = random.randint(1, 13)
        card = int(cards[get_random_card -1])
        dealer_cards.append(card)

    get_dealer_card()

    # Your cards: [6, 10], current score: 16
    print(f"You cards are {player_cards}, so your current score is {player_score}")
    print(f"Dealer's first hand is {dealer_cards[0]}")

    add_card = input("Type 'y' to get another card or type 'n' to pass: ") 

    while add_card == "y":
        print("\n")
        get_player_card()
        player_score = sum(player_cards)
        
        print(f"You cards are {player_cards}, so your current score is {player_score}")
        print(f"Dealer's first hand is {dealer_cards[0]}")
        
        if player_score > 21:
            print(f"You cards are {player_cards}, so your current score is {player_score}")
            print(f"Dealer's first hand is {dealer_cards[0]}")
            print("You went over. You lose 😭")
            blackjack()
        
        add_card = input("Type 'y' to get another card or type 'n' to pass: ") 
            
    get_dealer_card()
    dealer_score = sum(dealer_cards)
    
    dealers_turn = True
    
    while dealers_turn:
        while dealer_score < 17:
            get_dealer_card()
            dealer_score = sum(dealer_cards)
            
        print(f"You final hand is {player_cards} with a final score of {player_score}.")
        print(f"Dealer's final hand is {dealer_cards} with a final score of {dealer_score}.")
        
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
    
    


        
blackjack()       

    
