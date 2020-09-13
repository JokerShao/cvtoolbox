import numpy as np
import time
from math import acos, sin, sqrt,  sin, cos


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


def quat2rotm(q):
    """ [w x y z] 1x4 vector """
    q0, q1, q2, q3 = q[0,0], q[0,1], q[0,2], q[0,3]
    return np.array([ 1-2*q2*q2-2*q3*q3, 2*q1*q2-2*q0*q3, 2*q1*q3+2*q0*q2,
                      2*q1*q2+2*q0*q3, 1-2*q1*q1-2*q3*q3, 2*q2*q3-2*q0*q1,
                      2*q1*q3-2*q0*q2, 2*q2*q3+2*q0*q1, 1-2*q1*q1-2*q2*q2]).reshape(3,3)


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


def axang2quat(axang):
    """
    [x y z theta] 1x4 rotation vector
    [w x y z] 1x4 vector
    """
    x, y, z, theta = axang[0,0], axang[0,1], axang[0,2], axang[0,3]
    sth = sin(theta/2)
    return np.array([cos(theta/2), x*sth, y*sth, z*sth]).reshape(1,4)


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
    


def skew(v):
    """
    input 3x1 vector
    """
    return np.array([0,       -v[2,0], v[1,0] , \
                     v[2,0],  0,       -v[0,0], \
                     -v[1,0], v[0,0],  0      ]).reshape(3,3)





if __name__ == '__main__':

    A = np.random.random((3,3))
    R, _ = np.linalg.qr(A)

    q = np.random.random((1,4))

    axis = np.random.random((1,3))
    theta = np.random.random((1,1))
    axis = axis / np.linalg.norm(axis)
    axang = np.hstack((axis, theta))

    time.sleep(1)

    time_begin = time.time()
    for i in range(500000):
        axang = rotm2quat(R)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')

    time_begin = time.time()
    for i in range(500000):
        axang = quat2axang(q)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')

    time_begin = time.time()
    for i in range(500000):
        R = axang2rotm(axang)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')

    time_begin = time.time()
    for i in range(500000):
        axang = rotm2axang(R)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')

    time_begin = time.time()
    for i in range(500000):
        R = axang2quat(axang)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')

    time_begin = time.time()
    for i in range(500000):
        R = quat2rotm(q)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')
