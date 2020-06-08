# -*- coding: utf-8 -*-
from PIL import Image
from pylab import *
#import matplotlib.pyplot as plt
import numpy as np
import cv2
import pdb

if __name__ == '__main__':

    # soure iamge points
    im = array(Image.open('E:\\greenscreen\\14_cut\\13.jpg'))
    imshow(im)

    # raw image 4 points
    print('Please click 4 points')
    src_point = ginput(4)  
    src_point = np.float32(src_point)
    print(src_point)

    # destination image points
    imd = array(Image.open('E:\\greenscreen\\allblue.jpg'))  
    imshow(imd)
    # raw image 4 points
    print('Please click 4 points')
    dst_point = ginput(4)  
    dst_point = np.float32(dst_point)
    print(dst_point)
    #print(imd.shape[0],imd.shape[1],imd.shape[2])

    # desired image size,(line,row)
    dsize=(1204,550)

    #dst_point = np.float32([[0,0],[0,dsize[1]-1],[dsize[0]-1,dsize[1]-1],[dsize[0]-1,0]])
    # At least four points, one to one, find the mapping matrix h
    #pdb.set_trace()
    h, s = cv2.findHomography(src_point, dst_point, cv2.RANSAC, 10)

    fs = cv2.FileStorage('E:\\P4Workspace\\Proj\\Config\\CanonEOS\\intrinmat.xml', cv2.FileStorage_READ)
    K = fs.getNode('M').mat()
    print('K:', K)
    retval, rot, trans, normalv = cv2.decomposeHomographyMat(h, K)

    print('retva:', retval)
    print('rot:', rot)
    print('trans:', trans)
    print('normal vector', normalv)

    # print(h)
    # print(s)
    book = cv2.warpPerspective(im, h, dsize)
    # image is RGB��cv2.imwrite save as BGR
    book = cv2.cvtColor(book, cv2.COLOR_RGB2BGR)
    cv2.imshow('book', book)
    cv2.waitKey(0)
    # cv2.imwrite('dst.jpg',book)

