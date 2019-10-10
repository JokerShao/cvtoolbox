import numpy as np
import cv2

row = 669
col = 234
imagepath = ''

image = cv2.imread(imagepath)
print('B G R order:', image[row][col])
print('BGR Color Space Coordinate:', image[row][col]/255.0*400.0)

print(115/255, 145/255, 93/255)
print(95/255, 135/255, 82/255)