import cv2

test1_path = "detection/test1.jpg"
test2_path = "detection/test2.jpg"
test3_path = "detection/test3.png"

face_cascade = cv2.CascadeClassifier('detection/haarcascade_frontalface_default.xml')
width: int = 180
height: int = 180
frame_rate: int = 10


def get_see_obj(camera: int):
    cap = cv2.imread(test3_path)  # cv2.VideoCapture(camera).read()
    # cap.set(cv2.CAP_PROP_FPS, int(frame_rate))
    cap_height, cap_width, cap_channel = cap.shape

    print("height: ", cap_height, "\nwidth: ", cap_width)

    cap_height_center = cap_height / 2
    cap_width_center = cap_width / 2
    print(cap_height_center)
    print(cap_width_center)
    cap_top_wanted = cap_height_center - (height / 2)
    cap_left_wanted = cap_width_center - (width / 2)
    print(int(cap_top_wanted))
    print(int(cap_left_wanted))

    cap_size = cap[int(cap_top_wanted):500, int(cap_left_wanted):500]

    gray = cv2.cvtColor(cap_size, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # cv2.imshow("d", cap)

    if len(faces) > 0:
        print("true")
        return True
    else:
        print("false")
        return


def position(pos1: str, cam2: int):
    print("pos1", cam2)
    # pos = "1,1,1,1"
    return True
