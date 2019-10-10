import cv2

def see_esc_retval():
    """
    pass
    """
    cv2.namedWindow('ttt')
    retval = cv2.waitKey(0)
    print(retval)

if __name__ == '__main__':
    see_esc_retval()