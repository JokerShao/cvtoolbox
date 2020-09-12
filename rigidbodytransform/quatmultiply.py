import numpy as np


def quatmultiply(q1, q2):
    sa, xa, ya, za = q1.flatten()
    sb, xb, yb, zb = q2.flatten()
    return np.array([[sa*sb-xa*xb-ya*yb-za*zb,
                      sa*xb+xa*sb+ya*zb-za*yb,
                      sa*yb-xa*zb+ya*sb+za*xb,
                      sa*zb+xa*yb-ya*xb+za*sb]])
