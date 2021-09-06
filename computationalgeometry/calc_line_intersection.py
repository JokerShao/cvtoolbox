'''
author:      Zexi Shao
email:       zexishao@foxmail.com
date:        2021.09.06
last modify: 2021.09.06

'''
import numpy as np


def method1(P1, L1_norm, P2, L2_norm):
    '''
    reference: https://zhuanlan.zhihu.com/p/137563599
    '''
    x1, y1, z1 = P1[0,0], P1[1,0], P1[2,0]
    Lx1, Ly1, Lz1 = L1_norm[0,0], L1_norm[1,0], L1_norm[2,0]

    x2, y2, z2 = P2[0,0], P2[1,0], P2[2,0]
    Lx2, Ly2, Lz2 = L2_norm[0,0], L2_norm[1,0], L2_norm[2,0]

    t1 = (y1-y2-((x1*Ly2)/Lx2)+(x2*Ly2)/Lx2) / ((Lx1*Ly2)/Lx2-Ly1)
    # t2 = (x1+t1*Lx1-x2) / Lx2

    P = np.array([
        [x1+t1*Lx1],
        [x1+t1*Ly1],
        [z1+t1*Lz1]
    ])

    return P

def method2(P1, L1_norm, P2, L2_norm):
    '''
    refer: https://blog.csdn.net/xdedzl/article/details/86009147
    seems like something wrong.
    '''
    CA = P2 - P1 #P1 - P2
    vec_s1 = np.cross(L1_norm.T, L2_norm.T)
    vec_s2 = np.cross(CA.T, L2_norm.T)

    return np.dot(vec_s1, vec_s2.T) * L1_norm

def method3():
    ''' doc string '''
    pass


if __name__ == '__main__':

    P1 = [0, 0, 0]
    L1 = [1, 1, 1]

    P2 = [1, 0, 0]
    L2 = [-1, 1, 1]

    P1 = np.array(P1, dtype=np.float64).reshape(3,1)
    L1 = np.array(L1, dtype=np.float64).reshape(3,1)
    L1 = L1 / np.linalg.norm(L1)
    P2 = np.array(P2, dtype=np.float64).reshape(3,1)
    L2 = np.array(L2, dtype=np.float64).reshape(3,1)
    L2 = L2 / np.linalg.norm(L2)

    P_method1 = method1(P1, L1, P2, L2)
    print('P_method1:\n', P_method1)

    P_method2 = method2(P1, L1, P2, L2)
    print('P_method2:', P_method2)

    method3()

