"""
preprocessing image for recognize algorithm
"""
import cv2
import numpy as np

def fun1():
    """ doc string """
    ledoff = cv2.imread('./image01/0.jpg')
    ledon = cv2.imread('./image01/1.jpg')

    difference = cv2.subtract(ledon, ledoff)
    channels = cv2.split(difference)
    blue, green, red = channels

    blue = cv2.equalizeHist(blue)

    cv2.imshow('ledoff', ledoff)
    cv2.imshow('ledon', ledon)
    cv2.imshow('difference', difference)
    cv2.imshow('blue', blue)
    cv2.imshow('green', green)
    cv2.imshow('red', red)
    cv2.waitKey(0)

def equalizeHist():
    """ doc string """
    ledoff = cv2.imread('./image01/0.jpg')
    blue, green, red = cv2.split(ledoff)

    blue = cv2.equalizeHist(blue)
    green = cv2.equalizeHist(green)
    red = cv2.equalizeHist(red)

    processed = cv2.merge((blue, green, red))
    cv2.imshow('processed', processed)
    cv2.waitKey(0)

def gamma():
    """ doc string """
    GAMMA = 0.5
    ledoff = cv2.imread('./image01/0.jpg')

    blue, green, red = cv2.split(ledoff)

    processed = cv2.pow(blue, GAMMA)
    cv2.normalize(processed, processed, 0, 255, cv2.NORM_MINMAX)
    cv2.convertScaleAbs(processed, processed)
    
    # for row in range(1080):
    #     for col in range(1920):
    #         ledoff[row, col, 0] = cv2.pow(ledoff[row, col, 0], GAMMA)
    #         ledoff[row, col, 1] = cv2.pow(ledoff[row, col, 1], GAMMA)
    #         ledoff[row, col, 2] = cv2.pow(ledoff[row, col, 2], GAMMA)

    cv2.imshow('gamma processed', processed)
    cv2.waitKey(0)

def calc_and_draw_hist(image, color):
    """ doc string """
    hist= cv2.calcHist([image], [0], None, [256], [0.0,255.0])
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256,256,3], np.uint8)
    hpt = int(0.9* 256)
    
    for h in range(256):  
        intensity = int(hist[h]*hpt/maxVal)  
        cv2.line(histImg,(h,256), (h,256-intensity), color)  
          
    return histImg, maxVal

def show_hist():
    """ doc string """
    ledoff = cv2.imread('./image01/303.jpg')
    ledon = cv2.imread('./image01/304.jpg')
    diff = cv2.subtract(ledon, ledoff)
    b, g, r = cv2.split(diff)
    s = b + g
    
    histImgB = calc_and_draw_hist(b, [255, 0, 0])
    histImgG = calc_and_draw_hist(g, [0, 255, 0])
    histImgR = calc_and_draw_hist(r, [0, 0, 255])
    histImgS = calc_and_draw_hist(s, [255, 255, 255])
    
    cv2.imshow("histImgB", histImgB)
    cv2.imshow("histImgG", histImgG)
    cv2.imshow("histImgR", histImgR)
    cv2.imshow('histImgS', histImgS)
    cv2.imshow("Img", ledoff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cpp_recognize():
    """ doc string """
    ledoff = cv2.imread('./image05/36.jpg')
    ledon = cv2.imread('./image05/37.jpg')
    diff = cv2.subtract(ledon, ledoff)
    b, g, r = cv2.split(diff)
    s = cv2.add(b, g)
    _, maxval, _, _ = cv2.minMaxLoc(s)

    if maxval == 255:
        ratio = 0.95
    elif maxval > 180 and maxval < 255:
        ratio = 0.85
    elif maxval > 128 and maxval <= 180:
        ratio = 0.75
    elif maxval > 50 and maxval <= 128:
        ratio = 0.65
    else:
        ratio = 0.60

    print(maxval*ratio)

    _, binary = cv2.threshold(s, maxval*ratio, 255.0, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (23, 23))
    dilate = cv2.dilate(binary, kernel, None, None, 3)
    cv2.imshow('s', s)

    hist, _ = calc_and_draw_hist(s, [255, 255, 255])
    print(maxval)
    
    cv2.imshow('ledoff', ledoff)
    cv2.imshow('ledon', ledon)
    cv2.imshow('s', s)
    cv2.imshow('hist of s', hist)
    cv2.imshow('binary', binary)
    cv2.imshow('dilate', dilate)
    cv2.waitKey(0)


def adaptive_threshold():
    """ doc string """
    ledoff = cv2.imread('./image01/303.jpg')
    ledon = cv2.imread('./image01/304.jpg')
    diff = cv2.subtract(ledon, ledoff)
    b, g, r = cv2.split(diff)
    s = cv2.add(b, g)

    binary = cv2.adaptiveThreshold(
        s, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
        19,  -50.)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (19, 19))
    dilate = cv2.dilate(binary, kernel)
    cv2.imshow('off', ledoff)
    cv2.imshow('on', ledon)
    cv2.imshow('s', s)
    cv2.imshow('binary', binary)
    cv2.imshow('dilate', dilate)
    cv2.waitKey(0)

def createCLAHE():
    """ doc string """
    ledoff = cv2.imread('./image01/303.jpg')
    ledon = cv2.imread('./image01/304.jpg')

    diff = cv2.subtract(ledon, ledoff)
    b, g, r = cv2.split(diff)
    s = cv2.add(b, g)
   
    clahe = cv2.createCLAHE(clipLimit=600.0, tileGridSize=(1,1))
    processed = clahe.apply(s)


    # r, g, b = cv2.split(ledon)
    # clahe = cv2.createCLAHE(clipLimit=600.0, tileGridSize=(1,1))
    # rclahe = clahe.apply(r)
    # gclahe = clahe.apply(g)
    # bclahe = clahe.apply(b)
    # processed = cv2.merge((rclahe, gclahe, bclahe))
    cv2.imshow('ledon', ledon)
    cv2.imshow('s', s)
    cv2.imshow('processed', processed)
    cv2.waitKey(0)
    
if __name__ == '__main__':
    # fun1()
    # equalizeHist()
    # show_hist()
    cpp_recognize()
    # createCLAHE()