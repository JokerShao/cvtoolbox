"""
convert quaternion to others.
"""
import math
import numpy as np


def normalize(vec):
    """ normalize a vector. """
    vec = np.array(vec, dtype=np.float64)
    return vec / np.linalg.norm(vec)

def quat2axisangle(q):
    """
    input a normalized quaternion, return axis angle
    """
    q = normalize(q)
    theta = math.acos(q[0]) * 2
    axis = normalize(q[1:] / math.sin(theta/2))

    return axis, theta

def quat2rvec(q):
    """
    input a normalized quaternion, return rotation vector
    """
    q = normalize(q)
    axis, theta = quat2axisangle(q)

    return axis*theta

def rvec2quat(rvec):
    """
    input a rotation vector, return quaternion
    """
    rvec = np.array(rvec, dtype=np.float64)
    theta = np.linalg.norm(rvec)
    axis = rvec / theta
    sht = math.sin(theta/2)

    return np.append(math.cos(theta/2), axis*sht)


if __name__ == '__main__':
    q = np.array([10, 2, 35, 4])
    q_norm = normalize(q)
    Axis, Theta = quat2axisangle(q_norm)
    rvec = quat2rvec(q_norm)
    q_res = rvec2quat(rvec)

    print('quat:', q)
    print('quat_norm:', q_norm)
    print('axis:', Axis, ' theta:', Theta)
    print('rvec:', rvec)
    print('q_res:', q_res)
