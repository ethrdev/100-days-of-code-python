## =====================================================
##             Demo: Rock, Paper, Scissors
## =====================================================
import random

# Definition der Spieloptionen als mehrzeilige Strings:
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Zusammenstellung der Optionen in einer Liste:
action_options = [rock, paper, scissors]

# Eingabeaufforderung: Der Spieler gibt seine Wahl ein (0 = Rock, 1 = Paper, 2 = Scissors).
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: \n"))
npc_choice = random.randint(0, 2)

print("Computer chose:")
print(action_options[npc_choice])

print("You chose:")
if player_choice >= 0 and player_choice <= 2:
    print(action_options[player_choice])

## =====================================================
##             Bestimmen des Spielergebnisses
## =====================================================
# Vergleich der Auswahl des Spielers und des Computers zur Ermittlung des Ergebnisses.
if player_choice >= 3 or player_choice < 0:
    print("You typed a invalid number. You lose!")
elif npc_choice == player_choice:
    print("Draw")
elif (npc_choice == 0 and player_choice == 2) or \
     (npc_choice == 1 and player_choice == 0) or \
     (npc_choice == 2 and player_choice == 1):
    print("You lose.")
else:
    print("You won!")

## =====================================================
##             Alternative: Ergebnisbestimmung mit modulo-Arithmetik
## =====================================================
# Eine alternative Methode zur Bestimmung des Ergebnisses mittels modulo-Arithmetik:
# result = (player_choice - npc_choice) % 3
#
# if result == 0:
#    print("Draw")
# elif result == 2:
#    print("You lose.")
# else:
#    print("You won!")
