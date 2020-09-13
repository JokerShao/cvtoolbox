import numpy as np
import time
from math import sin, cos


def axang2quat(axang):
    """
    [x y z theta] 1x4 rotation vector
    [w x y z] 1x4 vector
    """
    x, y, z, theta = axang[0,0], axang[0,1], axang[0,2], axang[0,3]
    sth = sin(theta/2)
    return np.array([cos(theta/2), x*sth, y*sth, z*sth]).reshape(1,4)


if __name__ == '__main__':

    axis = np.random.random((1,3))
    theta = np.random.random((1,1))
    axis = axis / np.linalg.norm(axis)

    axang = np.hstack((axis, theta))
    time.sleep(1)

    time_begin = time.time()
    for i in range(500000):
        R = axang2quat(axang)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')
