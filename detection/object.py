import time
import cv2

face_cascade = cv2.CascadeClassifier('detection/haarcascade_frontalface_default.xml')
width: int = 180
height: int = 180
length = 1.1
fps = 1


def get_see_obj(camera: int):
    cap = cv2.VideoCapture(camera)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 180)
    ret, capch = cap.read()  # cv2.imread(test1_path)
    cap_height, cap_width, _ = capch.shape

    print(cap_width)
    cap_size = capch.resize(180)
    print(cap_size)

    while length < fps:
        time.sleep(.1)
    try:
        get_see_obj(camera)
    except KeyboardInterrupt:
        exit(0)
    # cap_height_center = cap_height / 2
    # cap_width_center = cap_width / 2
    # print(cap_height_center)
    # print(cap_width_center)
    # cap_top_wanted = cap_height_center - (height / 2)
    # cap_left_wanted = cap_width_center - (width / 2)
    # print(int(cap_top_wanted))
    # print(int(cap_left_wanted))
    #
    # cap_size = cap[int(cap_top_wanted):500, int(cap_left_wanted):500]
    # print(cap_size)
    #
    # gray = cv2.cvtColor(cap_size, cv2.COLOR_BGR2GRAY)
    # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #
    # cv2.imshow("d", cap)
    # time.sleep(1000)
    #
    # if len(faces) > 0:
    #     print("true")
    #     return True
    # else:
    #     print("false")
    #     return


def position(pos1: str, cam2: int):
    print("pos1", cam2)
    # pos = "1,1,1,1"
    return True
