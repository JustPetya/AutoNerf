import cv2

print(cv2.__version__)
# x_cord = 0
# y_cord = 0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera_r = cv2.VideoCapture(0)


def get_see_obj(cam_l: int, cam_r: int):
    cam = camera_r.read(cam_l)
    # cv2.VideoCapture.set(CV_CAP_PROP_FRAME_WIDTH, 500)
    # cv2.VideoCapture.set(CV_CAP_PROP_FRAME_HEIGHT, 500)
    gray = cv2.cvtColor(cam, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        detected: bool = True
        return detected
    else:
        detected: bool = False
        return detected


def position():
    pos = "1,1,1,1"
    return pos
