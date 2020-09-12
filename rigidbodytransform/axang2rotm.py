import numpy as np


def skew(v):
    """
    input 3x1 vector
    """
    return np.array([[0,       -v[2,0], v[1,0] ],
                     [v[2,0],  0,       -v[0,0]],
                     [-v[1,0], v[0,0],  0      ]])

def axang2rotm(axang):
    """
    convert use rodrigues' formula
    [x y z theta] 1x4 vector, theta in radian
    """
    n = axang[0:1,0:3].T
    theta = axang[0:1,3:4]
    return np.cos(theta)*np.eye(3)+(1-np.cos(theta))*n*n.T+np.sin(theta)*skew(n)
