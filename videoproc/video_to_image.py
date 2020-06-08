""" read a video file and write per image to disk. """
import numpy as np
import cv2

def video2imageseq(videopath, imgseqpath):
    """
    convert a video to a image sequence.
    """
    cnt = 0
    realindex = 0

    capture = cv2.VideoCapture(videopath)

    while True:
        retval, frame = capture.read()

        frame = cv2.resize(frame, (1920, 1080))

        if not retval:
            break
        # mod = cnt % 5
        # if cnt >= 804:
        cv2.imwrite(imgseqpath+'/'+str(cnt)+'.png', frame)
        # if cnt >= 1556:
            # break

        # if mod == 0 or mod == 3:
        # # if cnt % 2 == 0: # 取一半视频帧
        #     resizedframe = cv2.resize(frame, (1920, 1080))
        #     cv2.imwrite(imgseqpath+'/'+str(realindex)+'.jpg', resizedframe)
        #     realindex += 1
        cnt += 1
        print(cnt)
    capture.release()


if __name__ == '__main__':
    videopath = 'D:\\gitrepo\\cvtoolbox\\videoproc\\00041.MTS'
    imgseqpath = 'D:\\gitrepo\\cvtoolbox\\videoproc\\00041\\'

    video2imageseq(videopath, imgseqpath)
