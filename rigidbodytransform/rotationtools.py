import math
import numpy as np


def quat2euler(quat):
	""" doc """
	# YZX
	quat = np.array(quat)
	w, x, y, z = quat
	r11 = w*w + x*x - y*y - z*z
	r12 = 2 * (x*y + w*z)
	r13 = 2 * (x*z - w*y)
	r22 = w*w - x*x + y*y - z*z
	r32 = 2 * (y*z - w*x)

	# x: pitch; y: yaw; z: roll
	if (r12 > 0.99999):
		r12 = 1 if r12 > 1 else r12
		Ex = 0
		Ey = 2 * math.atan2(x, w)
		Ez = math.asin(r12)
		
		if (Ey > np.pi):
			Ey -= 2*np.pi
		elif (Ey < -np.pi):
			Ey += 2*np.pi
	elif (r12 < -0.99999):
		r12 = -1 if r12 < (-1) else r12
		Ex = 0
		Ey = -2 * math.atan2(x, w)
		Ez = math.asin(r12)
		if (Ey > np.pi):
			Ey -= 2*np.pi
		elif (Ey < -np.pi):
			Ey += 2*np.pi
	else:
		Ex = math.atan2(-r32, r22)
		Ey = math.atan2(-r13, r11)
		Ez = math.asin(r12)
	
	E = np.array([Ex, Ey, Ez])
	euler_angle = E * 180 / np.pi
	return euler_angle

def euler2quat(euler_angle):
	"""
	这是YZX顺序的QtoEuler 和EulertoQ，是测试没问题的，旋转角度任意
	X:pitch,Y:yaw,Z,roll;对应咱们的坐标系
	"""	
	# YZX
	euler_angle = np.array(euler_angle)
	E = euler_angle * np.pi / 180
	# Pitch: E[0]  Yaw:E[1]  Roll:E[2]
	CP = math.cos(E[0] / 2)
	SP = math.sin(E[0] / 2)
	CY = math.cos(E[1] / 2)
	SY = math.sin(E[1] / 2)
	CR = math.cos(E[2] / 2)
	SR = math.sin(E[2] / 2)

	w = CP * CY * CR - SP * SY * SR
	x = SP * CY * CR + CP * SY * SR
	y = CP * SY * CR + SP * CY * SR
	z = CP * CY * SR - SP * SY * CR
	
	return np.array([w, x, y, z])


def normalize(vec):
    """ normalize a vector. """
    vec = np.array(vec, dtype=np.float64)
    return vec / np.linalg.norm(vec)



if __name__ == '__main__':
    q = np.array([10, 2, 35, 4])
    q_norm = normalize(q)
    # Axis, Theta = quat2axisangle(q_norm)
    # rvec = quat2rvec(q_norm)
    # q_res = rvec2quat(rvec)

    print('quat:', q)
    print('quat_norm:', q_norm)
    # print('axis:', Axis, ' theta:', Theta)
    # print('rvec:', rvec)
    # print('q_res:', q_res)
