import numpy as np
from math import acos, sin, sqrt
import time



def rotm2axang(R):
    """
    """
    r11, r12, r13, r21, r22, r23, r31, r32, r33 = R.reshape(-1)
    theta = acos((r11+r22+r33-1)/2)
    tmp = 1/(2*sin(theta))
    x = tmp * (r32-r23)
    y = tmp * (r13-r31)
    z = tmp * (r21-r12)
    norm = sqrt(x*x+y*y+z*z)
    return np.array([x/norm, y/norm, z/norm, theta]).reshape(1,4)
    

if __name__ == '__main__':

    A = np.random.random((3,3))
    R, _ = np.linalg.qr(A)
    time.sleep(1)

    time_begin = time.time()
    for i in range(50000):
        axang = rotm2axang3(R)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')