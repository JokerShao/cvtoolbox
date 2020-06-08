"""
Newton法
Rosenbrock函数
函数 f(x0,x1)=100*(x(2)-x(1).^2).^2+(1-x(1)).^2
梯度 g(x0,x1)=(-400*(x(2)-x(1)^2)*x(1)-2*(1-x(1)),200*(x(2)-x(1)^2))^(T)
"""
import numpy as np
import matplotlib.pyplot as plt


def jacobian(x):
    return np.array([2*x[0] + 2*x[1], 2*x[0]+2*x[1]])

def hessian(x):
    return np.array([[2, 2], [2, 2]])

# def jacobian(x):
#     return np.array([-400*x[0]*(x[1]-x[0]**2)-2*(1-x[0]),200*(x[1]-x[0]**2)])

# def hessian(x):
#     return np.array([[-400*(x[1]-3*x[0]**2)+2,-400*x[0]],[-400*x[0],200]])

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
        x = x + gamma * dk
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

X1=np.arange(-1.5,1.5+0.05,0.05)
X2=np.arange(-3.5,2+0.05,0.05)
[x1,x2]=np.meshgrid(X1,X2)
# f=100*(x2-x1**2)**2+(1-x1)**2 # 给定的函数
f=x1**2+2*x1*x2+x2**2
plt.contour(x1,x2,f,20) # 画出函数的20条轮廓线

x0 = np.array([-1.2,1])
epsilon = 1e-9  # 函数值变化精度
gamma=0.5  # dk系数
itera = 1e5

W=newton(x0, epsilon, gamma, itera)

plt.plot(W[0,:],W[1,:],'g*',W[0,:],W[1,:]) # 画出迭代点收敛的轨迹
plt.show()

