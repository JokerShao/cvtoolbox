import numpy as np


def quatinv(q):
    """ [w x y z] 1x4 vector """
    return np.array([[q[0,0], -q[0,1], -q[0,2], -q[0,3]]]) / \
        (q[0,0]**2+q[0,1]**2+q[0,2]**2+q[0,3]**2)
