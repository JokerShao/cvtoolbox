import time
import cv2
import numpy as np


while True:
    image = np.zeros((1080, 1920, 3), dtype=np.uint8)*255

    time_now = str(int(time.time()*1000))
    img = cv2.putText(image, time_now[-6:], (0, 1080//2), cv2.FONT_HERSHEY_SIMPLEX, 11, (0, 0, 255),18)

    cv2.imshow('img', img)
    cv2.waitKey(1)
    

#time_last = time.time()*1000

#while True:
#    time_now = time.time()*1000
#    # print(time_now-time_last)
#    if (time_now-time_last)>2:
#        print(time.time()*1000)
#        time_last = time_now
