#berechnung wenn die kameras parralel sind, nicht general stereo cameras

# feste werte
brennweite = 25
breite = 5

# positinen von timo
x1 = 5
x2 = 4

y1 = 10
y2 = 10


pos1 = x1 * y1 #rechter pointer
pos2 = x2 * y2 #linker pointer

höhe = (brennweite * breite) / pos1 - pos2

print("Höhe:", höhe)

print("Hallo")
