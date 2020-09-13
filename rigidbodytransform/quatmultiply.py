import numpy as np
import time



def quatmultiply(q1, q2):
    sa, xa, ya, za = q1[0,0], q1[0,1], q1[0,2], q1[0,3]
    sb, xb, yb, zb = q2[0,0], q2[0,1], q2[0,2], q2[0,3]
    return np.array([sa*sb-xa*xb-ya*yb-za*zb,
                      sa*xb+xa*sb+ya*zb-za*yb,
                      sa*yb-xa*zb+ya*sb+za*xb,
                      sa*zb+xa*yb-ya*xb+za*sb]).reshape(1,4)



if __name__ == '__main__':

    q1 = np.random.random((1,4))
    q2 = np.random.random((1,4))
    time.sleep(1)

    time_begin = time.time()
    for i in range(500000):
        q_prod = quatmultiply(q1, q2)
    time_end = time.time()
    print((time_end-time_begin)*1000, 'ms')
