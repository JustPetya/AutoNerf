# Feste Werte
__BRENNWEITE__ = 2.1
__BREITE_ZWISCHEN_KAMERA__ = 6 #muss timo noch sagen
__bildbreite_in_CM__ = 45.2 #muss timo mir sagen # 45,2 wäre wenn 1280*720pixel & 72 dpi
__horizontale_pixel__ =  720 #max res 1280* 720
__pixeldichte__ = __horizontale_pixel__ * 2.54 / __bildbreite_in_CM__
__physicalsizesensorreal__ = 0.635 #ist in inc 1/4 ist dann der cm wert, von der größe vond er kamera vom sensro

def berechne_tiefe(x1, x2):
    hoehe = (__BRENNWEITE__ * __BREITE_ZWISCHEN_KAMERA__) / __physicalsizesensorreal__ * (x1 - x2)
    print("cm") # inc m
    print(hoehe) # inc m
    print("m") # inc m
    print(hoehe / 100) # in m
    return hoehe
