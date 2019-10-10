import numpy as np
import cv2

def test_func0():
    # cap = cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    imageidx = 6
    fs = cv2.FileStorage(
        'E:\\zexishao\\calibration_tool\\StereoMethod_PY\\sony_x280\\0_best.xml',
        cv2.FileStorage_READ)

    cam_mat = fs.getNode('M').mat()
    dist_coeff = fs.getNode('D').mat()

    I = np.eye(3)
    image_size = (1920, 1080)

    # 新相机的内参可选标志，指示在新摄像机矩阵中主点是否应位于图像中心。
    # 默认情况下，选择主点以使源图像的子集（由alpha确定）与校正图像最佳拟合。
    new_cam_mat0, roi0 = cv2.getOptimalNewCameraMatrix(cam_mat, dist_coeff, image_size, 0, image_size, 0)
    new_cam_mat1, roi1 = cv2.getOptimalNewCameraMatrix(cam_mat, dist_coeff, image_size, 1, image_size, 0)
    # 关于initUndistortRectifyMap函数：
    # @param cameraMatrix 标定结果中的内参数矩阵
    # @param distCoeffs 标定结果中的畸变矫正向量
    # @param R 原文：
    #     Also, this new camera is oriented differently
    #   in the coordinate space, according to R. That, 
    #   for example, helps to align two heads of a stereo 
    #   camera so that the epipolar lines on both images become
    #   horizontal and have the same y- coordinate
    #   (in case of a horizontally aligned stereo camera).
    # 意思是新相机相对于本相机的姿态，通常用在双摄标定中的极线矫正中,
    # 如果单纯为了生成畸变矫正表，传进来单位矩阵I就可以
    # @param newCameraMatrix 新相机的内参数，对于单目相机，可以传入
    # 原相机参数，或者使用getOptimalNewCameraMatrix来生成新的相机矩阵，
    # 以便更好的控制缩放。
    # @param size 新图像的大小
    # @param m1type 映射表数据类型
    # mapu0, mapv0 = cv2.initUndistortRectifyMap(cam_mat, dist_coeff, I, new_cam_mat0, image_size, cv2.CV_32FC1)
    # mapu1, mapv1 = cv2.initUndistortRectifyMap(cam_mat, dist_coeff, I, new_cam_mat1, image_size, cv2.CV_32FC1)
    mapu0, mapv0 = cv2.initUndistortRectifyMap(cam_mat, dist_coeff, I, cam_mat, image_size, cv2.CV_32FC1)
    mapu1, mapv1 = cv2.initUndistortRectifyMap(cam_mat, dist_coeff, I, cam_mat, image_size, cv2.CV_32FC1)

    img = cv2.imread('C:\\Users\\shaoz\\Desktop\\sony_x280\\'+str(imageidx)+'.jpg')
    corrected0 = cv2.remap(img, mapu0, mapv0, cv2.INTER_LINEAR)
    corrected1 = cv2.remap(img, mapu1, mapv1, cv2.INTER_LINEAR)
    undistorted = cv2.undistort(img, cam_mat, dist_coeff)

    x, y, w, h = roi1
    print(roi0)
    print(roi1)
    src_res = corrected1[y:y + h, x:x + w]
    after_resize_src_res = cv2.resize(src_res, image_size)

    cv2.imshow('remap, alpha = 0', corrected0)
    cv2.imshow('remap, alpha = 1', corrected1)
    cv2.imshow('roi1', src_res)
    cv2.imshow('after resize', after_resize_src_res)
    cv2.imshow('undistorted', undistorted)

    difference = cv2.subtract(corrected0, after_resize_src_res)
    cv2.imshow('differnece between alpha 0 and 1', difference)
    difference1 = cv2.subtract(corrected0, undistorted)
    cv2.imshow('difference between function remap and undistort', difference1)
    cv2.waitKey(0)

def onMouse(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDOWN: 
        cv2.circle(params[0], (x, y), 1, (0, 0, 255), -1)
        # cv2.putText(params[0], '('+str(x)+','+str(y)+')', (x, y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,  0.5, (0, 0, 255))
        params[1].append([float(x), float(y)])

def test_func1():
    """
    测试外参标定步骤中的2d点抓取，
    1. 读入原始图像，采集原始图像中的特征点（鼠标回调的方式）
    2. 将点进行畸变矫正，投影回畸变矫正后的图像空间
    3. 对图像进行畸变矫正
    4. 将第二步中算出来的点绘制到第三步的图像中
    """
    # src_img = cv2.imread('C:\\Users\\shaoz\\Desktop\\sony_x280\\2.jpg')
    src_img = cv2.imread('C:\\Users\\shaoz\\Desktop\\cam64\\rtsp2.jpg')
    cv2.namedWindow('src_img')
    params = [src_img, []]
    cv2.setMouseCallback('src_img', onMouse, params)
    while True:
        cv2.imshow('src_img', src_img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

    fs = cv2.FileStorage(
        # 'E:\\zexishao\\calibration_tool\\StereoMethod_PY\\sony_x280\\1.xml',
        'E:\\zexishao\\calibration_tool\\StereoMethod_PY\\192.168.1.64_fixed_pp\\2_best.xml',
        # 'E:\\zexishao\\calibration_tool\\StereoMethod_PY\\192.168.1.64-1\\3.xml',
        cv2.FileStorage_READ)

    cam_mat = fs.getNode('M').mat()
    dist_coeff = fs.getNode('D').mat()
    # image_size = (1920, 1080)
    image_size = (1280, 720)
    I = np.eye(3)
    new_cam_mat1, roi1 = cv2.getOptimalNewCameraMatrix(cam_mat, dist_coeff, image_size, 1, image_size, 0)
    # new_cam_mat0, roi0 = cv2.getOptimalNewCameraMatrix(cam_mat, dist_coeff, image_size, 0, image_size, 0)
    # mapu1, mapv1 = cv2.initUndistortRectifyMap(cam_mat, dist_coeff, I, new_cam_mat1, image_size, cv2.CV_32FC1)
    mapu1, mapv1 = cv2.initUndistortRectifyMap(cam_mat, dist_coeff, I, new_cam_mat1, image_size, cv2.CV_32FC1)

    I = np.eye(3)
    result = np.array([])
    print('\ncamera matrix:')
    print(cam_mat)
    print('\nnew_cam_mat1:')
    print(new_cam_mat1)
    # print('\nnew_cam_mat0:')
    # print(new_cam_mat0)
    # return 
    # result = cv2.undistortPoints(np.array([params[1]]), cam_mat, dist_coeff, None, I, new_cam_mat1)
    result = cv2.undistortPoints(np.array([params[1]]), cam_mat, dist_coeff, None, None, new_cam_mat1)
    corrected1 = cv2.remap(src_img, mapu1, mapv1, cv2.INTER_LINEAR)

    for pt in result[0]:
        # print(pt)
        cv2.circle(corrected1, (int(pt[0]), int(pt[1])), 3, (255, 0, 0), 1)
        cv2.putText(corrected1, '('+str(int(pt[0]))+','+str(int(pt[1]))+')', (int(pt[0]), int(pt[1]-20)), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (255, 0, 0))

    cv2.imshow('result', corrected1)
    cv2.waitKey(0)
    cv2.imwrite('./2.png', corrected1)

def test_fun2(num):
    """
    doc
    """

    # num = 1

    src_img = cv2.imread('E:\\greenscreen\\chessboard.png')

    fs = cv2.FileStorage(
        'E:\\zexishao\\CameraCalibrationToolkit\\intrinsic_params\\35mm\\1_best_no_coeff.xml',
        # 'E:\\zexishao\\CameraCalibrationToolkit\\intrinsic_params\\35mm\\'+str(num)+'.xml',
        cv2.FileStorage_READ)

    cam_mat = fs.getNode('M').mat()
    dist_coeff = fs.getNode('D').mat()
    image_size = (1920, 1080)
    I = np.eye(3)
    new_cam_mat1, roi1 = cv2.getOptimalNewCameraMatrix(cam_mat, dist_coeff, image_size, 1, image_size, 0)
    mapu1, mapv1 = cv2.initUndistortRectifyMap(cam_mat, dist_coeff, I, new_cam_mat1, image_size, cv2.CV_32FC1)

    I = np.eye(3)
    result = np.array([])
    print('\ncamera matrix:')
    print(cam_mat)
    print('\nnew_cam_mat1:')
    print(new_cam_mat1)
    # result = cv2.undistortPoints(np.array([params[1]]), cam_mat, dist_coeff, None, I, new_cam_mat1)
    # result = cv2.undistortPoints(np.array([params[1]]), cam_mat, dist_coeff, None, None, new_cam_mat1)
    corrected1 = cv2.remap(src_img, mapu1, mapv1, cv2.INTER_LINEAR)

    diff = cv2.subtract(src_img, corrected1)

    cv2.imshow('result', corrected1)
    # cv2.imshow('diff', diff)
    cv2.waitKey(0)
    # cv2.imwrite('E:\\zexishao\\CameraCalibrationToolkit\\intrinsic_params\\select1802\\cc'+str(num)+'.jpg', corrected1)


if __name__ == '__main__':
    # test_func0()
    # test_func1()

    for i in range(6):
        test_fun2(i)