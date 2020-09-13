import numpy as np
from quat2rotm import quat2rotm
from rotm2quat import rotm2quat
from quatnormalize import quatnormalize
from quatmultiply import quatmultiply
from axang2rotm import axang2rotm, axang2rotm1
from quatconj import quatconj
from quatinv import quatinv
from quatrotate import quatrotate
from quat2axang import quat2axang
from axang2quat import axang2quat
from rotm2axang import rotm2axang

import cv2


# A = np.random.random((3,3))
# R, _ = np.linalg.qr(A)

# R = np.array([ [  -0.7150,    0.6875,    0.1273],
#                [ -0.3626 ,  -0.2089 ,  -0.9083],
#                [ -0.5978 ,  -0.6955 ,   0.3986]])

# print (R)

# q = rotm2quat(R)

# print (q)


# q = np.array([[ 0.3445  ,  0.1544  ,  0.5262  , -0.7620]])
# R = quat2rotm(q)

# print (R)


# axang = np.array([1, 2, 3, np.pi/3]).reshape(4,1)

# R = axang2rotm(axang)
# print(R)

# vv = 
# Rcv = cv2.Rodrigues(axang.flatten())

# # print (skew(np.array([[1,2,3]]).T))


# print('testing axang -> rotation matrix')
# print('================================')
# for i in range(1000):
#     n = np.random.random((1,3))
#     theta = np.random.random((1,1))
#     n_norm = n / np.linalg.norm(n)

#     vv = n_norm*theta
#     v = np.hstack((n_norm, theta))
#     print(v)

#     R, _ = cv2.Rodrigues(vv)
#     print(R)

#     R2 = axang2rotm(v)
#     print(R2)

#     diff = max(abs(R-R2).flatten())
#     if diff >= 1e-15:
#         print(diff)

# print('testing quatconj')
# print('================================')
# q = np.random.random((1,4))
# print(q)
# q_conj = quatconj(q)
# print(q_conj)

# print('testing quatinv')
# print('================================')
# q = np.random.random((1,4))
# print(q)
# q_inv = quatinv(q)
# print(q_inv)

# print('testing quatnormalize')
# print('================================')
# q = np.random.random((1,4))
# print(q)
# q_normalized = quatnormalize(q)
# print(q_normalized)

# print('testing quatmulply')
# print('================================')
# q1 = np.random.random((1,4))
# q2 = np.random.random((1,4))
# print(q1)
# print(q2)
# q_prod = quatmultiply(q1,q2)
# print(q_prod)

# print('testing quatrotate')
# print('================================')
# q = np.array([[0.43966648, 0.92258157, 0.90543036, 0.53108706]])#np.random.random((1,4))
# p = np.array([[0.90910111], [0.54535892], [0.68015601]])#np.random.random((3,1))
# print(q)
# print(p)
# p_rotated = quatrotate(q, p)
# print(p_rotated)

# print('testing quat2axang')
# print('================================')
# q = np.random.random((1,4))
# print(q)
# axang = quat2axang(q)
# print(axang)

# print('testing axang2quat')
# print('================================')
# axis = np.random.random((1,3))
# axis = axis / np.linalg.norm(axis)
# theta = np.random.random((1,1))
# axang = np.hstack((axis, theta))
# print(axang)
# q = axang2quat(axang)
# print(q)

# print('testing quat2rotm')
# print('================================')
# q = np.array([[1, 0, 0, 0]])#np.random.random((1,4))
# q = q/np.linalg.norm(q)
# print(q)
# R = quat2rotm(q)
# print(R)

# axang = quat2axang(q)
# R1 = axang2rotm(axang)
# print(R1)

# cv_axang = axang[0:1,0:3]*axang[0,3:4]
# R2, _ = cv2.Rodrigues(cv_axang)
# print(R2)

# A_f = np.array([[0,0,1]]).T
# axis = np.array([[1,0,0]])
# theta = np.array([[np.pi/2]])

# vv = axis*theta
# v = np.hstack((axis, theta))

# R, _ = cv2.Rodrigues(vv)
# print(R, '\n')

# R1 = axang2rotm(v)
# print(R1, '\n')

# q = axang2quat(v)
# print(q, '\n')

# R2 = quat2rotm(q)
# print(R2, '\n')


# R_wc = np.array([[1, 0, 0],
#                  [0, 0, 1],
#                  [0, -1, 0]], dtype=np.float64)


# # P_c = np.array([[0,0,1]],dtype=np.float64).T

# # print(R_wc@P_c)

# # q = rotm2quat(R_wc)

# # print(quat2rotm(q))

# # print(quatrotate(rotm2quat(R_wc), P_c))

# axang = rotm2axang(R_wc)
# axang1, _ = cv2.Rodrigues(R_wc)

# print(axang)
# print(axang1)




A = np.random.random((3,3))
R, _ = np.linalg.qr(A)


# R = np.array([[-0.8296004  , 0.5419175  ,-0.13449387],
#               [-0.25247174 ,-0.57891778 ,-0.77531427],
#               [-0.49801726 ,-0.60924513 , 0.61708928]] )

print(R, '\n')


Rtoquat = rotm2quat(R)
print(Rtoquat, '\n')

quattoaxang = quat2axang(Rtoquat)
print(quattoaxang, '\n')

axangtorotm = axang2rotm(quattoaxang)
print(axangtorotm, '\n')

# axangtorotm1 = axang2rotm1(quattoaxang)
# print(axangtorotm1, '\n')

rotmtoaxang = rotm2axang(axangtorotm)
print(rotmtoaxang, '\n')

axangtoquat = axang2quat(rotmtoaxang)
print(axangtoquat, '\n')

quattorotm = quat2rotm(axangtoquat)
print(quattorotm, '\n')

