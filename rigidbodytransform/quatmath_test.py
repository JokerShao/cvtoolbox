import time
import numpy as np
from quatmath import \
    quatconj, quatinv, quatnormalize, \
    quatmultiply, quatrotate


if __name__ == '__main__':

    q = np.random.random((1,4))
    q1 = np.random.random((1,4))
    q2 = np.random.random((1,4))
    p = np.random.random((3,1))
    print('q', q)
    print('q1', q1)
    print('q2', q2)
    print('p', p)

    qconj = quatconj(q)
    print('qconj', qconj)

    qinv = quatinv(q)
    print('qinv', qinv)
    print(quatmultiply(qinv,q))

    qmultiply = quatmultiply(q1, q2)
    print('qmultiply', qmultiply)

    p1 = quatrotate(q, p)
    print('p1', p1)


    time.sleep(1)

    time_begin = time.time()
    for i in range(500000):
        q_inv = quatconj(q)
    time_end = time.time()
    print('average:', (time_end-time_begin)*1000/500000, 'ms')

    time_begin = time.time()
    for i in range(500000):
        q_inv = quatinv(q)
    time_end = time.time()
    print('average:', (time_end-time_begin)*1000/500000, 'ms')

    time_begin = time.time()
    for i in range(500000):
        q_normalized = quatnormalize(q)
    time_end = time.time()
    print('average:', (time_end-time_begin)*1000/500000, 'ms')

    time_begin = time.time()
    for i in range(500000):
        q_prod = quatmultiply(q1, q2)
    time_end = time.time()
    print('average:', (time_end-time_begin)*1000/500000, 'ms')

    time_begin = time.time()
    for i in range(500000):
        p_new = quatrotate(q, p)
    time_end = time.time()
    print('average:', (time_end-time_begin)*1000/500000, 'ms')

