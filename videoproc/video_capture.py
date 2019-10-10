import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    retval, frame = cap.read()
    if retval is True:
        cv2.imshow('frame', frame)
        retkey = cv2.waitKey(1) & 0xFF
        if retkey == ord('q'):
            break

cv2.destroyAllWindows()

