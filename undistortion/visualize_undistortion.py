'''
Visualization of lens distortion parameters

author:      Zexi Shao
email:       zexishao@foxmail.com
date:        2020.01.01
last modify: 2021.05.24
'''
import numpy as np
import cv2


def create_chessboard(
    square_size: int, rows: int, cols: int, img_w: int, img_h: int) -> np.ndarray:
    '''
    create a chessboard image
    '''
    white_square = np.ones((square_size, square_size), dtype=np.uint8) * 255
    img = np.zeros((square_size*rows, square_size*cols), np.uint8)

    for row in range(rows):
        for col in range(cols):
            if (row%2==0 and col%2!=0) or (row%2!=0 and col%2==0):
                img[row*square_size:(row+1)*square_size, col*square_size:(col+1)*square_size] = white_square

    return cv2.resize(img, (img_w, img_h))


if __name__ == '__main__':

    square_size = 300
    rows = 30
    cols = 35
    img_w = 1280
    img_h = 1024

    cc_list = [
        654.1191122027699, 513.8920502402475,
        660.0589343928767, 496.51008085415543,
        674.9887204529734, 517.6356475215772,
        626.1616637431905, 516.6590947191718
    ]
    fc_list = [
        718.2605378516567, 718.6665933175939,
        717.3247144096108, 717.7466889710198,
        716.9716974157338, 717.5509706420194,
        721.7478496553418, 722.0749895413956
    ]
    kc_list = [
        -0.3900235002982064, 0.19191070583863643, 0.0002004872316689393, 3.566717619031195e-06, -0.049755825330610425,
        -0.39404395359553757, 0.1981769069801459, -6.600361195023239e-05, -7.071938352896775e-05, -0.05271784213495665,
        -0.38786461374919706, 0.19049336957090807, 0.0005057500941721278, 0.000279233794051633, -0.04918156593236308,
        -0.3984076538010568, 0.21468532399715626, -4.0553804886494005e-05, -0.0003000560887336763, -0.06464536654692253
    ]
    cam_idx = 0

    cc_array = np.array(cc_list).reshape(4, 2)
    fc_array = np.array(fc_list).reshape(4, 2)
    kc_array = np.array(kc_list).reshape(4, 5)

    cx, cy = cc_array[cam_idx]
    fx, fy = fc_array[cam_idx]
    k1, k2, p1, p2, k3 = kc_array[cam_idx]

    K = np.array([[fx,  0, cx],
                 [ 0, fy, cy],
                 [ 0,  0,  1]])
    dist_coeffs = np.array([[k1, k2, p1, p2, k3]]).T
    print('cam_k:\n', K, '\n', 'dist_coeffs:\n', dist_coeffs)

    img = create_chessboard(square_size, rows, cols, img_w, img_h)
    undistortion = cv2.undistort(img, K, dist_coeffs)

    undistortion_small = cv2.resize(undistortion, (img_w//2, img_h//2))
    cv2.imshow('undistortion', undistortion_small)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

