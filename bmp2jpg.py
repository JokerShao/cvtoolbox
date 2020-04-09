import cv2

inputimg2 = '/media/zexi/3C3EEB943EEB460C/Users/zexi/MVS/Data/MV-CA013-20GC (00D76547524)/'
outputimg2 = '/media/zexi/3C3EEB943EEB460C/Users/zexi/MVS/Data/00D76547524/'

inputimg3 = '/media/zexi/3C3EEB943EEB460C/Users/zexi/MVS/Data/MV-CA013-20GC (00D76547604)/'
outputimg3 = '/media/zexi/3C3EEB943EEB460C/Users/zexi/MVS/Data/00D76547604/'

inputimg4 = '/media/zexi/3C3EEB943EEB460C/Users/zexi/MVS/Data/MV-CA013-20GC (00D76547675)/'
outputimg4 = '/media/zexi/3C3EEB943EEB460C/Users/zexi/MVS/Data/00D76547675/'

for i in range(1, 2661):
    print(i)
    img2 = cv2.imread(inputimg2+'Image_'+str(i)+'.bmp')
    cv2.imwrite(outputimg2+'Image_'+str(i)+'.jpg', img2)

    img3 = cv2.imread(inputimg3+'Image_'+str(i)+'.bmp')
    cv2.imwrite(outputimg3+'Image_'+str(i)+'.jpg', img3)

    img4 = cv2.imread(inputimg4+'Image_'+str(i)+'.bmp')
    cv2.imwrite(outputimg4+'Image_'+str(i)+'.jpg', img4)