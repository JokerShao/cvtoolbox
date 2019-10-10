import cv2

# 原图像处理
endid = 446
src_path = "D:\\DataRepository\\greenscreen\\xinxinblue\\image_processed\\"
# 兴趣区域坐标 rowstart rowend colstart colend
# roipos_fg = (40, 1020, 550, 1300)
roipos_fg = (40, 850, 500, 1300)
# 重新设置兴趣区域大小
roiresize = (600, 800)

# 背景图像处理
endid_bg = 426
bg_path = "D:\\DataRepository\\greenscreen\\xinxinblue\\unity\\"
roipos_bg = (280,200)

# 从1开始
cnt = 1
vw = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 24.0, (1920, 1080))
while True:

    if cnt > (endid_bg-1):
        break

    # 原图 加5帧偏移量 背景图
    src = cv2.imread(src_path+str(cnt+5)+".png", -1)
    bg = cv2.imread(bg_path+str(cnt)+".jpg")
    # 拿到兴趣区域
    roi = src[roipos_fg[0]:roipos_fg[1],roipos_fg[2]:roipos_fg[3]]

    # 重新设置大小
    roi_resized = cv2.resize(roi, roiresize)
    roi_bgr = cv2.cvtColor(roi_resized, cv2.COLOR_BGRA2BGR)
    _,_,_,roimask = cv2.split(roi_resized)

    # 绘制正方形遮罩遮掉扣不掉的地方
    cv2.rectangle(roimask, (0, 0), (200, 60), 0, -1)
    cv2.rectangle(roimask, (350, 0), (800, 60), 0, -1)



    roimask_inv = ~roimask
    # 在背景左边切出来一块相同大小的图像
    bg_roi = bg[roipos_bg[0]:roipos_bg[0]+roiresize[1],roipos_bg[1]:roipos_bg[1]+roiresize[0]]

    img2_fg = cv2.bitwise_and(roi_bgr, roi_bgr, mask=roimask)
    img1_bg = cv2.bitwise_and(bg_roi, bg_roi, mask=roimask_inv)
    total = cv2.add(img2_fg, img1_bg)
    bg[roipos_bg[0]:roipos_bg[0]+roiresize[1],roipos_bg[1]:roipos_bg[1]+roiresize[0]] = total

    # cv2.imshow("roimask", roimask)
    # cv2.imshow("roimask_inv", roimask_inv)
    # cv2.imshow("img2_fg", img2_fg)
    # cv2.imshow("img1_bg", img1_bg)

    # # cv2.imshow('total', total)

    #     # cv2.imshow('roi', roi)
    # cv2.imshow('roi_resized', roi_resized)
    # cv2.imshow("bg_roi", bg_roi)
    # cv2.imshow('bg', bg)
    # cv2.waitKey(1)

    if cnt > 30:
        vw.write(bg)

    cnt+=1
    # if cnt>100:
    #     break
    print(cnt)


vw.release()