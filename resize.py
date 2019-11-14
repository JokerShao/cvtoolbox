import cv2
import glob

pnglist = glob.glob('./JPEGImages/*.jpg')
pnglist.sort()

for pngfile in pnglist:
    src = cv2.imread(pngfile)
    dst = cv2.resize(src, (640, 480))
    cv2.imwrite(pngfile, dst)
    print(pngfile)
