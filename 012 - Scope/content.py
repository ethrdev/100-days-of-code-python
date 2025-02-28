#### Namespaces and Scope
### Global vs. Local Scope

## Local Scope
# Variables (or functions) declared inside functions have local scope (also called function scope). 
# They are only seen by other code within the same block of code.

# e.g.
'''
def my_function():
    my_local_var = 2
    
# This will cause a NameErrorr
print(my_local_var) 
'''

## Global Scope
# Variables or functions declared at the top level (unindented) of a code file have global scope. 
# It is accessible anywhere in the code file.

# e.g.
'''
my_global_var = 3

def my_function():
    # This works no problems
    print(my_global_var)
'''

## Beispiel 1

enemies = 1

# Diese Funktion hat keinen Einfluss auf die Variable enemies
def increase_enemies():
    # Der Output hier ist 2, weil die Variable enemies innerhalb der Funktion neu definiert wird
    enemies = 2
    print(f"enemies inside function: {enemies}") # 2

# Der Output hier ist 1, weil die Variable enemies außerhalb der Funktion nicht verändert wird
increase_enemies()
print(f"enemies outside function: {enemies}") # 1

# Der Output hier ist 2, weil die Funktion increase_enemies() den Wert der Variable enemies zurückgibt
print(increase_enemies()) # 2

## Beispiel 2

# Bevor wir eine Funktion definieren, sollen wir sicherstellen, dass die Variable, die wir ändern möchten, global ist.
player_health = 10

def game():
    def drink_potion():
        # Die Variable potion_strength hat Local Scope und kann nur innerhalb der Funktion drink_potion() verwendet werden
        potion_strength = 2
        print(player_health) # 10
    drink_potion()

print(player_health) # 10

### Block Scope in Python
# Python is a bit different from other programming languages in that it does not have block scope.
# This means that variables created nested in other blocks of code e.g. for loops, if statements, while loops etc. don't get local scope. 
# They are given function scope if they are within a function or global scope if they are not.

# e.g.

# Accessible anywhere
my_global_var = 1

def my_function():
    # Only accessible within my_function()
    my_local_var = 2
    
for _ in range(10):
    # Accessible anywhere
    my_block_var = 3

## Beispiel

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]


if game_level < 5:
    new_enemy = enemies[0]

# Der Output ist Skeleton, da die Variable new_enemy innerhalb des if-Blocks definiert wurde.
print(new_enemy) # Skeleton

def create_enemy():
    # Wir sollten die Variable new_enemy innerhalb der Funktion definieren, da sie nicht vergeben ist, falls game_level >= 5 ist.
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

# Der Output ist NameError: name 'new_enemy' is not defined, da die Variable new_enemy innerhalb der Funktion create_enemy() definiert 
# wurde und somit nicht außerhalb der Funktion zugänglich ist.
print(new_enemy) # NameError: name 'new_enemy' is not defined


### Modifying a global scope mit Global Vars


enemies = 1

def increase_enemies():
    # Um die globale Variable enemies zu modifizieren, müssen wir das Schlüsselwort global verwenden.
    # Diese Variante sollte jedoch vermieden werden, da sie zu unübersichtlichem Code führen kann.
    '''
    global enemies
    enemies += 1
    '''
    # Stattdessen sollten wir Returns verwenden, um die Variable zu modifizieren.
    # Nun kann die globale Variable enemies modifiziert werden.
    print(f"enemies inside function: {enemies}") # Zombie
    return enemies + 1


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}") # Skeleton


### Global Constants
# You can define global constants in your code file for easy access. 
# Their job is meant to be "set and forget" so you can use their values but never need to mofy them.

## Naming Convention
# Global constants are normally declared in ALL_CAPS with a underscore in between.
# e.g.

PI = 3.14159
GOOGLE_URL = "https://www.google.com"



### Challenge: Prime Number Checker
## Prime numbers are numbers that can only be cleanly divided by themselves and 1. Wikipedia  

# You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.  
# It should return True or False.

# e.g.
# 7 is a primer number because it is only divisible by 1 and itself.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# NOTE: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1. 



def is_prime(num):
    if num < 2:
        return False
    
    # number**0.5 berechnet die Quadratwurzel von number.
    # Der Grund, nur bis zur Quadratwurzel zu überprüfen, ist, dass ein möglicher Teiler jenseits dieser Grenze zwangsläufig einen zugehörigen 
    # Teiler unterhalb der Quadratwurzel hätte. Mit anderen Worten:

    # Wenn eine Zahl n einen Teiler d besitzt, dann ist n = d * k.
    # Entweder ist d <= sqrt(n) oder k <= sqrt(n) (einer von beiden ist immer kleiner oder gleich der Wurzel).

    # Deshalb reicht es, nur bis zur Quadratwurzel (sqrt(n)) zu suchen, um alle möglichen „kleinen“ Teiler zu finden. Wird dort keiner gefunden, existieren auch keine „großen“ Teiler.
    # int(number**0.5) wandelt die gefundene Quadratwurzel in eine ganze Zahl um. 
    # Das + 1 sorgt dafür, dass im Falle einer gerundeten Wurzel (z. B. bei Quadratzahlen) der Bereich korrekt bis zum letzten benötigten Wert geht und bei 11.9 im 
    # Fall einer Fließkommadarstellung nicht versehentlich nur bis 11 überprüft wird.
    upper_limit = int(num**0.5) + 1

    for divisor in range(2, upper_limit):
        if num % divisor == 0:
            return False
    
    return True

print(is_prime(1))
print(is_prime(13))
print(is_prime(73))
print(is_prime(75))