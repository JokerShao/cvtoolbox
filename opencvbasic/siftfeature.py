import numpy as np
import cv2


def sift_func(img_path1,img_path2):
    # img_1 = cv2.imread(img_path1)

    # img_2 = cv2.imread(img_path2)

    img_1 = cv2.imread('lena.jpg')
    img_2 = cv2.rotate(img_1, cv2.ROTATE_90_CLOCKWISE)
    gray_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
    gray_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)

    # SIFT特征计算
    sift = cv2.xfeatures2d.SIFT_create()
    psd_kp1, psd_des1 = sift.detectAndCompute(gray_1, None)
    psd_kp2, psd_des2 = sift.detectAndCompute(gray_2, None)
# src = cv2.drawKeypoints(src, outImage=src, keypoints=keypoints, flags=cv2.DrawMatchesFlags_DEFAULT)

    # Flann特征匹配
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(psd_des1, psd_des2, k=2)
    goodMatch = []
    for m, n in matches:
        # goodMatch是经过筛选的优质配对，如果2个配对中第一匹配的距离小于第二匹配的距离的1/2，
        # 基本可以说明这个第一配对是两幅图像中独特的，不重复的特征点,可以保留。
        if m.distance < 0.50*n.distance:
            goodMatch.append(m)

    # 增加一个维度
    goodMatch = np.expand_dims(goodMatch, 1)
    # print(goodMatch[:20])
    img_out = cv2.drawMatchesKnn(img_1, psd_kp1,
                                 img_2, psd_kp2,
                                 goodMatch[:20], None, flags=2)
    return img_out

if __name__ == '__main__':
    img_path1 = 'shanghai_01.png'
    img_path2 = 'shanghai_02.png'
    img_out = sift_func(img_path1, img_path2)
    
    cv2.imshow('image', img_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
