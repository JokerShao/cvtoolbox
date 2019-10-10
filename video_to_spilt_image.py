"""
convert video to some image
"""
import cv2
import numpy as np

def run():
    """ doc string """
    step = 3
    cur = 0
    cnt = 0

    cap = cv2.VideoCapture('./05.mov')
    
    while True:
        retval, frame = cap.read()
        if not retval:
            break
        if cur < step:
            cur += 1
        else:
            cur = 0
            cv2.imwrite('./image05/'+str(cnt)+'.jpg', frame)
            cnt+=1
            cv2.imshow('frame', frame)
            cv2.waitKey(1)


if __name__ == '__main__':
    """ doc string """
    run()