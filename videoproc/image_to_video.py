""" read a image sequence to a video """
import numpy as np
import cv2

def video2imageseq(videopath, imgseqpath):
    """
    convert a video to a image sequence.
    """
    cnt = 0

    capture = cv2.VideoCapture(videopath)

    while True:
        retval, frame = capture.read()
        if not retval:
            break
        if cnt % 5 == 0: # 取一半视频帧
            cv2.imwrite(imgseqpath+'/'+str(cnt)+'.jpg', frame)
        cnt += 1
    capture.release()

# def imageseq2video(imgseqpath, videopath):
def imageseq2video():
    """ doc string """
    cnt = 165 # 图像开始序号
    number = 727 # 图像持续帧数

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    vw = cv2.VideoWriter('./out.mp4', fourcc, 24.0, (1920, 1080))

    for nn in range(number):
        imgpath = 'D:\\DataRepository\\greenscreen\\test2\\xushi\\Image2\\Map_YanShi.'+str(cnt+nn)+'.jpg'
        print(nn)
        img = cv2.imread(imgpath)
        vw.write(img)
    
    vw.release()

# def imageseq2video(imgseqpath, videopath):
def imageseq2video0():
    """ doc string """
    cnt = 956 # 图像开始序号
    number = 524 # 图像持续帧数

    target = np.zeros((1080, 960, 3), dtype=np.uint8)

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    vw = cv2.VideoWriter('./outsplit.avi', fourcc, 24.0, (960, 1080))

    for nn in range(number):
        srcpath = 'D:\\DataRepository\\greenscreen\\processed\\2019_09_29_primatte\\'+str(nn+cnt)+'src.png'
        dstpath = 'D:\\DataRepository\\greenscreen\\processed\\2019_09_29_primatte\\'+str(nn+cnt)+'dst.png'
        src = cv2.imread(srcpath)
        dst = cv2.imread(dstpath)
        src_small = cv2.resize(src, (960, 540))
        dst_small = cv2.resize(dst, (960, 540))

        target[0:540, :, :] = src_small
        target[540:1080, :, :] = dst_small

        cv2.imshow('target', target)
        cv2.waitKey(1)


        print(nn+cnt)
        # img = cv2.imread(imgpath)
        vw.write(target)
    vw.release()

if __name__ == '__main__':
    # videopath = 'E:\\P4Workspace\\calibration-package\\external_params\\00015.MTS'
    # imgseqpath = 'E:\\P4Workspace\\calibration-package\\external_params\\00015\\'

    # video2imageseq(videopath, imgseqpath)
    imageseq2video0()
