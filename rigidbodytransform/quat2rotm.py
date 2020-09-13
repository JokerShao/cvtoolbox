import numpy as np
import time


def quat2rotm(q):
    """ [w x y z] 1x4 vector """
    q0, q1, q2, q3 = q[0,0], q[0,1], q[0,2], q[0,3]
    return np.array([ 1-2*q2*q2-2*q3*q3, 2*q1*q2-2*q0*q3, 2*q1*q3+2*q0*q2,
                      2*q1*q2+2*q0*q3, 1-2*q1*q1-2*q3*q3, 2*q2*q3-2*q0*q1,
                      2*q1*q3-2*q0*q2, 2*q2*q3+2*q0*q1, 1-2*q1*q1-2*q2*q2]).reshape(3,3)


if __name__ == '__main__':

    q = np.random.random((1,4))
    time.sleep(1)

    time_begin = time.time()
    for i in range(500000):
        R = quat2rotm(q)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')
