import numpy as np


def normalize(vec):
    """ normalize a vector. """
    vec = np.array(vec, dtype=np.float64)
    return vec / np.linalg.norm(vec)

def quat2axang(q):
    """
    [w x y z] 1x4 vector
    [x y z theta] 1x4 rotation vector
    """
    q = q/np.sqrt(q[0,0]**2+q[0,1]**2+q[0,2]**2+q[0,3]**2)
    theta = np.arccos(q[0:1,0:1])*2
    axis = np.array([[1,0,0]]) if theta < 1e-10 else normalize(q[0:1,1:4] / np.sin(theta/2))
    return np.hstack((axis, theta))
