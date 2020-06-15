import cv2


img = cv2.imread('im.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

integral = cv2.integral(gray)

cv2.imshow('integral', integral)
cv2.waitKey(0)

