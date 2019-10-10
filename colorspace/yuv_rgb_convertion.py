import numpy as np
import cv2

B = 60
G = 120
R = 200
image_size = (300, 300)

# 创建纯色三通道图像
blue_channel = np.full(image_size, B, dtype=np.uint8)
green_channel = np.full(image_size, G, dtype=np.uint8)
red_channel = np.full(image_size, R, dtype=np.uint8)
image = cv2.merge((blue_channel, green_channel, red_channel))

# image_big = cv2.imread('D:\\DataRepository\\greenscreen\\mountain.jpg')
# image = cv2.resize(image_big, (300, 300))

cv2.imshow('image', image)
cv2.waitKey(1)
print('BGR: ', B, ',', G, ',', R, '\n')

# 第一种转换方式，OpenCV自带-------------------------------->采用
image_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
print('YUV convert by OpenCV:', image_yuv[0][0][0], ',', image_yuv[0][0][1], ',', image_yuv[0][0][2], '\n')

# 第二种转换方式，取自https://blog.csdn.net/liyuanbhu/article/details/68951683
Y0 = 0.299 * R + 0.587*G+0.114*B
V0 = 0.500 * R - 0.419 * G - 0.081 * B + 128
U0 = -0.169 * R - 0.331 * G + 0.500 * B + 128
# print('YUV convert method0: ', Y0, U0, V0, '\n')

# 第三种转换方式
Y1 = int(0.299*R + 0.587*G + 0.114*B)
U1 = int((B-Y1)*0.492)        + 128.0
V1 = round((R-Y1)*0.877)       + 128.0
# print('YUV convert method1: ', Y1, U1, V1, '\n')

# 第四种转换方式，和第三种一样，但是不截断
Y2 = 0.299*R + 0.587*G + 0.114*B
U2 = (B-Y2)*0.492        + 128.0
V2 = (R-Y2)*0.877       + 128.0
# print('YUV convert method2: ', Y2, U2, V2, '\n')

# 第五种转换方式，和第三种一样，不过周围取近整----------------------->采用
Y3 = min(255, max(0, round(0.299*R + 0.587*G + 0.114*B)))
U3 = min(255, max(0, round((B-Y3)*0.492)        + 128.0))
V3 = min(255, max(0, round((R-Y3)*0.877)       + 128.0))
print('YUV convert method3: ', Y3, U3, V3, '\n')

# 第六种转换方式
Y4 = 0.299*R + 0.587*G + 0.114*B
U4 = -0.147*R - 0.289*G + 0.436*B
V4 = 0.615*R - 0.515*G - 0.100*B
# print('YUV convert method4: ', Y4, U4, V4, '\n')

# OpenCV YUV to BGR----------------------------------------->采用
image_yuv2bgr = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2BGR)
print('OpenCV convert yuv to BGR: ', image_yuv2bgr[0][0][0], image_yuv2bgr[0][0][1], image_yuv2bgr[0][0][2], '\n')
# cv2.imshow('image yuv2bgr', image_yuv2bgr)
# cv2.waitKey(0)

# YUV转回BGR
Us = U1      - 128.0
Vs = V1      - 128.0
nR = Y1 + 1.140*Vs
nG = Y1 - 0.395*Us - 0.581*Vs
nB = Y1 + 2.032*Us
print('new BGR:', nB, nG, nR, '\n')

# YUV3转回BGR------------------------------------>采用
Us3 = U3      - 128.0
Vs3 = V3       - 128.0
nR3 = min(255, max(0, round(Y3 + 1.140*Vs3)))
nG3 = min(255, max(0, round(Y3 - 0.395*Us3 - 0.581*Vs3)))
nB3 = min(255, max(0, round(Y3 + 2.032*Us3)))
print('method 3 to BGR : ', nB3, nG3, nR3, '\n')

# 另一种转换
R4 = Y3 + 1.403 * Vs3
G4 = Y3 - 0.343 * Us3 - 0.714 * Vs3
B4 = Y3 + 1.77 * Us3
print('method 4 to BGR : ', B4, G4, R4, '\n')

cv2.imshow('image_yuv0', image_yuv[:, :, 0])
cv2.imshow('image_yuv1', image_yuv[:, :, 1])
cv2.imshow('image_yuv2', image_yuv[:, :, 2])
cv2.waitKey(0)

