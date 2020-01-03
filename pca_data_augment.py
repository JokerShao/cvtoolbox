from PIL import Image
from numpy import *
# from pylab import *

path = '/home/zexi/rubiks_cube/LINEMOD/rubikscube/JPEGImages/000001.jpg'

def pca(X):
    num_data, dim = X.shape  # 获取维数
    mean_X = X.mean(axis=0)  # 数据中心化
    X = X - mean_X

    if dim > num_data:
          # 使用紧致技巧
        M = dot(X, X.T)  # 协方差矩阵
        e, EV = linalg.eight(M)  # 特征值和特征向量
        tmp = dot(X.T, EV)  # 紧致技巧
        V = tmp[::-1]  # 由于最后的特征向量是我们所需要的，所以要将其逆转
        S = sqrt(e)[::-1]  # 由于特征值是按照递增顺序排列的，所以需要将其逆转
        for i in range(V.shape[1]):
            V[:, i] /= S
    else:
        U, S, V = linalg.svd(X)
    V = V[:num_data]  # 仅仅返回前num_data维的数据才合理

    return V, S, mean_X