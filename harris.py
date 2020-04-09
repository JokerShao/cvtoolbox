import cv2

stereo_img = cv2.imread('/home/zexi/robotic_operator/dataset/image/narrow/203.png')
stereo_gray = cv2.cvtColor(stereo_img, cv2.COLOR_BGR2GRAY)
h, w = stereo_gray.shape

left = stereo_img[:,w//2:w]
right = stereo_img[:,0:w//2]

left_gray = stereo_gray[:,w//2:w]
right_gray = stereo_gray[:,0:w//2]

left_harris = cv2.cornerHarris(left_gray, 2, 3, 0.0000004)
right_harris = cv2.cornerHarris(right_gray, 2, 3, 0.0000004)

left[left_harris>0.01*left_harris.max()]=[0,0,255]
right[right_harris>0.01*right_harris.max()] = [0, 0, 255]

# cv2.imshow('dst',img)

cv2.imshow('left', left)
cv2.imshow('right', right)
# cv2.imshow('left_harris', left_harris)
# cv2.imshow('right_harris', right_harris)
cv2.waitKey(0)
