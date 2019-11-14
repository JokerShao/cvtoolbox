import cv2
import numpy as np

camid = 64

cap = cv2.VideoCapture('rtsp://admin:admin888@192.168.1.'+str(camid)+':554//Streaming/Channels/1')
cnt = 0

while True:
    retval, frame = cap.read()
    if retval is True:
        cv2.imshow('frame', frame)
        retkey = cv2.waitKey(1) & 0xFF
        if retkey == ord('q'):
            break
        elif retkey == ord('s'):
            cv2.imwrite(str(cnt)+'.jpg', frame)
            cnt+=1

cv2.destroyAllWindows()

