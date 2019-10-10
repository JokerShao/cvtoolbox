import cv2
import numpy as np

def spilt_vid():
    """
    split video file
    """
    vid_width = 1920
    vid_height = 1080
    vid_frame_rate = 24.0
    vid_in_path = 'E:\\greenscreen\\vid\\hair_fixedIso_output.mp4'
    vid_out_path = 'E:\\greenscreen\\vid\\hair_fixedIso_output_cut.mp4'
    start_frameID = 192
    end_frameID = 624
    
    # Initialize a video capture.
    capture = cv2.VideoCapture(vid_in_path)
    # Define the codec and create VideoWriter object
    output = cv2.VideoWriter(vid_out_path, -1, vid_frame_rate, (vid_width,vid_height))

    current_num = 0
    while True:
        if not (current_num % 10):
            print('processed', current_num, 'frame')
        retval, frame = capture.read()
        if not retval:
            break
        if current_num >= start_frameID:
            cv2.imshow('Record frame', frame)
            cv2.waitKey(1)
            output.write(frame)
        if current_num >= end_frameID:
            break
        current_num += 1

    capture.release()
    output.release()


if __name__ == '__main__':
    """ call main function. """
    spilt_vid()

