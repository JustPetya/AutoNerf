import os
import cv2
from time import sleep
from detection.object import position
# from mapping.distance import stereo_cam_depth


def main():
    print(position(0, 2))

    # cords = position(0, 2)
    # stereo_cam_depth(cords[0], cords[2])


if __name__ == "__main__":
    print(cv2.__version__)
    sleep(2.5)
    if os.name in ("nt", "dos"):
        os.system("cls")
    else:
        os.system("clear")
    main()
