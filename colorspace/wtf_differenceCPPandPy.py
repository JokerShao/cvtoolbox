import cv2
import numpy as np

def evaluate(real_image3c, dst_image):
    """
    两个三通道图片作差，比较均值和标准差，评估相似性
    """
    eval_ans = list()

    sub_ansAB = cv2.subtract(real_image3c, dst_image)
    sub_ansBA = cv2.subtract(dst_image, real_image3c)
    sub_ansTotal = cv2.add(sub_ansAB, sub_ansBA)
    mean, stddev = cv2.meanStdDev(sub_ansTotal)

    eval_ans += [x for x in mean[:, 0]]
    eval_ans += [0.0] # 为灰度图像留出空间
    eval_ans += [x for x in stddev[:, 0]]
    eval_ans += [0.0]

    sub_ansTotalGray = cv2.cvtColor(sub_ansTotal, cv2.COLOR_BGR2GRAY)
    mean, stddev = cv2.meanStdDev(sub_ansTotalGray)
    
    # 这个是根据图片通道数来的，和c++版本不太一样 没有多余的alpha通道
    eval_ans[3] = mean[0, 0]
    eval_ans[7] = stddev[0, 0]

    print('\nmean B G R Gray stdDev B G R Gray:\n', eval_ans[:4], '__', eval_ans[4:])

def evaluate1c(real_image, dst_image):
    """
    两个单通道图片作差，比较均值和标准差，评估相似性
    """
    eval_ans = list()

    sub_ansAB = cv2.subtract(real_image, dst_image)
    sub_ansBA = cv2.subtract(dst_image, real_image)
    sub_ansTotal = cv2.add(sub_ansAB, sub_ansBA)
    mean, stddev = cv2.meanStdDev(sub_ansTotal)

    # 这个是根据图片通道数来的，和c++版本不太一样 没有多余的alpha通道
    eval_ans.append(mean[0, 0])
    eval_ans.append(stddev[0, 0])

    # print('single channel image:', eval_ans)

# 入口函数
if __name__ == "__main__":

    image_size = (1080, 1920)

    # Load sample image
    img_bgr = cv2.imread("D:\\DataRepository\\greenscreen\\mountain.jpg")

    cv2.imshow("original", img_bgr)

    # Convert from BGR to YUV
    img_yuv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YUV)

    # Converting directly back from YUV to BGR results in an (almost) identical image
    img_bgr_restored = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    cv2.imshow("converted by yuv", img_bgr_restored)

    evaluate(img_bgr, img_bgr_restored)
    diff = img_bgr.astype(np.int16) - img_bgr_restored
    print("mean/stddev diff (BGR => YUV => BGR)", np.mean(diff), np.std(diff))

    # Create YUYV from YUV
    y0 = np.expand_dims(img_yuv[...,0][::,::2], axis=2)
    u = np.expand_dims(img_yuv[...,1][::,::2], axis=2)
    y1 = np.expand_dims(img_yuv[...,0][::,1::2], axis=2)
    v = np.expand_dims(img_yuv[...,2][::,::2], axis=2)
    img_yuyv = np.concatenate((y0, u, y1, v), axis=2)
    img_yuyv_cvt = img_yuyv.reshape(img_yuyv.shape[0], img_yuyv.shape[1] * 2, int(img_yuyv.shape[2] / 2))

    # Convert back to BGR results in more saturated image.
    img_bgr_restored = cv2.cvtColor(img_yuyv_cvt, cv2.COLOR_YUV2BGR_YUYV)
    cv2.imshow("converted by yuyv", img_bgr_restored)

    evaluate(img_bgr, img_bgr_restored)
    diff = img_bgr.astype(np.int16) - img_bgr_restored
    print("mean/stddev diff (BGR => YUV => YUYV => BGR)", np.mean(diff), np.std(diff))

    ########################################
    # --------------------------
    # 插值算法计算yuv后转回BGR
    y, uv = cv2.split(img_yuyv_cvt)

    # 显示原始 UV值
    cv2.imshow('u', u)
    cv2.imshow('v', v)

    local_image_y = cv2.imread('./cpumatY_convert_by_gpu.bmp', -1)
    local_image_u = cv2.imread('./cpumatU_convert_by_gpu.bmp', -1)
    local_image_v = cv2.imread('./cpumatV_convert_by_gpu.bmp', -1)
    local_image_ucpu = cv2.imread('./cpumatU_convert_by_cpu.bmp', -1)
    local_image_vcpu = cv2.imread('./cpumatV_convert_by_cpu.bmp', -1)

    # 立方插值
    tm = cv2.TickMeter()
    tm.start()
    interpolation_u = cv2.resize(u, (1920, 1080), interpolation=cv2.INTER_CUBIC)
    # interpolation_u = cv2.resize(u, (1920, 1080), interpolation=cv2.INTER_LINEAR)
    tm.stop()
    # print(tm.getTimeMilli())
    interpolatino_v = cv2.resize(v, (1920, 1080), interpolation=cv2.INTER_CUBIC)
    # interpolatino_v = cv2.resize(v, (1920, 1080), interpolation=cv2.INTER_LINEAR)
    cv2.imshow('interpolation_u', interpolation_u)
    cv2.imshow('interpolatino_v', interpolatino_v)
    cv2.imshow('local_image_u', local_image_u)
    cv2.imshow('local_image_v', local_image_v)
    # cv2.waitKey(0)

    # # 计算这两个有什么区别

    # evaluate1c(y, local_image_y)
    # evaluate1c(interpolation_u, local_image_u)


    # diff_cpp_py_Y = y - local_image_y
    # diff_cpp_py_U = (interpolation_u - local_image_u)
    # diff_cpp_py_V = interpolatino_v - local_image_v
    # diff_cpp_py_Ucpu = interpolation_u - local_image_ucpu
    # diff_cpp_py_Vcpu = interpolatino_v - local_image_vcpu

    # # print("-----------", np.mean(diff_cpp_py_Y), np.std(diff_cpp_py_Y), np.min(diff_cpp_py_Y), np.max(diff_cpp_py_Y))
    # # print("-----------", np.mean(diff_cpp_py_U), np.std(diff_cpp_py_U), np.min(diff_cpp_py_U), np.max(diff_cpp_py_U))
    # # print("-----------", np.mean(diff_cpp_py_V), np.std(diff_cpp_py_V), np.min(diff_cpp_py_V), np.max(diff_cpp_py_V))
    # # print("-----------", np.mean(diff_cpp_py_Ucpu), np.std(diff_cpp_py_Ucpu))
    # # print("-----------", np.mean(diff_cpp_py_Vcpu), np.std(diff_cpp_py_Vcpu))
    # cv2.imshow('diff_cpp_py_Y', diff_cpp_py_Y)
    # cv2.imshow('diff_cpp_py_U', diff_cpp_py_U)
    # cv2.imshow('diff_cpp_py_V', diff_cpp_py_V)
    # cv2.imshow('diff_cpp_py_Ucpu', diff_cpp_py_Ucpu)
    # cv2.imshow('diff_cpp_py_Vcpu', diff_cpp_py_Vcpu)

    # 重组yuv
    interpolation_yuv = cv2.merge((y, interpolation_u, interpolatino_v))
    bgr_useinterpolationyuv = cv2.cvtColor(interpolation_yuv, cv2.COLOR_YUV2BGR)

    evaluate(img_bgr, bgr_useinterpolationyuv)
    diff_useinterpolatinoyuv = img_bgr.astype(np.int16) - bgr_useinterpolationyuv
    print("mean/stddev diff (BGR => YUV => YUYV => interpolation => YUV => BGR)", np.mean(diff_useinterpolatinoyuv), np.std(diff_useinterpolatinoyuv))

    cv2.imshow("bgr_useinterpolationyuv", bgr_useinterpolationyuv)
    cv2.waitKey(0)

