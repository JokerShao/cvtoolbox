""" module doc string """
import numpy as np
import cv2

def create_corner(corner_size, gamma_correction=True):
    """ doc string """
    if corner_size % 2:
        corner_size += 1
    # grayscale full white image
    white_image = np.ones((corner_size, corner_size, 1), np.float32)

    radius = corner_size / 2
    center_x = center_y = radius - 1
    for upos in np.arange(0, corner_size-1):
        for vpos in np.arange(0, corner_size-1):
            if (upos<=center_x and vpos<=center_y) or (upos>center_x and vpos>center_y):
                distance = np.sqrt((upos-center_x)**2 + (vpos-center_y)**2)
                white_image[upos, vpos] = min(distance/radius, 1)
    if gamma_correction:
        return cv2.pow(white_image, 2.2)
    else:
        return white_image


if __name__ == "__main__":
    corner = create_corner(1080)

    cv2.imshow('corner', corner)
    # cv2.imwrite('./corner.jpg', corner*255)
    cv2.waitKey(0)
