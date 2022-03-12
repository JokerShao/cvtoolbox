""" Quaternion basic calculation

dtype: ndarray
shape: 1x4  w x y z order
author: zexi shao
email: zexishao@foxmail.com
"""
from math import sqrt
from numpy import empty


def quatconj(q):
    qconj = empty((1,4))
    qconj[0,0], qconj[0,1], qconj[0,2], qconj[0,3] = q[0,0], -q[0,1], -q[0,2], -q[0,3]
    return qconj

def quatinv(q):
    q0, q1, q2, q3 = q[0,0], q[0,1], q[0,2], q[0,3]
    norm2 = (q0*q0+q1*q1+q2*q2+q3*q3)
    qinv = empty((1,4))
    qinv[0,0], qinv[0,1], qinv[0,2], qinv[0,3] = q0/norm2, -q1/norm2, -q2/norm2, -q3/norm2
    return qinv

def quatnormalize(q):
    q0, q1, q2, q3 = q[0,0], q[0,1], q[0,2], q[0,3]
    norm = sqrt(q0*q0+q1*q1+q2*q2+q3*q3)
    return q/norm

def quatmultiply(q1, q2):
    sa, xa, ya, za = q1[0,0], q1[0,1], q1[0,2], q1[0,3]
    sb, xb, yb, zb = q2[0,0], q2[0,1], q2[0,2], q2[0,3]
    q = empty((1,4))
    q[0,0], q[0,1], q[0,2], q[0,3] = sa*sb-xa*xb-ya*yb-za*zb, \
                                    sa*xb+xa*sb+ya*zb-za*yb, \
                                    sa*yb-xa*zb+ya*sb+za*xb, \
                                    sa*zb+xa*yb-ya*xb+za*sb
    return q

def quatrotate(q, p):
    """ Note: This is different with matlab!

    p: [x y z] 3x1 vector
    use formula: p1 = q*p*q^-1    p1 = R * p
    """
    q0, q1, q2, q3 = q[0,0], q[0,1], q[0,2], q[0,3]
    norm = sqrt(q0*q0+q1*q1+q2*q2+q3*q3)
    q0, q1, q2, q3 = q0/norm, q1/norm, q2/norm, q3/norm
    x, y, z = p[0,0], p[1,0], p[2,0]

    p1 = empty((3,1))
    p1[0,0], p1[1,0], p1[2,0] = (1-2*q2*q2-2*q3*q3)*x + (2*q1*q2-2*q0*q3)*y + (2*q1*q3+2*q0*q2)*z, \
                                (2*q1*q2+2*q0*q3)*x + (1-2*q1*q1-2*q3*q3)*y + (2*q2*q3-2*q0*q1)*z, \
                                (2*q1*q3-2*q0*q2)*x + (2*q2*q3+2*q0*q1)*y + (1-2*q1*q1-2*q2*q2)*z
    return p1

