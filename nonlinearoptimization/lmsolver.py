"""
levenberg marquardt algorithm
see: https://www.cnblogs.com/lianjiehere/p/5956578.html

author:        Zexi Shao
date:          2020.05.30
last modify:   2020.06.15
"""
import numpy as np


def compute_jacobian(func, p, data, delta=1e-9):
    """
    p:   [N x 1]
    """
    N = p.shape[0]
    h = func(p, data).shape[0]
    J = np.zeros((h, N), dtype=np.float64)

    delta_x = p * delta
    for i in range(N):
        pp1, pp2 = p.copy(), p.copy()
        pp1[i, 0] = pp1[i, 0] - delta_x[i, 0]
        pp2[i, 0] = pp2[i, 0] + delta_x[i, 0]

        fx1 = func(pp1, data)
        fx2 = func(pp2, data)
        J[:, i:i+1] = (fx2 - fx1) / (2*delta_x[i, 0])

    return J

def levenberg_marquardt(func, x0, data, gtol=1e-15, xtol=1e-15, k_max=1e4, verbose=False):
    """
    : ftol
    """
    tau = 1e-5

    k = 0
    v = 2
    x = x0

    J = compute_jacobian(func, x, data)
    A = J.T @ J
    fx = func(x, data)
    g = J.T @ fx
    found = (np.max(np.abs(g)) <= gtol)
    mu = tau * np.max(np.diag(A))

    print('\n\t\t\t\t\t\tFirst-Order')
    print('Iteration\tFunc-count\tResidual\toptimality\tLambda\t\tNorm of step')
    while (not found) and (k < k_max):

        print('%9i\t%10i\t%.6e\t%.6e\t%.3e' %(k, (x0.shape[0]+1)*(k+1), (fx.T@fx)[0,0], np.abs(g).max(), mu))
        k = k+1

        h_lm = np.linalg.solve(A + mu*np.eye(A.shape[0]), -g)
        if np.linalg.norm(h_lm) < (xtol*(np.linalg.norm(x)+xtol)):
            found = True
        else:
            x_new = x + h_lm
            fx_new = func(x_new, data)
            rho = (fx.T@fx - fx_new.T@fx_new) / (-h_lm.T@J.T@fx - 0.5*h_lm.T@J.T@J@h_lm)
            if rho > 0:
                x = x_new.copy()
                J = compute_jacobian(func, x, data)
                fx = func(x, data)
                A = J.T@J
                g = J.T@fx
                found = (np.max(np.abs(g)) <= gtol)
                mu = mu * np.max((1/3, 1-(2*rho[0, 0]-1)**3))
                v = 2
            else:
                mu = mu*v
                v = 2*v

    return x
