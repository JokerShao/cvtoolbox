# reference 
# http://zulko.github.io/blog/2013/09/27/read-and-write-video-frames-in-python-using-ffmpeg/
import numpy
import subprocess as sp
import cv2


FFMPEG_BIN = "ffmpeg" # on Linux ans Mac OS

command = [ FFMPEG_BIN,
            # '-i', 'template.mov',
            '-i', 'BOSSalpha.mov',
            '-f', 'image2pipe',
            '-pix_fmt', 'rgba',#a32',#24',
            '-vcodec', 'rawvideo', '-']
pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)

for i in range(1000):

    # read 420*360*3 bytes (= 1 frame)
    raw_image = pipe.stdout.read(1920*1080*4)#420*360*3)
    raw_image = pipe.stdout.read(1920*1080*4)#420*360*3)
    # transform the byte read into a numpy array
    image =  numpy.fromstring(raw_image, dtype='uint8')
    image = image.reshape((1080, 1920, 4)) #360,420,3))
    r = image[...,0]
    g = image[...,1]
    b = image[...,2]
    a = image[...,3]

    cv2.imshow('r', r)
    cv2.imshow('g', g)
    cv2.imshow('b', b)
    cv2.imshow('a', a)

    cv2.waitKey(1)



    # throw away the data in the pipe's buffer.
    pipe.stdout.__sizeof__()
    pipe.stdout.flush()

