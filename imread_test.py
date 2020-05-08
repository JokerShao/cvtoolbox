import cv2

img = cv2.imread('/home/zexi/slam_learn/rgbd_dataset_freiburg2_large_with_loop/rgb/1311875572.406161.png', -1)
cvtimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


img_gray = cv2.imread('/home/zexi/slam_learn/rgbd_dataset_freiburg2_large_with_loop/rgb/1311875572.406161.png', 0)

threshold = 1

s12 = cv2.subtract(img_gray, cvtimg)
_, b12 = cv2.threshold(s12, threshold, 255, cv2.THRESH_BINARY)

s21 = cv2.subtract(cvtimg, img_gray)
_, b21 = cv2.threshold(s21, threshold, 255, cv2.THRESH_BINARY)

cv2.imshow('b12', b12)
cv2.imshow('b21', b21)
cv2.waitKey(0)
