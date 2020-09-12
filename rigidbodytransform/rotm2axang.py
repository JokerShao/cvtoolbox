import numpy as np


def rotm2axang(R):
    """
    """
    r11, r12, r13, r21, r22, r23, r31, r32, r33 = R.flatten()
    theta = np.array([[np.arccos((r11+r22+r33-1)/2)]])
    axis = 1/(2*np.sin(theta)) * np.array([r32-r23,r13-r31,r21-r12])
    axis = axis/np.linalg.norm(axis)
    return np.hstack((axis, theta))
