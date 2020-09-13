import numpy as np
from math import cos, sin
import time


def skew(v):
    """
    input 3x1 vector
    """
    return np.array([0,       -v[2,0], v[1,0] , \
                     v[2,0],  0,       -v[0,0], \
                     -v[1,0], v[0,0],  0      ]).reshape(3,3)



def axang2rotm(axang):
    """
    convert use rodrigues' formula
    [x y z theta] 1x4 vector, theta in radian
    """
    x, y, z, theta = axang[0,0], axang[0,1], axang[0,2], axang[0,3]
    ctheta, stheta = cos(theta), sin(theta)

    ctheta_d1 = 1-ctheta
    return np.array([ \
        ctheta+ctheta_d1*x*x, ctheta_d1*x*y-stheta*z, ctheta_d1*x*z+stheta*y, \
        ctheta_d1*y*x+stheta*z, ctheta+ctheta_d1*y*y, ctheta_d1*y*z-stheta*x, \
        ctheta_d1*z*x-stheta*y, ctheta_d1*z*y+stheta*x, ctheta+ctheta_d1*z*z]).reshape(3,3)


if __name__ == '__main__':

    axis = np.random.random((1,3))
    theta = np.random.random((1,1))
    axis = axis / np.linalg.norm(axis)

    axang = np.hstack((axis, theta))
    time.sleep(1)


    time_begin = time.time()
    for i in range(50000):
        R = axang2rotm(axang)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')


