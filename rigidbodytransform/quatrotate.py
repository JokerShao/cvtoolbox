import numpy as np


def quatrotate(q, p):
    """
    q: [w x y z] 1x4 vector
    p: [x y z] 3x1 vector
    use fomual : p1 = q*p*q^-1
    Note: This is different with matlab!
    """
    q = q/np.sqrt(q[0,0]**2+q[0,1]**2+q[0,2]**2+q[0,3]**2)
    return np.dot( \
                  np.array([ [1-2*q[0,2]**2-2*q[0,3]**2, 2*q[0,1]*q[0,2]-2*q[0,0]*q[0,3], 2*q[0,1]*q[0,3]+2*q[0,0]*q[0,2]],
                             [2*q[0,1]*q[0,2]+2*q[0,0]*q[0,3], 1-2*q[0,1]**2-2*q[0,3]**2, 2*q[0,2]*q[0,3]-2*q[0,0]*q[0,1]],
                             [2*q[0,1]*q[0,3]-2*q[0,0]*q[0,2], 2*q[0,2]*q[0,3]+2*q[0,0]*q[0,1], 1-2*q[0,1]**2-2*q[0,2]**2]]), \
                p)
