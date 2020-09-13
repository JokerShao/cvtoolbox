import numpy as np
import time


def quatinv(q):
    """ [w x y z] 1x4 vector """
    q0, q1, q2, q3 = q[0,0], q[0,1], q[0,2], q[0,3]
    norm = (q0*q0+q1*q1+q2*q2+q3*q3)
    return np.array([q0/norm, -q1/norm, -q2/norm, -q3/norm]).reshape(1,4)




if __name__ == '__main__':

    q = np.random.random((1,4))
    time.sleep(1)

    time_begin = time.time()
    for i in range(500000):
        q_inv = quatinv(q)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')

