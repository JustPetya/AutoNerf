# Feste Werte
__BRENNWEITE__ = 2.1
__BREITE_ZWISCHEN_KAMERA__ = 12
__bildbreite_in_CM__ = 
__horizontale_pixel__ =  720 #max res 1280* 720
__pixeldichte__ = __horizontale_pixel__ * 2.54 / bildbreite_in_CM



def berechne_tiefe(x1, x2):
    hoehe = (__BRENNWEITE__ * __BREITE_ZWISCHEN_KAMERA__) /__pixeldichte__ * (x1 - x2)
    return hoehe
