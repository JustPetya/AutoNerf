class Distance:
    @staticmethod


    def berechne_hoehe_3d(brennweite, breite, x1, x2, y1, y2):
        pos1 = x1 * y1  # rechter Pointer
        pos2 = x2 * y2  # linker Pointer
        hoehe = (brennweite * breite) / (pos1 - pos2)
        return hoehe

    def berechne_hoehe_2d(brennweite, breite, x1, x2):
        hoehe = (brennweite * breite) / (x1 - x2)
        return hoehe

def start():
    # Feste Werte
    brennweite = 25
    breite = 5

    # Positionen von Timo
    x1 = 5
    x2 = 4
    y1 = 10
    y2 = 10

    hoehe_3d = Distance.berechne_hoehe_3d(brennweite, breite, x1, x2, y1, y2)
    
    
    #2d werte für nikas
    hoehe_2d = Distance.berechne_hoehe_2d(brennweite, breite, x1, x2)

    print("Höhe 3d:", hoehe_3d)
    print("Höhe 2d:", hoehe_2d)

if __name__ == "__main__":
    start()
