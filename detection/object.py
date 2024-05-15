import time
import cv2

cascade = [cv2.CascadeClassifier('detection/haarcascade_eye.xml'),
           cv2.CascadeClassifier('detection/haarcascade_frontalface_default.xml')]
width_wanted: int = 700
height_wanted: int = 700
size_wanted = [width_wanted, height_wanted]
frame_rate: int = 1  # time in seconds to wait till next run
coordinates = []


def record(cam_input: int):
    camera = cv2.VideoCapture(cam_input)

    if not camera.isOpened():
        exit(66)  # cannot open input

    # size_wanted = (width_wanted, height_wanted)
    ret, cap = camera.read()

    if not ret:
        exit(70)  # internal software error

    camera.release()
    return cap


def resize_img(image):
    height, width = image.shape[:2]

    print(height, width)

    aspect_ratio = float(width) / float(height)
    ratio_wanted = float(size_wanted[0]) / float(size_wanted[1])  # Corrected width_wanted to next_size

    if aspect_ratio > ratio_wanted:
        new_width: int = int(ratio_wanted * height)
        new_height: int = int(height)
    else:
        new_width: int = int(width)
        new_height: int = int(width / ratio_wanted)

    prefinal_img = cv2.resize(image, (new_width, new_height))

    crop_x = (new_width - size_wanted[0]) // 2
    crop_y = (new_height - size_wanted[1]) // 2

    final_img = prefinal_img[crop_y:crop_y + size_wanted[1], crop_x:crop_x + size_wanted[0]]

    print(final_img.shape[:2])
    return final_img


def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade[0].detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if frame is not None and frame != ():
        x, y, w, h = frame[0]
        update = [x, y]
    else:
        update = []

    coordinates.append(update)

    return faces


def position(cam_1: int, cam_2: int):
    while True:
        capture = record(cam_1)
        # frame = resize_img(capture)
        face = detect_faces(capture)
        if face is not None and face != ():
            x, y, w, h = face[0]
            coordinates.append([x, y])
            break
        else:
            print("no face in frame")
            time.sleep(1.5)

    while True:
        capture = record(cam_2)
        # frame = resize_img(capture)
        face = detect_faces(capture)
        if face is not None and face != ():
            x, y, w, h = face[0]
            coordinates.append([x, y])
            break
        else:
            print("no face in frame")
            time.sleep(1.5)

    return coordinates
