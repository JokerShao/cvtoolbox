"""
Rigid body basic transform, convert between axis angle,
rotation matrix and quaternion.
dtype: ndarray

q shape:     1x4  w x y z     order
axang shape: 1x4  x y z theta order
rvec shape:  1x3  x y z       order
R is right multiply matrix, for example:  p1 = R * p

author: zexi shao
email: zexishao@foxmail.com
"""
from math import sqrt, sin, cos, acos
from numpy import empty


def rotm2quat(R):
    r11, r12, r13 = R[0,0], R[0,1], R[0,2]
    r21, r22, r23 = R[1,0], R[1,1], R[1,2]
    r31, r32, r33 = R[2,0], R[2,1], R[2,2]

    q = empty((1,4))
    q0 = sqrt(1+r11+r22+r33)/2
    if q0<1e-8:
        if max(r11,r22,r33) is r11:
            t = sqrt(1+r11-r22-r33)
            q[0,0], q[0,1], q[0,2], q[0,3] = (r32-r23)/t, t/4, (r13+r31)/t, (r12+r21)/t
        elif max(r11,r22,r33) is r22:
            t = sqrt(1-r11+r22-r33)
            q[0,0], q[0,1], q[0,2], q[0,3] = (r13-r31)/t, (r12+r21)/t, t/4, (r32+r23)/t
        else:
            t = sqrt(r11-r22+r33)
            q[0,0], q[0,1], q[0,2], q[0,3] = (r21-r12)/t, (r13+r31)/t, (r23-r32)/t, t/4
    else:
        q[0,0], q[0,1], q[0,2], q[0,3] = q0, (r32-r23)/(4*q0), (r13-r31)/(4*q0), (r21-r12)/(4*q0)
    return q

def quat2rotm(q):
    q0, q1, q2, q3 = q[0,0], q[0,1], q[0,2], q[0,3]
    R = empty((3,3))
    R[0,0], R[0,1], R[0,2], R[1,0], R[1,1], R[1,2], R[2,0], R[2,1], R[2,2] = \
        1-2*q2*q2-2*q3*q3, 2*q1*q2-2*q0*q3, 2*q1*q3+2*q0*q2, \
        2*q1*q2+2*q0*q3, 1-2*q1*q1-2*q3*q3, 2*q2*q3-2*q0*q1, \
        2*q1*q3-2*q0*q2, 2*q2*q3+2*q0*q1, 1-2*q1*q1-2*q2*q2
    return R

def quat2axang(q):
    q0, q1, q2, q3 = q[0,0], q[0,1], q[0,2], q[0,3]
    norm = q0*q0+q1*q1+q2*q2+q3*q3
    q0, q1, q2, q3 = q0/norm, q1/norm, q2/norm, q3/norm
    theta = acos(q0)*2

    axang = empty((1,4))
    if theta < 1e-10:
        axang[0,0], axang[0,1], axang[0,2], axang[0,3] = 1,0,0,0
    else:
        sth = sin(theta/2)
        x, y, z = q1/sth, q2/sth, q3/sth
        norm = sqrt(x*x+y*y+z*z)
        axang[0,0], axang[0,1], axang[0,2], axang[0,3] = x/norm, y/norm, z/norm, theta
    return axang

def axang2quat(axang):
    x, y, z, theta = axang[0,0], axang[0,1], axang[0,2], axang[0,3]
    sth = sin(theta/2)
    q = empty((1,4))
    q[0,0], q[0,1], q[0,2], q[0,3] = cos(theta/2), x*sth, y*sth, z*sth
    return q

def axang2rotm(axang):
    """ convert use rodrigues' formula """
    x, y, z, theta = axang[0,0], axang[0,1], axang[0,2], axang[0,3]
    ctheta, stheta = cos(theta), sin(theta)
    ctheta_d1 = 1-ctheta

    R = empty((3,3))
    R[0,0], R[0,1], R[0,2], R[1,0], R[1,1], R[1,2], R[2,0], R[2,1], R[2,2] = \
        ctheta+ctheta_d1*x*x, ctheta_d1*x*y-stheta*z, ctheta_d1*x*z+stheta*y, \
        ctheta_d1*y*x+stheta*z, ctheta+ctheta_d1*y*y, ctheta_d1*y*z-stheta*x, \
        ctheta_d1*z*x-stheta*y, ctheta_d1*z*y+stheta*x, ctheta+ctheta_d1*z*z
    return R

def rotm2axang(R):
    r11, r12, r13, r21, r22, r23, r31, r32, r33 = \
        R[0,0], R[0,1], R[0,2], \
        R[1,0], R[1,1], R[1,2], \
        R[2,0], R[2,1], R[2,2]
    theta = acos((r11+r22+r33-1)/2)
    tmp = 1/(2*sin(theta))
    x, y, z = tmp*(r32-r23), tmp*(r13-r31), tmp*(r21-r12)
    norm = sqrt(x*x+y*y+z*z)
    axang = empty((1,4))
    axang[0,0], axang[0,1], axang[0,2], axang[0,3] = x/norm, y/norm, z/norm, theta
    return axang

def rvec2axang(rvec):
    x, y, z = rvec[0,0], rvec[0,1], rvec[0,2]
    theta = sqrt(x*x+y*y+z*z)
    axang = empty((1,4))
    axang[0,0], axang[0,1], axang[0,2], axang[0,3] = \
        x/theta, y/theta, z/theta, theta
    return axang

def axang2rvec(axang):
    x, y, z, theta = axang[0,0], axang[0,1], axang[0,2], axang[0,3]
    rvec = empty((1,3))
    rvec[0,0], rvec[0,1], rvec[0,2] = x*theta, y*theta, z*theta
    return rvec

def rvec2rotm(rvec):
    x, y, z = rvec[0,0], rvec[0,1], rvec[0,2]
    theta = sqrt(x*x+y*y+z*z)
    x, y, z = x/theta, y/theta, z/theta
    ctheta, stheta = cos(theta), sin(theta)
    ctheta_d1 = 1-ctheta

    R = empty((3,3))
    R[0,0], R[0,1], R[0,2], R[1,0], R[1,1], R[1,2], R[2,0], R[2,1], R[2,2] = \
        ctheta+ctheta_d1*x*x, ctheta_d1*x*y-stheta*z, ctheta_d1*x*z+stheta*y, \
        ctheta_d1*y*x+stheta*z, ctheta+ctheta_d1*y*y, ctheta_d1*y*z-stheta*x, \
        ctheta_d1*z*x-stheta*y, ctheta_d1*z*y+stheta*x, ctheta+ctheta_d1*z*z
    return R

def rotm2rvec(R):
    r11, r12, r13, r21, r22, r23, r31, r32, r33 = \
        R[0,0], R[0,1], R[0,2], \
        R[1,0], R[1,1], R[1,2], \
        R[2,0], R[2,1], R[2,2]
    theta = acos((r11+r22+r33-1)/2)
    tmp = 1/(2*sin(theta))
    x, y, z = tmp*(r32-r23), tmp*(r13-r31), tmp*(r21-r12)
    rvec = empty((1,3))
    rvec[0,0], rvec[0,1], rvec[0,2] = x*theta, y*theta, z*theta
    return rvec

def quat2rvec(q):
    q0, q1, q2, q3 = q[0,0], q[0,1], q[0,2], q[0,3]
    norm = q0*q0+q1*q1+q2*q2+q3*q3
    q0, q1, q2, q3 = q0/norm, q1/norm, q2/norm, q3/norm
    theta = acos(q0)*2

    rvec = empty((1,3))
    if theta < 1e-10:
        rvec[0,0], rvec[0,1], rvec[0,2] = 1,0,0
    else:
        sth = sin(theta/2)
        x, y, z = q1/sth, q2/sth, q3/sth
        rvec[0,0], rvec[0,1], rvec[0,2]= x*theta, y*theta, z*theta
    return rvec

def rvec2quat(rvec):
    x, y, z = rvec[0,0], rvec[0,1], rvec[0,2]
    theta = sqrt(x*x+y*y+z*z)
    sht = sin(theta/2)
    q = empty((1,4))
    q[0,0], q[0,1], q[0,2], q[0,3] = cos(theta/2), x/theta*sht, y/theta*sht, z/theta*sht
    return q

def skew(v):
    """ input 3x1 vector """
    pass
    # return np.array([0,       -v[2,0], v[1,0] , \
    #                  v[2,0],  0,       -v[0,0], \
    #                  -v[1,0], v[0,0],  0      ]).reshape(3,3)
