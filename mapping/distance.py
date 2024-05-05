__BRENNWEITE__ = 2.1
__breite_zwischen_kameras__ = 6  # muss timo noch sagen
__bildbreite_in_CM__ = 45.2  # muss timo mir sagen # 45,2 wäre wenn 1280*720pixel & 72 dpi
__horizontale_pixel__ = 720  # max res 1280* 720
__pixeldichte__ = __horizontale_pixel__ * 2.54 / __bildbreite_in_CM__
__physicalsizesensorreal__ = 0.635
__breite_zwischen_kamera_turret__ = 12

import math


def stereo_cam_depth(xr, xl):
    if xr < xl:  # wenn xr < xl dann tauschen, so entstehen keine minus zahlen
        xr, xl = xl, xr
    depth = (__BRENNWEITE__ * __breite_zwischen_kameras__) / (__physicalsizesensorreal__ * (xr - xl))
    print("Depth in cm:")
    print(depth)  # tiefe in cm
    print("Depth in m:")
    print(depth / 100)  # tiefe in meter
    return depth


def target_angels_turret(xr, xl, y):
    depth = stereo_cam_depth(xr, xl)
    if xl < xr:
        floor_depth = math.cos(y) * depth
        cam_to_turret_angel = 180 - xl - math.asin((math.sin(xl) * 0.5 * __breite_zwischen_kameras__) / floor_depth)
        floor_turret_depth = math.sqrt((__breite_zwischen_kamera_turret__ ** 2) + (floor_depth ** 2)
                                       - (2 * __breite_zwischen_kameras__ * floor_depth
                                       * math.cos(cam_to_turret_angel)))
        turret_to_cam_angel = math.asin((math.sin(cam_to_turret_angel) * floor_depth) / floor_turret_depth)
    pan = None
    tilt = None
    return pan, tilt
