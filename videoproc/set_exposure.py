import time

import cv2

cap = cv2.VideoCapture(0)


# 相机初始化
# cap = cv2.VideoCapture(0)
# ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280*2)
# ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# ret = cap.set(cv2.CAP_PROP_FPS, 60)
# fourcc = cv2.VideoWriter_fourcc(*'YUY2')
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
ret = cap.set(cv2.CAP_PROP_FOURCC, fourcc)

ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)




fps = cap.get(cv2.CAP_PROP_FPS)
print('fps:', fps)

auto_exposure = cap.get(cv2.CAP_PROP_AUTO_EXPOSURE)
print('auto exposure', auto_exposure)

auto_exposure_state = cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
# auto_exposure_state = cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
print('auto_exposure_state', auto_exposure_state)

auto_exposure1 = cap.get(cv2.CAP_PROP_AUTO_EXPOSURE)
print('auto exposure1:', auto_exposure1)


exposure_time = cap.get(cv2.CAP_PROP_EXPOSURE)
print('before set exposure time:', exposure_time)

state = cap.set(cv2.CAP_PROP_EXPOSURE, 1)
print('set state:', state)

exposure_time1 = cap.get(cv2.CAP_PROP_EXPOSURE)
print('after set exposure time:', exposure_time1)

time1 = time.time()

while True:

    time2 = time.time()
    time_elapsed = time2-time1
    print('time elapsed:', time_elapsed*1000)
    time1 = time2
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    cv2.waitKey(1)


