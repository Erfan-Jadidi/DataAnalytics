import cv2

video_reader = cv2.VideoCapture("my_vid.mp4")

ret, frame = video_reader.read()

while ret:
    ret, frame = video_reader.read()

    frame = cv2.resize(frame, (640, 480))
    edge = cv2.Canny(frame, 20, 200)

    cv2.imshow('Live Video', frame)
    cv2.imshow('Live Edge', edge)
    if cv2.waitKey(1) == 27:
        break
