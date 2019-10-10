import math
import numpy as np

def angle2radian(angle):
    """doc"""
    return angle*np.pi/180

def radian2angle(radian):
    """doc"""
    return radian*180/np.pi

start_angle = np.arccos(-0.63)
print(radian2angle(start_angle))

disappear_angle = np.arccos(-0.9119)
print(radian2angle(disappear_angle))