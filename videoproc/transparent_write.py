import numpy as np
import cv2


for i in range(500, 980):
    img = cv2.imread('frames/{}.png'.format(str(i).zfill(4)), -1)
    b = cv2.resize(img[:,:,0], (1920//2, 1080//2))
    g = cv2.resize(img[:,:,1], (1920//2, 1080//2))
    r = cv2.resize(img[:,:,2], (1920//2, 1080//2))
    a = cv2.resize(img[:,:,3], (1920//2, 1080//2))
    # print(a[800//2:900//2, 400//2:500//2])
    _, bin_a = cv2.threshold(a, 254, 255, cv2.THRESH_OTSU)

    print(np.sum(a))
    # print('==============')
    # for j in range(500):
    #     print(a[j,:].min(), a[j,:].max())
    # cv2.imshow('b', b)
    # cv2.imshow('g', g)
    # cv2.imshow('r', r)
    # cv2.imshow('a', bin_a)
    # cv2.waitKey(0)

