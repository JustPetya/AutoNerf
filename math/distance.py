# Feste Werte
__BRENNWEITE__ = 2.1
__BREITE_ZWISCHEN_KAMERA__= 12


def berechne_tiefe(x1, x2):
        hoehe = (__BRENNWEITE__ * __BRENNWEITE__) / (x1 - x2)
        return hoehe




