# --- Tagesprojekt: Band Name Generator ---
# Das Programm funktioniert folgendermaßen:
# 1. Es begrüßt den Benutzer.
# 2. Es fragt nach der Stadt, in der der Benutzer aufgewachsen ist.
# 3. Es fragt nach dem Namen des Haustiers.
# 4. Anschließend wird ein möglicher Bandname erstellt, indem die Stadt und der Haustiername kombiniert werden.
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be" + " " + city + " " + pet)