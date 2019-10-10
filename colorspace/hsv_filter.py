import numpy as np
import cv2

def hsv_filter():
    """
    doc string
    """
    cap = cv2.VideoCapture(
        'E:\\greenscreen\\greenscreen1.mp4')

    while True:
        retval, frame = cap.read()
        if not retval:
            break
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # hsv_filter = cv2.bilateralFilter(hsv, 9, 1.0, 1.0)
        # hsv_filter = cv2.blur(hsv, (7, 7))

        # difference = cv2.subtract(hsv, hsv_filter)
        # diff_h, diff_s, diff_v = difference[:,:,0], difference[:,:,1], difference[:,:,2]
        # retval, diff_bin = cv2.threshold(difference, 1, 255, cv2.THRESH_BINARY)

        channels = cv2.split(hsv)
        h, s, v = channels
        cv2.imshow('h', h)
        cv2.imshow('s', s)
        cv2.imshow('v', v)



        # cv2.imshow('difference', difference)
        # cv2.imshow('hsv', hsv)
        # cv2.imshow('hsv filter', hsv_filter)
        # cv2.imshow('diff bin', diff_bin)
        retval = cv2.waitKey(0) & 0xFF
        if retval == ord('q'):
            break

if __name__ == '__main__':
    hsv_filter()