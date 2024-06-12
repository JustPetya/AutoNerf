import math

brennweite = 2.1
raum_zwischen_kameras = 6
bildbreite_in_cm = 33.9
horizontale_pixel = 720
pixeldichte = horizontale_pixel * 2 / bildbreite_in_cm
physicalsizesensorreal = 0.635

raum_zwischen_kameras_turret = 12


def stereo_cam_depth(xr, xl):
    hoehe = (brennweite * raum_zwischen_kameras) / physicalsizesensorreal * (xl - xr)
    print(hoehe, " cm\n", (hoehe / 100), " m")
    return hoehe


def target_angels_turret(xr, xl, y):

    def deg_to_rad(x): return math.pi/180 * x

    def map(x, in_min, in_max, out_min, out_max): return (
        x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    depth = stereo_cam_depth(xr, xl)

    angle_y = map(y, 0, 360, 80, 0)

    angle_xl = map(xl, 0, 640, 130, 50)

    floor_depth: float = math.cos(angle_y) * depth

    cam_to_turret_angle: float = 180 - angle_xl -  math.asin((math.sin(angle_xl) * 0.5 * raum_zwischen_kameras) / floor_depth)

    floor_turret_depth: float = math.sqrt((raum_zwischen_kameras_turret ** 2) + (floor_depth ** 2) - (2 * raum_zwischen_kameras_turret * floor_depth * math.cos(cam_to_turret_angle)))

    turret_to_cam_angel: float = math.asin( (math.sin(cam_to_turret_angle) * floor_depth) / floor_turret_depth)

    pan: int = 87
    tilt: int = int(180 - turret_to_cam_angel)
    return pan, tilt
