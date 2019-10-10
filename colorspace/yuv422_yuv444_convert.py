import cv2
import numpy as np

B = 255
G = 0
R = 0
image_size = (1080, 1920)

# 创建纯色三通道图像
blue_channel = np.full(image_size, B, dtype=np.uint8)
green_channel = np.full(image_size, G, dtype=np.uint8)
red_channel = np.full(image_size, R, dtype=np.uint8)
image = cv2.merge((blue_channel, green_channel, red_channel))

# Load sample image
img_bgr = cv2.imread("D:\\DataRepository\\greenscreen\\mountain.jpg")
# img_bgr = image
cv2.imshow("original", img_bgr)
# cv2.waitKey(0)

# Convert from BGR to YUV
img_yuv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YUV)

# Converting directly back from YUV to BGR results in an (almost) identical image
img_bgr_restored = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
cv2.imshow("converted by yuv", img_bgr_restored)
# cv2.waitKey(0)
diff = img_bgr.astype(np.int16) - img_bgr_restored
print("mean/stddev diff (BGR => YUV => BGR)", np.mean(diff), np.std(diff))

# Create YUYV from YUV
y0 = np.expand_dims(img_yuv[...,0][::,::2], axis=2)
u = np.expand_dims(img_yuv[...,1][::,::2], axis=2)
y1 = np.expand_dims(img_yuv[...,0][::,1::2], axis=2)
v = np.expand_dims(img_yuv[...,2][::,::2], axis=2)
img_yuyv = np.concatenate((y0, u, y1, v), axis=2)
img_yuyv_cvt = img_yuyv.reshape(img_yuyv.shape[0], img_yuyv.shape[1] * 2, int(img_yuyv.shape[2] / 2))

# Convert back to BGR results in more saturated image.
img_bgr_restored = cv2.cvtColor(img_yuyv_cvt, cv2.COLOR_YUV2BGR_YUYV)
cv2.imshow("converted by yuyv", img_bgr_restored)
# cv2.waitKey(0)

diff = img_bgr.astype(np.int16) - img_bgr_restored
print("mean/stddev diff (BGR => YUV => YUYV => BGR)", np.mean(diff), np.std(diff))

# --------------------------
# 插值算法计算yuv后转回BGR
y, uv = cv2.split(img_yuyv_cvt)

# 显示原始 UV值
cv2.imshow('u', u)
cv2.imshow('v', v)

# 立方插值
tm = cv2.TickMeter()
tm.start()
# interpolation_u = cv2.resize(u, (1920, 1080), interpolation=cv2.INTER_CUBIC)
interpolation_u = cv2.resize(u, (1920, 1080), interpolation=cv2.INTER_LINEAR)
tm.stop()
print(tm.getTimeMilli())
# interpolatino_v = cv2.resize(v, (1920, 1080), interpolation=cv2.INTER_CUBIC)
interpolatino_v = cv2.resize(v, (1920, 1080), interpolation=cv2.INTER_LINEAR)
cv2.imshow('interpolation_u', interpolation_u)
cv2.imshow('interpolatino_v', interpolatino_v)
# cv2.waitKey(0)

# 重组yuv
interpolation_yuv = cv2.merge((y, interpolation_u, interpolatino_v))
bgr_useinterpolationyuv = cv2.cvtColor(interpolation_yuv, cv2.COLOR_YUV2BGR)
diff_useinterpolatinoyuv = img_bgr.astype(np.int16) - bgr_useinterpolationyuv
print("mean/stddev diff (BGR => YUV => YUYV => interpolation => YUV => BGR)", np.mean(diff_useinterpolatinoyuv), np.std(diff_useinterpolatinoyuv))

cv2.imshow("bgr_useinterpolationyuv", bgr_useinterpolationyuv)
cv2.waitKey(0)

