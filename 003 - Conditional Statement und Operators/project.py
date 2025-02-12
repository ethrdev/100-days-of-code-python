## =====================================================
##             Projekt: Treasure Island
## =====================================================
## Dieses textbasierte Abenteuer demonstriert, wie if/else-Strukturen eingesetzt werden,
## um dem Nutzer verschiedene Entscheidungswege und Spielverläufe zu ermöglichen.
## Mithilfe von mehrzeiligen Strings wird hier ASCII-Art verwendet,
## und die Methode .lower() sorgt dafür, dass Eingaben in Kleinbuchstaben umgewandelt werden.

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome, intrepid explorer, to the fabled Treasure Island!")
print("Your quest: to unearth the hidden treasure of legends.")

# Nutze den Backslash (\), um Sonderzeichen (z. B. Ausrufezeichen) innerhalb von Strings zu maskieren.
# Verwende .lower(), um die Benutzereingaben in Kleinbuchstaben zu konvertieren.
direction_choice = input("At a mysterious crossroad, which path calls to you... \"left\" or \"right?\" ").lower()
if direction_choice == "left":
    river_choice = input("Before you lies a roaring river of uncertainty. Will you \"swim\" through its tumultuous currents or \"wait\" for a safer passage? ").lower()
    if river_choice == "swim":
        door_choice = input("Emerging from the river, you stand before an ancient castle with three enchanted doors. \n"
                           "Which door beckons you: \"Red\", \"Blue\", or \"Yellow\"? ").lower()
        if door_choice == "red":
            print("A raging inferno engulfs you! The flames consume your hope. Game over.")
        elif door_choice == "blue":
            print("Monstrous creatures leap from the shadows and devour you. Your quest ends here. Game Over.")
        elif door_choice == "yellow":
            print("Huzzah! You have uncovered the treasure and earned eternal glory!")
        else:
            print("An error in your choice leads you astray... The fates have condemned you. Game Over.")
    else:
        print("A swarm of vicious trout ambushes you, ending your journey abruptly. Game Over.")
else:
    print("You tread the perilous right path and fall into an endless abyss. Game Over.")