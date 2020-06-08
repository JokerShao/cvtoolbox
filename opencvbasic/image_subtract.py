import cv2

def tt1():

    num = 2459

    while True:
        if num >= 3420:
            break
        image1 = cv2.imread(
        'E:\\P4Workspace\\Proj\\Projects\\CalculatorDllTest'+
            '\\stable-pixelpos-closelight\\1\\Frames\\image_'+str(num)+'.jpg')

        image2 = cv2.imread(
        'E:\\P4Workspace\\Proj\\Projects\\CalculatorDllTest'+
            '\\stable-pixelpos-closelight\\1\\Frames\\image_'+str(num+1)+'.jpg')

        gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

        blur1 = cv2.GaussianBlur(gray1, (11, 11), 2.0)
        blur2 = cv2.GaussianBlur(gray2, (11, 11), 2.0)
        # blur1 = cv2.blur(gray1, (3, 3))
        # blur2 = cv2.blur(gray2, (3, 3))

        subtract21 = cv2.subtract(blur1, blur2)
        _, bin = cv2.threshold(subtract21, 1, 255, cv2.THRESH_BINARY)
        # gray = cv2.cvtColor(subtract21, cv2.COLOR_BGR2GRAY)
        # blur = cv2.blur(gray, (5, 5))
        # _, bin = cv2.threshold(gray, 2, 255, cv2.THRESH_BINARY)
        # _, blur_bin = cv2.threshold(blur, 2, 255, cv2.THRESH_BINARY)
        cv2.putText(bin, str(num), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255))
        # cv2.namedWindow('subtract21', 1)
        cv2.imshow('subtract', subtract21)
        cv2.imshow('blur1', blur1)
        cv2.imshow('blur2', blur2)
        # cv2.imshow('grayscale', gray)
        # cv2.imshow('blur', blur)
        cv2.imshow('binary', bin)
        # cv2.imshow('blur_binary', blur_bin)
        cv2.waitKey(1)
        num+=1
    # subtract32 = cv2.subtract(image3, image2)
    # subtract43 = cv2.subtract(image4, image3)

    # cv2.namedWindow('subtract32', 1)
    # cv2.namedWindow('subtract43', 1)
    # cv2.imshow('subtract32', subtract32)
    # cv2.imshow('subtract43', subtract43)



def tt3():
    """ doc string """
    cnt = 14053

    
    while True:
        img1path = 'E:\\P4Workspace\\ORB_SLAM2_Windows\\LocalizationModeTest\\Frames\\image_'+str(cnt)+'.jpg'
        img2path = 'E:\\P4Workspace\\ORB_SLAM2_Windows\\LocalizationModeTest\\Frames\\image_'+str(cnt+1)+'.jpg'
        img1 = cv2.imread(img1path)
        img2 = cv2.imread(img2path)
        diff12 = cv2.subtract(img1, img2)
        gray12 = cv2.cvtColor(diff12, cv2.COLOR_BGR2GRAY)
        diff21 = cv2.subtract(img2, img1)
        gray21 = cv2.cvtColor(diff21, cv2.COLOR_BGR2GRAY)
        _, bin12 = cv2.threshold(gray12, 1, 255, cv2.THRESH_BINARY)
        _, bin21 = cv2.threshold(gray21, 1, 255, cv2.THRESH_BINARY)

        bin12sm = cv2.resize(bin12, (960, 540))
        bin21sm = cv2.resize(bin21, (960, 540))
        cv2.putText(bin12sm, str(cnt), (50, 50), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 255, 255), 5)

        cv2.imshow('bin12', bin12sm)
        # cv2.imshow('bin21', bin21sm)
        cv2.waitKey(1)
        cnt+=1

if __name__ == "__main__":
    tt3()