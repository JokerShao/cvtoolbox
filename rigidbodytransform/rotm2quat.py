import numpy as np
from math import sqrt
import time

def rotm2quat(R):
    """
    [w x y z] 1 x 4 vector
    """
    r11, r12, r13 = R[0,0], R[0,1], R[0,2]
    r21, r22, r23 = R[1,0], R[1,1], R[1,2]
    r31, r32, r33 = R[2,0], R[2,1], R[2,2]

    q0 = sqrt(1+r11+r22+r33)/2
    q1 = (r32-r23)/(4*q0)
    q2 = (r13-r31)/(4*q0)
    q3 = (r21-r12)/(4*q0)

    if q0<1e-8:
        if max(r11,r22,r33) is r11:
            t = sqrt(1+r11-r22-r33)
            return np.array([(r32-r23)/t, t/4, (r13+r31)/t, (r12+r21)/t]).reshape(1,4)
        elif max(r11,r22,r33) is r22:
            t = sqrt(1-r11+r22-r33)
            return np.array([(r13-r31)/t, (r12+r21)/t, t/4, (r32+r23)/t]).reshape(1,4)
        elif max(r11, r22, r33) is r33:
            t = sqrt(r11-r22+r33)
            return np.array([(r21-r12)/t, (r13+r31)/t, (r23-r32)/t, t/4]).reshape(1,4)

    return np.array([q0, q1, q2, q3]).reshape(1,4)



if __name__ == '__main__':

    A = np.random.random((3,3))
    R, _ = np.linalg.qr(A)
    time.sleep(1)



    time_begin = time.time()
    for i in range(500000):
        axang = rotm2quat(R)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')
