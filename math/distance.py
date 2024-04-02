# Feste Werte
__BRENNWEITE__ = 2.1
__BREITE_ZWISCHEN_KAMERA__ = 12
__pixeldichte__


def berechne_tiefe(x1, x2, horizontale_pixel,bildbreite_in_CM):
    __pixeldichte__ = horizontale_pixel * 2.54/ bildbreite_in_CM 
    hoehe = (__BRENNWEITE__ * __BREITE_ZWISCHEN_KAMERA__) /__pixeldichte__ * (x1 - x2)
    return hoehe
