## =====================================================
##             Demo: Escaping the Maze
## =====================================================

# Dieses Beispiel (auskommentiert) zeigt, wie man mit bedingten Anweisungen und Loops
# ein Labyrinth verlässt. Die Logik basiert darauf, dass die Figur je nach Umgebung
# (Wand links/rechts, freier Weg) unterschiedlich reagiert.
#
# Interaktive Demo:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# while not at_goal():
#     if not wall_on_right():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
