import numpy as np
import time


def quatconj(q):
    """ [w x y z] 1x4 vector """
    return np.array([q[0,0], -q[0,1], -q[0,2], -q[0,3]]).reshape(1,4)

