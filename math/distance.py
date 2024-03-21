import random

# fete werte
brennweite = 25
breite = 24

# positinen von timo
rechter_pointer_x = -12
rechter_pointer_y = 5

linker_pointer_x = 12
linker_pointer_y = 6


höhe = (brennweite * breite) / ((rechter_pointer_x - linker_pointer_x) * (rechter_pointer_y - linker_pointer_y))

print("Höhe:", höhe)

print("Hallo")
