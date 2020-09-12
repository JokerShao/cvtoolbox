import numpy as np


def rotm2quat(R):
    """
    [w x y z] 1 x 4 vector
    """
    r11, r12, r13, r21, r22, r23, r31, r32, r33 = R.reshape(-1)

    q0 = np.sqrt(1+r11+r22+r33)/2
    q1 = (r32-r23)/(4*q0)
    q2 = (r13-r31)/(4*q0)
    q3 = (r21-r12)/(4*q0)

    if q0<1e-8:
        if max(r11,r22,r33) is r11:
            t = np.sqrt(1+r11-r22-r33)
            q0 = (r32-r23)/t
            q1 = t/4
            q2 = (r13+r31)/t
            q3 = (r12+r21)/t
            return np.array([[q0, q1, q2, q3]])
        elif max(r11,r22,r33) is r22:
            t = np.sqrt(1-r11+r22-r33)
            q0 = (r13-r31)/t
            q1 = (r12+r21)/t
            q2 = t/4
            q3 = (r32+r23)/t
            return np.array([[q0, q1, q2, q3]])
        elif max(r11, r22, r33) is r33:
            t = np.sqrt(r11-r22+r33)
            q0 = (r21-r12)/t
            q1 = (r13+r31)/t
            q2 = (r23-r32)/t
            q3 = t/4
            return np.array([[q0, q1, q2, q3]])

    return np.array([[q0, q1, q2, q3]])

