""" [w x y z] 1x4 vector """
import numpy as np
import time

from math import sqrt


def quatconj(q):
    return np.array([q[0,0], -q[0,1], -q[0,2], -q[0,3]]).reshape(1,4)

def quatinv(q):
    q0, q1, q2, q3 = q[0,0], q[0,1], q[0,2], q[0,3]
    norm = (q0*q0+q1*q1+q2*q2+q3*q3)
    return np.array([q0/norm, -q1/norm, -q2/norm, -q3/norm]).reshape(1,4)

def quatnormalize(q):
    q0, q1, q2, q3 = q[0,0], q[0,1], q[0,2], q[0,3]
    norm = sqrt(q0*q0+q1*q1+q2*q2+q3*q3)
    return q/norm

def quatmultiply(q1, q2):
    sa, xa, ya, za = q1[0,0], q1[0,1], q1[0,2], q1[0,3]
    sb, xb, yb, zb = q2[0,0], q2[0,1], q2[0,2], q2[0,3]
    return np.array([sa*sb-xa*xb-ya*yb-za*zb,
                      sa*xb+xa*sb+ya*zb-za*yb,
                      sa*yb-xa*zb+ya*sb+za*xb,
                      sa*zb+xa*yb-ya*xb+za*sb]).reshape(1,4)

def quatrotate(q, p):
    """
    q: [w x y z] 1x4 vector
    p: [x y z] 3x1 vector
    use fomual : p1 = q*p*q^-1
    Note: This is different with matlab!

    return np.dot( \
                  np.array([ 1-2*q2*q2-2*q3*q3, 2*q1*q2-2*q0*q3, 2*q1*q3+2*q0*q2, \
                             2*q1*q2+2*q0*q3, 1-2*q1*q1-2*q3*q3, 2*q2*q3-2*q0*q1, \
                             2*q1*q3-2*q0*q2, 2*q2*q3+2*q0*q1, 1-2*q1*q1-2*q2*q2]).reshape(3,3), \
                p)
    """
    q0, q1, q2, q3 = q[0,0], q[0,1], q[0,2], q[0,3]
    norm = sqrt(q0*q0+q1*q1+q2*q2+q3*q3)
    q0, q1, q2, q3 = q0/norm, q1/norm, q2/norm, q3/norm

    x, y, z = p[0,0], p[1,0], p[2,0]

    return np.array([ (1-2*q2*q2-2*q3*q3)*x + (2*q1*q2-2*q0*q3)*y + (2*q1*q3+2*q0*q2)*z, \
                    (2*q1*q2+2*q0*q3)*x + (1-2*q1*q1-2*q3*q3)*y + (2*q2*q3-2*q0*q1)*z, \
                    (2*q1*q3-2*q0*q2)*x + (2*q2*q3+2*q0*q1)*y + (1-2*q1*q1-2*q2*q2)*z]).reshape(3,1)



if __name__ == '__main__':

    q = np.random.random((1,4))
    q1 = np.random.random((1,4))
    q2 = np.random.random((1,4))

    q = np.random.random((1,4))
    p = np.random.random((3,1))
    time.sleep(1)

    time_begin = time.time()
    for i in range(500000):
        q_inv = quatinv(q)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')


    time_begin = time.time()
    for i in range(500000):
        q_normalized = quatnormalize(q)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')



    time_begin = time.time()
    for i in range(500000):
        q_prod = quatmultiply(q1, q2)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')



    time_begin = time.time()
    for i in range(200000):
        p_new = quatrotate(q, p)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')

