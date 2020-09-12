import numpy as np
from math import sqrt


def quatnormalize(q):
    """ [w x y z] 1x4 vector """
    return q/sqrt(q[0,0]**2+q[0,1]**2+q[0,2]**2+q[0,3]**2)
