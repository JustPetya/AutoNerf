import os
import cv2
from time import sleep
# from detection.position import get_pos
from detection.object import get_see_obj
from math.distance import berechne_tiefe


def main():

    print(berechne_tiefe(10,21))
    # while True:
    try:
        get_see_obj(0)
        if get_see_obj:
            print("Face detected: x=" + "x_cord" + " y=" + "y_cord")
            # dist(1, 1, 1, 1)
        else:
            print("No humans in frame detected!")
    except KeyboardInterrupt:
        print("\nShutting down with code \"0\"...")
        exit(0)

    # x = get_pos().split(",")
    # print(x)


if __name__ == "__main__":
    print(cv2.__version__)
    sleep(5)
    if os.name in ("nt", "dos"):
        os.system("cls")
    else:
        os.system("clear")
    main()
