# -*- coding: utf-8 -*-
from PIL import Image
from pylab import *
#import matplotlib.pyplot as plt
import numpy as np
import cv2
import pdb
import sys

Tx = 0
Ty = 0
# mouse callback function
def draw_boundingbox(event, x, y, flags, param):
    global Tx,Ty
     
    if event == cv2.EVENT_LBUTTONDOWN:
        Tx, Ty = x, y
        print([Tx,Ty])

    #elif event == cv2.EVENT_MOUSEMOVE:
    #    print('EVENT_MOUSEMOVE')
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP')
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        print('EVENT_RBUTTONDOWN')


if __name__ == '__main__':

    cap = cv2.VideoCapture(sys.argv[1])
    cv2.namedWindow('tracking')
    cv2.setMouseCallback('tracking',draw_boundingbox)

    isInit = True
    src_point = []
    dst_point = []
    Hm = []
    dSize = []
    imd = []
    #pdb.set_trace()
    ret, frame0 = cap.read()
    while(cap.isOpened()):
        '''
        ret, frame0 = cap.read()
        if not ret:
            break
        '''
        if isInit:
            # soure iamge points
            im = array(frame0)  
            imshow(im)

            # raw image 4 points
            print('Please click 4 points')
            src_point = ginput(4)  
            src_point = np.float32(src_point)
            print(src_point)

            # destination image points
            imd = array(Image.open('E:\\greenscreen\\allblue.jpg'))  
            imshow(imd)
            # desired image size,(line,row)
            #dSize=(1204,550)
            dSize = (imd.shape[1],imd.shape[0])
            # raw image 4 points
            print('Please click 4 points')
            dst_point = ginput(4)  
            dst_point = np.float32(dst_point)
            print(dst_point)
            # At least four points, one to one, find the mapping matrix h
            Hm, s = cv2.findHomography(src_point, dst_point, cv2.RANSAC, 10)   
            print('mapping:',Hm,s)
            isInit = False

        nimg = cv2.warpPerspective(frame0, Hm, dSize)
        #cv2.circle(img, (x,y), radius, (b, g, r), -1)
        cv2.circle(frame0,(Tx,Ty),6,(0,0,255),-1)
        cv2.imshow('tracking',frame0)

        cv2.imshow('transform',nimg)

        #pdb.set_trace()
        # transform the raw coordinate to de destination by Homography matrix
        pts = np.float32([[Tx,Ty]]).reshape(-1,1,2)
        pointsOut = cv2.perspectiveTransform(pts, Hm)
        #print('pointsOut:',[pointsOut[0,0,0],pointsOut[0,0,1]])
        cv2.circle(imd,(pointsOut[0,0,0],pointsOut[0,0,1]),6,(0,0,255),-1)
        cv2.imshow('ref',imd)
        #pdb.set_trace()
        '''
        figure(0)
        subplot(121)
        imshow(frame0) 
        subplot(122)
        imshow(nimg)
        show()
        '''

        c = cv2.waitKey(1000) & 0xFF
        if c==27 or c==ord('q'):
            break
    cap.release()

    