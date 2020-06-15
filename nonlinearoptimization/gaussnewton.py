"""
Gauss Newton method

author:       Zexi Shao
date:         2020.06.12
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

def gauss_newton(func, X0, data, alpha=1e-1, ftol=1e-15, xtol=1e-15, max_iter=1e10, verbose=False):

    k = 0
    X = X0

    err_last = 1e9

    while k < max_iter:
        err = func(X, data)
        J = compute_jacobian(func, X, data)
        if np.linalg.norm(J) == 0:
            return X

        H = J.T@J
        B = -(J.T@err)

        delta_x = np.linalg.inv(H)@B #np.linalg.solve(H, B)
        delta_err = np.linalg.norm(err_last-err)

        if verbose:
            print('Iteration: %6i     Residual: %13f'%(k, np.linalg.norm(err)), '    X:', X.T, '    delta_x:', delta_x.T)
        if np.linalg.norm(delta_x) < xtol:
            return X
        if delta_err < ftol:
            return X

        k = k+1
        X = X + delta_x
        err_last = err

    return X
    