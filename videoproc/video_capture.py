import cv2

# 相机初始化
cap = cv2.VideoCapture(0)
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280*2)
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
ret = cap.set(cv2.CAP_PROP_FPS, 60)
fourcc = cv2.VideoWriter_fourcc(*'YUY2')
ret = cap.set(cv2.CAP_PROP_FOURCC, fourcc)

cnt = 0
cntt = 0

while True:
    retval, frame = cap.read()

    small_frame = cv2.resize(frame, (1280, 360))

    if retval is True:
        cv2.imshow('frame', small_frame)
        retkey = cv2.waitKey(1) & 0xFF
        if retkey == ord('q'):
            break
        # elif retkey == ord('g'):
        if cnt >= 3:
            cv2.imwrite('./hand/'+str(cntt)+'.png', frame)
            cnt = 0
            cntt += 1
        cnt+=1

cv2.destroyAllWindows()

