import cv2

# test_path = "detection/test.png"

face_cascade = cv2.CascadeClassifier('detection/haarcascade_frontalface_default.xml')
width: int = 500
height: int = 500
frame_rate: int = 15


def get_see_obj(camera: int):
    cap = cv2.VideoCapture(camera).read()  # cv2.imread(test_path)
    # cap.set(cv2.CAP_PROP_FPS, int(frame_rate))
    cap_height, cap_width, cap_channel = cap.shape

    print("height: ", cap_height, "\nwidth: ", cap_width)

    cap_height_center = cap_height / 2
    cap_width_center = cap_width / 2
    cap_top_wanted = cap_height_center - (height / 2)
    cap_left_wanted = cap_width_center - (width / 2)

    cap_size = cap[cap_top_wanted:500, cap_left_wanted:500]

    gray = cv2.cvtColor(cap_size, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    cv2.imshow("d", cap)

    if len(faces) > 0:
        return True
    else:
        return False


def position(pos1: str, cam2: int):
    print(pos1, cam2)
    pos = "1,1,1,1"
    return pos
