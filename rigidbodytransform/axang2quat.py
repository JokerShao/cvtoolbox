import numpy as np


def axang2quat(axang):
    """
    [x y z theta] 1x4 rotation vector
    [w x y z] 1x4 vector
    """
    axis = axang[0:1,0:3]
    theta = axang[0:1,3:4]
    sht = np.sin(theta/2)
    return np.hstack((np.cos(theta/2), axis*sht))