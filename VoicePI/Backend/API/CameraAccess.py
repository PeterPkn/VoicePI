from itertools import count
import cv2
import time


def take_photo():
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    count = 0
    while True:
        count += 1
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
        cv2.namedWindow("Input", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Input",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Input", frame)
        if count > 60:
            # cv2.imwrite('images/c1.png', frame)
            
            cv2.imwrite(f'images/pic_{time.time()}.png', frame)
            cv2.destroyAllWindows()
            break

        c = cv2.waitKey(1)
        if c == 27:
            break


def take_video():
    vid = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not vid.isOpened():
        raise IOError("Cannot open webcam")

    frame_width = int(vid.get(3))
    frame_height = int(vid.get(4))

    size = (frame_width, frame_height)
    result = cv2.VideoWriter(f'videos/video{time.time()}.avi',
                             cv2.VideoWriter_fourcc(*'MJPG'),
                             30, size)
    max_frames = 200
    frames = 0
    while True:
        frames += 1
        ret, frame = vid.read()
        cv2.imshow('Input', frame)
        if ret:
            result.write(frame)
            cv2.imshow('Frame', frame)
            if frames is max_frames:
                break
        # Break the loop
        else:
            break

    vid.release()
    result.release()

    cv2.destroyAllWindows()


# take_video()
# take_photo()
