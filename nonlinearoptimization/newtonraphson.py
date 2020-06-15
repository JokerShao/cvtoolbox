import numpy as np

from mylmsolver import levenberg_marquardt


def newton_raphson(X0, h, y, epslion=1e-8, max_iter=1e10):

    xk = X0.reshape(3,1)
    k = 0
    while k < max_iter:

        cost = 0
        H = np.zeros((3,3))
        b = np.zeros((3,1))

        for i in range(h.shape[0]):
            hi = h[i]
            yi = y[i]
            err = yi - func(xk, hi)

            J = compute_jacobian(xk, hi, yi)
            print(J)

            if np.linalg.norm(J) < epslion:
                return xk

            H += J.T @ J
            b += err * J.T

            cost += err**2

        dx = np.linalg.inv(H) @ b

        xk = xk+dx

        print('---------')
        print(cost)
        print(H)
        print(b)
        print(xk)
        print('')





        # print(gk)
        # # gkn = compute_jacobian_numerical(xk)
        # # print(gkn)

        # if abs(np.linalg.norm(gk)) < epslion:
        #     return xk

        # Hk = gk.T@gk
        # pk = -np.linalg.inv(Hk)@gk.T

        # xk = xk + np.mean(pk, 1)
        # k += 1
        


# def gradient_descent(x0):
#     epslion = 1e-8
#     max_iter = 1e10

#     xk = x0

#     k = 0
#     while k < max_iter:

#         fk = func(xk)
#         gk = compute_jacobian(xk)

#         if abs(gk) < epslion:
#             return x

#         pk = -gk

#         xk = xk + pk
#         # k += 1

#         # print('gk:', gk, 'fk1: ', fk1, ' xk1:', xk1)
#         # if abs(fk1-fk) < epslion:
#         #     return x

#         # xk1 = x - lambdaa*fk/gk
#         # fk1 = func(xk1)
        
#         # x = xk1
#         # k+=1

#     return x

def cost_f(x, h, y):
    return (func(x, h) - y)**2

def compute_jacobian(x, h, y):
    delta = 0.05

    # J = np.zeros((h.shape[0], x.shape[0]))
    J = np.zeros((1, x.shape[0]))

    for i in range(x.shape[0]):
        xx1 = x.copy()
        xx2 = x.copy()
        xx1[i] = xx1[i] - delta*xx1[i]
        xx2[i] = xx2[i] + delta*xx2[i]

        fx1 = func(xx1, h)
        fx2 = func(xx2, h)
        J[:, i] = (fx2-fx1) / ((xx2[i]-xx1[i])+1e-10)

    return J


def compute_jacobian_numerical(x):
    delta = 0.05
    x1 = x - x*delta
    x2 = x + x*delta

    gk = (func(x2) - func(x1)) / (x2 - x1)

    return gk

def cost(abc, data):
    h, y = data[0], data[1]
    fx = func(abc, h)
    # print(fx)
    # print(y)
    err = y - fx
    return err

def func(abc, x):
    a, b, c = abc
    fx = np.exp(a*x**2 + b*x + c)
    # print(fx)
    return fx


if __name__ == '__main__':

    # 测试优化算法用
    # 假设函数为
    #    f(x) = exp(a*x^2 + b*x + c)

    X_real = np.array([1, 2, 1], dtype=np.float64).reshape(3,1)
    X0 = np.array([1, 2, 2], dtype=np.float64).reshape(3,1)

    h = np.linspace(0, 1, 20).astype(np.float64).reshape(-1, 1)
    y = func(X_real, h).reshape(-1, 1)

    X = levenberg_marquardt(cost, X0, [h, y])
    print('X_real:\n', X_real.T)
    print('X0:\n', X0.T)
    print('X:\n', X.T)

    # xx = newton_raphson(X0, h, y, epslion=1e-8, max_iter=1e10)
    # print(xx)








"""
Newton's method, Convex Optimization P487

author:       Zexi Shao
date:         2020.06.02
last modify:  2020.06.02
"""
import numpy as np


def compute_jacobian(func, X, data):
    """
    X:   [N x 1]
    """
    N = X.shape[0]
    h = func(X, data).shape[0]
    J = np.zeros((h, N))

    delta = 0.005
    delta_x = X * delta
    for i in range(N):
        X1, X2 = X.copy(), X.copy()
        X1[i, 0] = X[i, 0] - delta_x[i, 0]
        X2[i, 0] = X[i, 0] + delta_x[i, 0]

        fx1 = func(X1, data)
        fx2 = func(X2, data)
        J[:, i:i+1] = (fx2 - fx1) / (2*delta_x[i, 0])

    return J

def newton_method(func, X0, data, tol=1e-15):
    """
    X0:     [N x 1]
    """
    









"""
Rosenbrock function
f(x0,x1)=100*(x(2)-x(1).^2).^2+(1-x(1)).^2
g(x0,x1)=(-400*(x(2)-x(1)^2)*x(1)-2*(1-x(1)),200*(x(2)-x(1)^2))^(T)
"""
import numpy as np
import matplotlib.pyplot as plt


# def jacobian(x):
#     return np.array([2*x[0] + 2*x[1], 2*x[0]+2*x[1]])

# def hessian(x):
#     return np.array([[2, 2], [2, 2]])

def jacobian(x):
    return np.array([-400*x[0]*(x[1]-x[0]**2)-2*(1-x[0]),200*(x[1]-x[0]**2)])

def hessian(x):
    return np.array([[-400*(x[1]-3*x[0]**2)+2,-400*x[0]],[-400*x[0],200]])

def newton(x0, epsilon=1e-7, gamma=1e-2, itera=1e5):
    #函数功能：利用牛顿法优化迭代找到最优解
    #输入：一个初始点(x0,x1)
    #输出：每次迭代的迭代点
    print('初始点为:')
    print(x0,'\n')
    W=np.zeros((2,int(itera)))
    k = 1
    W[:,0] = x0
    x = x0

    while k < itera:
        gk = jacobian(x)
        Hk = hessian(x)
        if np.linalg.norm(gk) < epsilon:
            break
        dk = -np.linalg.inv(Hk) @ gk.reshape(2,1)
        x = x + gamma * dk.reshape(2)
        W[:,k] = x
        k+=1
        #  and delta>TolX:
        # p = -np.dot(np.linalg.inv(hessian(x)),jacobian(x))
        # x0 = x
        # x = x + alpha*p
        # epsilon = sum((x-x0)**2)
        print('第', k, '次迭代结果:')
        print(x,'\n')
        # i=i+1
        # # W=W[:,0:i]  # 记录迭代点  
    return W


if __name__ == '__main__':

    X1=np.arange(-1.5,1.5+0.05,0.05)
    X2=np.arange(-3.5,2+0.05,0.05)
    [x1,x2]=np.meshgrid(X1,X2)
    # rosenbrock function
    f=(1-x1)**2 + 100*(x2-x1**2)**2

    plt.contour(x1,x2,f,20) # 画出函数的20条轮廓线

    x0 = np.array([-1.2,1.5])
    epsilon = 1e-9
    gamma=0.5  # dk coefficient
    itera = 1e5

    W=newton(x0, epsilon, gamma, itera)

    plt.plot(W[0,:],W[1,:],'g*',W[0,:],W[1,:]) # 画出迭代点收敛的轨迹
    plt.show()
