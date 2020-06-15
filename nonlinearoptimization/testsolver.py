import numpy as np

from gradientdescent import gradient_descent
from gaussnewton import gauss_newton
from lmsolver import levenberg_marquardt


def cost(X, data):
    x1, x2 = X
    _ = data

    err = (1-x1)**2 + 100*(x2-x1**2)**2
    return np.array(err).reshape(1,1)


if __name__ == '__main__':

    # rosenbrock function
    # f=(1-x1)**2 + 100*(x2-x1**2)**2
    x0 = np.array([1, 1.1]).reshape(2,1)

    # x_gd = gradient_descent(cost, x0, '', t=1e-3, ftol=1e-7, xtol=1e-7, verbose=True)
    x_gn = gauss_newton(cost, x0, '', ftol=1e-7, xtol=1e-7, verbose=True)
    # x_lm = levenberg_marquardt(cost, x0, '')

    # print(x_gd)
    print(x_gn)
    # print(x_lm)
    print('')

