import time
import numpy as np
from rigidtransform import \
    rotm2quat, quat2rotm, axang2quat, \
    quat2axang, axang2rotm, rotm2axang, \
    rvec2axang, rvec2quat, rvec2rotm, \
    axang2rvec, quat2rvec, rotm2rvec
from quatmath import quatrotate

import cv2


if __name__ == '__main__':

    A = np.random.random((3,3))
    R, _ = np.linalg.qr(A)
    p = np.random.random((3,1))

    print('R:\n', R, '\n')

    Rtoquat = rotm2quat(R)
    print('Rtoquat:\n', Rtoquat, '\n')

    quattoaxang = quat2axang(Rtoquat)
    print('quattoaxang:\n', quattoaxang, '\n')

    axangtorotm = axang2rotm(quattoaxang)
    print('axangtorotm:\n', axangtorotm, '\n')

    rotmtoaxang = rotm2axang(axangtorotm)
    print('rotmtoaxang:\n', rotmtoaxang, '\n')

    axangtoquat = axang2quat(rotmtoaxang)
    print('axangtoquat:\n', axangtoquat, '\n')

    quattorotm = quat2rotm(axangtoquat)
    print('quattorotm:\n', quattorotm, '\n')

    p1 = R@p
    print('p1\n', p1, '\n')

    p2 = quatrotate(axangtoquat, p)
    print('p2\n', p2, '\n')

    # test rvec
    rvec = np.random.random((1,3))
    print('rvec:\n', rvec)

    rvectoaxang = rvec2axang(rvec)
    print('rvectoaxang\n', rvectoaxang)
    axangtorvec = axang2rvec(rvectoaxang)
    print('axangtorvec:\n', axangtorvec)

    rvectoquat = rvec2quat(rvec)
    print('rvectoquat:\n', rvectoquat)
    quattorvec = quat2rvec(rvectoquat)
    print('quattorvec:\n', quattorvec)

    rvectorotm = rvec2rotm(rvec)
    print('rvectortm:\n', rvectorotm)
    rotmtorvec = rotm2rvec(rvectorotm)
    print('rotmtorvec:\n', rotmtorvec)

    rvectorotm_cv, _ = cv2.Rodrigues(rvec)
    print('rvectorotm_cv:\n', rvectorotm_cv)


    time.sleep(1)

    time_begin = time.time()
    for i in range(500000):
        axang = rotm2quat(R)
    time_end = time.time()
    print('average:', (time_end-time_begin)*1000/500000, 'ms')

    time_begin = time.time()
    for i in range(500000):
        axang = quat2axang(Rtoquat)
    time_end = time.time()
    print('average:', (time_end-time_begin)*1000/500000, 'ms')

    time_begin = time.time()
    for i in range(500000):
        R = axang2rotm(quattoaxang)
    time_end = time.time()
    print('average:', (time_end-time_begin)*1000/500000, 'ms')

    time_begin = time.time()
    for i in range(500000):
        axang = rotm2axang(axangtorotm)
    time_end = time.time()
    print('average:', (time_end-time_begin)*1000/500000, 'ms')

    time_begin = time.time()
    for i in range(500000):
        R = axang2quat(rotmtoaxang)
    time_end = time.time()
    print('average:', (time_end-time_begin)*1000/500000, 'ms')

    time_begin = time.time()
    for i in range(500000):
        R = quat2rotm(axangtoquat)
    time_end = time.time()
    print('average:', (time_end-time_begin)*1000/500000, 'ms')

