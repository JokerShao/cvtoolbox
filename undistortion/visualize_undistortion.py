import numpy as np
import cv2

cnt = 0
cnt1 = 0

ROW_SQUARE_NUM = 18
COL_SQUARE_NUM = 32
IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 1080

black_square = np.zeros((int(IMAGE_HEIGHT/ROW_SQUARE_NUM), int(IMAGE_WIDTH/COL_SQUARE_NUM), 3), np.uint8)
white_square = np.ones((int(IMAGE_HEIGHT/ROW_SQUARE_NUM), int(IMAGE_WIDTH/COL_SQUARE_NUM), 3), np.uint8) * 255

black = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH, 3), np.uint8)

flag = True

for row in range(0, IMAGE_HEIGHT, int(IMAGE_HEIGHT/ROW_SQUARE_NUM)):
    for col in range(0, IMAGE_WIDTH, int(IMAGE_WIDTH/COL_SQUARE_NUM)):
        if flag:
            black[row:row+int(IMAGE_HEIGHT/ROW_SQUARE_NUM), col:col+int(IMAGE_WIDTH/COL_SQUARE_NUM),:] = black_square
        else:
            black[row:row+int(IMAGE_HEIGHT/ROW_SQUARE_NUM), col:col+int(IMAGE_WIDTH/COL_SQUARE_NUM),:] = white_square
        flag = not flag
    flag = not flag

for cnt in range(0, 1):
    for cnt1 in range(0, 5):
        fs = cv2.FileStorage('E:\\P4Workspace\\calibration-package\\intrinsic_params\\sony_MC2500\\'+str(cnt1)+'.xml', cv2.FileStorage_READ)
        # fs = cv2.FileStorage('E:\\zexishao\\calibrationtool\\StereoMethod_PY\\20181116-canon\\'+str(cnt1)+'.xml', cv2.FileStorage_READ)
        cameraMatrix = fs.getNode('M').mat()
        distCoeffs = fs.getNode('D').mat()

        print(cameraMatrix)
        # print(distCoeffs)

        undistortion = cv2.undistort(black, cameraMatrix, distCoeffs)
        # undistortion = cv2.undistort(black, cameraMatrix, None)
        # small0 = cv2.resize(black, (int(IMAGE_WIDTH /2) , int(IMAGE_HEIGHT / 2)))
        # small1 = cv2.resize(undistortion, (int(IMAGE_WIDTH /2) , int(IMAGE_HEIGHT / 2)))
        # differ = cv2.subtract(small1, small0)
        cv2.imshow('undistortion', undistortion)
        # cv2.imshow('differ', differ)
        # cv2.imshow('small0', small0)
        # cv2.imshow('small1', small1)
        # cv2.imwrite('E:\\P4Workspace\\qiedianceshi\\intrinsic_params\\dahengvision\\'+str(cnt1)+'-undist.jpg', undistortion)
        cv2.waitKey(0)
        cv2.destroyAllWindows()