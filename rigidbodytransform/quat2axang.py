import numpy as np
import time
from math import sqrt, acos, sin


def normalize(vec):
    """ normalize a vector. """
    vec = np.array(vec, dtype=np.float64)
    return vec / np.linalg.norm(vec)



def quat2axang(q):
    """
    [w x y z] 1x4 vector
    [x y z theta] 1x4 rotation vector
    """
    q0, q1, q2, q3 = q[0,0], q[0,1], q[0,2], q[0,3]
    norm = q0*q0+q1*q1+q2*q2+q3*q3
    q0, q1, q2, q3 = q0/norm, q1/norm, q2/norm, q3/norm
    theta = acos(q0)*2
    if theta < 1e-10:
        return np.array([1,0,0,0]).reshape(1,4)
    else:
        sth = sin(theta/2)
        x, y, z = q1 / sth, q2 / sth, q3 / sth
        norm = sqrt(x*x+y*y+z*z)
        return np.array([x/norm, y/norm, z/norm, theta]).reshape(1,4)




if __name__ == '__main__':

    q = np.random.random((1,4))
    time.sleep(1)


    time_begin = time.time()
    for i in range(50000):
        axang = quat2axang(q)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')
