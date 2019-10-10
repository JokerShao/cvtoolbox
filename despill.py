"""
despill color algorithm test
"""
import cv2
import numpy as np

def create_image():
    """
    test image channels order
    """
    image_4c = np.ones((720, 1280, 4), np.uint8) * 0
    b, g, r, a = image_4c[:,:,0], image_4c[:,:,1], image_4c[:,:,2], image_4c[:,:,3]
    # b += 255
    # g += 255
    # r += 255
    # a += 255

    cv2.imshow('image_4c', image_4c)
    cv2.imshow('alpha', a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def test_matrix_cat():
    val = 20
    idx = 220

    while True:
        mixed = cv2.imread(
            'E:\P4Workspace\Prj\Projects\CalculatorDllTest\proc\\processed_out_'+
            str(idx)+'.png', -1)
        idx+=1
        b, g, r, mask = mixed[:,:,0], mixed[:,:,1], mixed[:,:,2], mixed[:,:,3]

        cv2.imshow('mixed', mixed)
        cv2.imshow('mask', mask)

        for row in range(0, mixed.shape[0]):
            for col in range(0, mixed.shape[1]):
                if mask[row, col] == 255:
                    tempval = g[row, col]
                    res = min(255, max(0, g[row, col]-val))
                    ratio = res / tempval
                    b[row, col] = min(255, max(0, b[row, col]/ratio))
                    g[row, col] = res
                    r[row, col] = min(255, max(0, r[row, col]/ratio))

        cv2.imshow('mixed_sub_green_channels', mixed)
        cv2.waitKey(1)

def hsv_standardization(H, S, V):
    """
    convert opencv hsv format to standard format.
    from H(180), S(255), V(255) to H(360), S(0.0f-1.0f), V(0.0f-1.0f)

    convert to int, same as opencv
    """
    return int(H)*2, int(S)/255, int(V)/255

def hsv2rgb(H, S, V):
    """
    using standard hsv value, convert to RGB color space(0-255)
    """
    C = V * S
    Hdot = H / 60
    print('Hdot%2', Hdot%2)
    print('abs(Hdot%2-1)', abs(Hdot%2-1))
    print('1 - abs(Hdot%2-1)', 1 - abs(Hdot%2-1))
    X = C * (1 - abs(Hdot%2-1))

    print('mine hsv to rgb: C', C, 'H\'', Hdot, 'X', X)

    # if Hdot>=0 and Hdot<1:
    #     R, G, B = 0, 0, 0
    if Hdot>=0 and Hdot<1:
        R1, G1, B1 = C, X, 0
    elif Hdot>=1 and Hdot<2:
        R1, G1, B1 = X, C, 0
    elif Hdot>=2 and Hdot<3:
        R1, G1, B1 = 0, C, X
    elif Hdot>=3 and Hdot<4:
        R1, G1, B1 = 0, X, C
    elif Hdot>=4 and Hdot<5:
        R1, G1, B1 = X, 0, C
    elif Hdot>=5 and Hdot<6:
        R1, G1, B1 = C, 0, X

    m = V - C

    print('m:', m)
    print('R1:', R1, 'B1:', B1, 'G1', G1)
    R, G, B = R1+m, G1+m, B1+m

    print('before muti 255:', R, G, B)

    R = int(R*255)
    G = int(G*255)
    B = int(B*255)

    return R, G, B

def rgb2yuv(R, G, B):
    """
    convert image from rgb color space to yuv color space

    return value is float.
    """
    # Y = 0.299*R + 0.587*G + 0.114*B
    # U = -0.1687*R - 0.3313*G + 0.5*B + 128
    # V = 0.5*R - 0.4187*G - 0.0813*B + 128

    Y = 0.299*R + 0.587*G + 0.114*B
    # U = -0.147*R - 0.289*G + 0.436*B + 128
    # V = 0.615*R - 0.515*G - 0.100*B + 128

    # not clip
    U = -0.147*R - 0.289*G + 0.436*B
    V = 0.615*R - 0.515*G - 0.100*B

    # Y = round(Y)
    # U = round(U)
    # V = round(V)

    return Y, U, V

def create_colorful_image(R, G, B):
    """
    parameter R, G and B datatype is uint8
    """
    image_4c = np.ones((720, 1280, 4), np.uint8) * 0
    b, g, r, mask = image_4c[:,:,0], image_4c[:,:,1], image_4c[:,:,2], image_4c[:,:,3]
    b += B
    g += G
    r += R
    mask += 255

    return image_4c

def despill_algorithm0():
    """
    despill algorithm 0,
    test yuv hsv and rgb color space convert.
    """
    hd, sd, vd, hu, su, vu = 36, 23, 203, 55, 225, 255
    H_mid, S_mid, V_mid = (hd+hu)/2, (sd+su)/2, (vd+vu)/2

    my_hsv = np.ones((720, 1280, 3), np.uint8)*0
    my_hsv[:,:,0] = H_mid
    my_hsv[:,:,1] = S_mid
    my_hsv[:,:,2] = V_mid

    # opencv convert
    bgr_from_hsv_opencv = cv2.cvtColor(my_hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('bgr image convert from my_hsv use opencv', bgr_from_hsv_opencv)
    print('opencv convert:',
          bgr_from_hsv_opencv[0,0,0],
          bgr_from_hsv_opencv[0,0,1],
          bgr_from_hsv_opencv[0,0,2],
          )

    # my convert
    H, S, V = hsv_standardization(H_mid, S_mid, V_mid)
    R, G, B = hsv2rgb(H, S, V)
    print('my convert', B, G, R)

    bgr_from_hsv_mine = create_colorful_image(R, G, B)
    cv2.imshow('bgr image convert from my_hsv use mine', bgr_from_hsv_mine)
    cv2.waitKey(0)

def despill_algorithm1():
    """
    doc string
    """
    idx = 238
    mixed = cv2.imread(
        'E:\P4Workspace\Proj\Projects\CalculatorDllTest\proc\\processed_out_'+
        str(idx)+'.png', -1)
    mixed_small = cv2.resize(mixed, (1280, 720))
    b, g, r, mask = mixed_small[:,:,0], mixed_small[:,:,1], mixed_small[:,:,2], mixed_small[:,:,3]
    bgr = cv2.cvtColor(mixed_small, cv2.COLOR_BGRA2BGR)
    hsl = cv2.cvtColor(mixed_small, cv2.COLOR_BGR2HLS)
    h, s, l = hsl[:,:,0], hsl[:,:,1], hsl[:,:,2]

    h_val = 0
    s_val = 15
    l_val = -10

    for row in range(0, mixed_small.shape[0]):
        for col in range(0, mixed_small.shape[1]):
            if mask[row, col] == 255:
                h[row, col] -= h_val
                s[row, col] -= s_val
                # if s[row, col] <= 20:
                #     s[row, col] = 10
                # print(s[row, col])
                l[row, col] -= l_val

    bgr_fixed = cv2.cvtColor(hsl, cv2.COLOR_HLS2BGR)
    # cv2.imshow('mask', mask)
    cv2.imshow('mixed', mixed_small)
    cv2.imshow('bgr_fixed', bgr_fixed)
    cv2.waitKey(0)


def despill_algorithm2():
    """
    doc string
    """
    idx = 238
    mixed = cv2.imread(
        'E:\P4Workspace\Proj\Projects\CalculatorDllTest\proc\\processed_out_'+
        str(idx)+'.png', -1)
    mixed_small = cv2.resize(mixed, (1280, 720))
    b, g, r, mask = mixed_small[:,:,0], mixed_small[:,:,1], mixed_small[:,:,2], mixed_small[:,:,3]
    bgr = cv2.cvtColor(mixed_small, cv2.COLOR_BGRA2BGR)
    hsv = cv2.cvtColor(mixed_small, cv2.COLOR_BGR2HSV)
    h, s, v = hsv[:,:,0], hsv[:,:,1], hsv[:,:,2]

    h_val = 0
    s_val = -15
    v_val = 20

    for row in range(0, mixed_small.shape[0]):
        for col in range(0, mixed_small.shape[1]):
            if mask[row, col] == 255:
                h[row, col] -= h_val
                s[row, col] -= s_val
                # if s[row, col] <= 20:
                #     s[row, col] = 10
                # print(s[row, col])
                v[row, col] -= v_val

    bgr_fixed = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    # cv2.imshow('mask', mask)
    cv2.imshow('mixed', mixed_small)
    cv2.imshow('bgr_fixed', bgr_fixed)
    cv2.waitKey(0)

def test_func():
    h = 42
    s = 133
    v = 251
    print('source color: H', h, 'S', s, 'V', v)
    h_stand, s_stand, v_stand = hsv_standardization(h, s, v)
    print('standard hsv color:', h_stand, s_stand, v_stand)
    r, g, b = hsv2rgb(h_stand, s_stand, v_stand)
    print(b, g, r)

def test_func1():
    """
    pass    1763    95
    """
    bgr = cv2.imread('E:\\greenscreen\\girl.jpg')
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    print(hsv[95, 1763, :])
    

if __name__ == "__main__":
    # create_image()
    # test_matrix_cat()
    # test_func()
    # despill_algorithm0()
    test_func1()
