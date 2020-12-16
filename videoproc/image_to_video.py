"""
read an image sequence to a video

avi file support list:
    I420: YUV uncompressed
    PIMI: MPEG-1 encoding
    XVID: MPEG-4 encoding

mp4 file support list:
    mp4v

flv file support list:
    flv1
"""
import numpy as np
import cv2


def imageseq2video( \
    img_prefix_path='./', vid_output_name='out.mp4', \
    img_type_name='png', start_idx=0, duration_num=75, \
    fps=24.0, vid_w=1920, vid_h=1080):
    """
    img_prefix_path 图像路径前缀
    vid_output_name 视频输出文件名
    start_idx 图像起始序号
    duration_num 图像持续帧数
    fps 输出视频帧率
    vid_w 输出视频宽度
    vid_h 输出视频高度
    """
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    vw = cv2.VideoWriter(vid_name, fourcc, fps, (vid_w, vid_h))

    for nn in range(duration_num):
        imgpath = img_prefix_path+str(start_idx+nn)+'.'+img_type_name
        print(nn)
        img = cv2.imread(imgpath)
        vw.write(img)

    vw.release()

def imageseq_merge2video( \
    img0_prefix_path='./img0/', img1_prefix_path='./img1/', \
    img_type_name='png', vid_output_name='out.mp4', \
    img0_start_idx=0, img1_start_idx=0, duration_num=75, \
    fps=24.0, vid_w=960, vid_h=1080):
    """
    合并对齐两幅图像，并压入视频文件
    img0_start_idx 源图像0 开始序号
    duration_num 持续帧数
    """
    # 合并后的缓存图像
    target = np.zeros((vid_h, vid_w, 3), dtype=np.uint8)

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    vw = cv2.VideoWriter(vid_output_name, fourcc, fps, (vid_w, vid_h))

    for nn in range(duration_num):
        srcpath0 = img0_prefix_path+str(nn+img0_start_idx)+'.'+img_type_name
        srcpath1 = img1_prefix_path+str(nn+img1_start_idx)+'.'+img_type_name
        src0 = cv2.imread(srcpath0)
        src1 = cv2.imread(srcpath1)
        src0_small = cv2.resize(src0, (vid_w, vid_h//2))
        src1_small = cv2.resize(src1, (vid_w, vid_h//2))

        target[0:vid_h//2, :, :] = src0_small
        target[vid_h//2:vid_h, :, :] = src1_small
        cv2.imshow('target', target)
        cv2.waitKey(1)
        print(nn+cnt)
        vw.write(target)
    vw.release()


if __name__ == '__main__':
    # videopath = 'video_aruco.mp4'
    # imgseqpath = 'imgs/'
    imageseq2video()

