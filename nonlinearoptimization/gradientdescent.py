"""
Gradient descent method, Convex Optimization P466
see: https://zhuanlan.zhihu.com/p/66192821

author:       Zexi Shao
date:         2020.06.02
last modify:  2020.06.12
"""
import numpy as np


def compute_jacobian(func, X, data, delta=1e-9):
    """
    X:   [N x 1]
    """
    N = X.shape[0]
    h = func(X, data).shape[0]
    J = np.zeros((h, N), dtype=np.float64)

    delta_x = X * delta
    for i in range(N):
        X1, X2 = X.copy(), X.copy()
        X1[i, 0] = X[i, 0] - delta_x[i, 0]
        X2[i, 0] = X[i, 0] + delta_x[i, 0]

        fx1 = func(X1, data)
        fx2 = func(X2, data)
        J[:, i:i+1] = (fx2 - fx1) / (2*delta_x[i, 0])

    return J

def gradient_descent(func, X0, data, t=1e-2, ftol=1e-15, xtol=1e-15, max_iter=1e10, verbose=False):
    """
    X0:     [N x 1]
    """
    k = 0
    X = X0

    while k < max_iter:
        k = k+1

        J = compute_jacobian(func, X, data)
        err = func(X, data)
        delta_x = -t * J.T

        if verbose:
            print('Iteration: %6i     Residual: %13f'%(k, np.linalg.norm(err)), '    X:', X.T, '    delta_x:', delta_x.T)
        if np.linalg.norm(err) < ftol:
            return X
        if np.linalg.norm(delta_x) < xtol:
            return X

        X = X + delta_x

    return X
