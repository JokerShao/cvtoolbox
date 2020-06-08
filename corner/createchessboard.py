import numpy as np
import cv2

ROW_SQUARE_NUM = 4
COL_SQUARE_NUM = 4
IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 1080

black_square = np.zeros((int(IMAGE_HEIGHT/ROW_SQUARE_NUM), int(IMAGE_WIDTH/COL_SQUARE_NUM), 3), np.uint8)
white_square = np.ones((int(IMAGE_HEIGHT/ROW_SQUARE_NUM), int(IMAGE_WIDTH/COL_SQUARE_NUM), 3), np.uint8) * 255

chessboard = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH, 3), np.uint8)

flag = True

for row in range(0, IMAGE_HEIGHT, int(IMAGE_HEIGHT/ROW_SQUARE_NUM)):
    for col in range(0, IMAGE_WIDTH, int(IMAGE_WIDTH/COL_SQUARE_NUM)):
        if flag:
            chessboard[row:row+int(IMAGE_HEIGHT/ROW_SQUARE_NUM), col:col+int(IMAGE_WIDTH/COL_SQUARE_NUM),:] = black_square
        else:
            chessboard[row:row+int(IMAGE_HEIGHT/ROW_SQUARE_NUM), col:col+int(IMAGE_WIDTH/COL_SQUARE_NUM),:] = white_square
        flag = not flag
    flag = not flag

cv2.imshow('chessboard', chessboard)
# cv2.imwrite('chessboard.jpg', chessboard)
cv2.waitKey(0)
