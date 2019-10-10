import numpy as np
import cv2

def write_vid():
    """
    doc
    """
    cnt = 0
    empty_frame = np.ones((1080, 1920, 3), np.uint8) * 255

    # Define the codec and create VideoWriter object
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fourcc = cv2.VideoWriter_fourcc(*'MP42')
    out = cv2.VideoWriter('output.avi',fourcc, 24.0, (1920, 1080))

    while True:
        # frame = empty_frame.clone()
        frame = np.array(empty_frame, copy=True)
        
        cv2.putText(frame, str(cnt), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255, 255), 2)
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        out.write(frame)

        if cnt>= 24:
            break
        else:
            cnt+=1

    out.release()
    cv2.destroyAllWindows()

def read_vid():
    """
    doc
    """
    cap = cv2.VideoCapture('output.avi')
    cnt = 0
    while True:
        retval, frame = cap.read()

        if retval == False:
            break
        else:
            cv2.imshow('f', frame)
            cv2.waitKey(1)
            # cv2.imwrite('output/'+str(cnt)+'.jpg', frame)
            cnt+=1

    print(cnt)#应该等于239
    cap.release()

if __name__ == '__main__':
    write_vid()
    # read_vid()