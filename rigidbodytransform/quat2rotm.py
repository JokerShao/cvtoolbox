import numpy as np


def quat2rotm(q):
    """ [w x y z] 1x4 vector """
    return np.array([ [1-2*q[0,2]**2-2*q[0,3]**2, 2*q[0,1]*q[0,2]-2*q[0,0]*q[0,3], 2*q[0,1]*q[0,3]+2*q[0,0]*q[0,2]],
                      [2*q[0,1]*q[0,2]+2*q[0,0]*q[0,3], 1-2*q[0,1]**2-2*q[0,3]**2, 2*q[0,2]*q[0,3]-2*q[0,0]*q[0,1]],
                      [2*q[0,1]*q[0,3]-2*q[0,0]*q[0,2], 2*q[0,2]*q[0,3]+2*q[0,0]*q[0,1], 1-2*q[0,1]**2-2*q[0,2]**2]])
