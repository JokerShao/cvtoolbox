import cv2


# 参数配置
cam_w = 1920
cam_h = 1080
cam_fps = 30

# 相机初始化
cap = cv2.VideoCapture(0)
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, cam_w)
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_h)
ret = cap.set(cv2.CAP_PROP_FPS, cam_fps)
# fourcc = cv2.VideoWriter_fourcc(*'YUY2')
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
ret = cap.set(cv2.CAP_PROP_FOURCC, fourcc)

cnt = 0
while True:
    retval, frame = cap.read()

    if retval is True:
        cv2.imshow('frame', frame)
        retkey = cv2.waitKey(1) & 0xFF
        if retkey == ord('q'):
            break
        elif retkey == ord('g'):
            cv2.imwrite('./imgs/'+str(cnt)+'.png', frame)
            cnt = 0
        cnt+=1

cv2.destroyAllWindows()

