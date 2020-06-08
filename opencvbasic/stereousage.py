import numpy as np
from scipy.optimize import minimize
import cv2

# 棋盘格上的三维点
Pts = np.random.uniform(-15, 15, (3,88));
Pts = np.vstack((Pts, np.ones((1, 88))))

fs = cv2.FileStorage('/home/zexi/robotcalibration/StereoCamParams_720_Matlab.xml', cv2.FileStorage_READ)
R21 = fs.getNode('R_rl').mat()
t21 = fs.getNode('t_rl').mat()
K1 = fs.getNode('K_left').mat()
K2 = fs.getNode('K_right').mat()
E = fs.getNode('E').mat()
F = fs.getNode('F').mat()
fs.release()

print(R21)
print(t21)

t0, t1, t2 = t21
tprod = np.array([[0, -t2, t1], [t2, 0, -t0], [-t1, t0, 0]])
E_computed = np.array(tprod @ R21, dtype=np.float64)
print(E)
print(E_computed)

print('---')
F_computed = np.linalg.inv(K2).T @ E_computed @ np.linalg.inv(K1)
print(F/F[2,2])
print(F_computed/F_computed[2,2])


# 1左眼 2右眼
T21 = np.vstack((np.hstack((R21, t21)), np.array([[0, 0, 0, 1]])))
T12 = np.linalg.inv(T21)


# K1 = np.array([[1139.52250164735, 0, 0],
#                 [0, 1139.44191865558, 0],
#                 [637.318653650454, 313.142770524206, 1]]).T

# K2 = np.array([[1139.80972146911,	0,	0],
#                 [0,	1139.71594761323,	0],
#                 [692.176254393361,	350.117194234653,	1]]).T

# E = np.array([[1.38824397692056e-05, -0.0106625380937231, -0.158150509230442],
#                 [-0.0224503093804326, -0.0730750696261002, 36.1046692838736],
#                 [-0.277598241608939, -36.1039534311430, -0.0731981328305389]]).T / 10

# F = np.array([[1.06883467754025e-11, -8.20986557913865e-09, -0.000136187627878395],
#                 [-1.72863300028008e-08, -5.62704541151051e-08, 0.0317072934475875],
#                 [-0.000237564424082333, -0.0316602622120772, -1.00281316110991]]).T/10

# fs = cv2.FileStorage('/home/zexi/robotcalibration/StereoCamParams_720_Matlab.xml', cv2.FileStorage_WRITE)
# fs.write('K_left', K1)
# fs.write('D_left', np.ones(5))
# fs.write('K_right', K2)
# fs.write('D_right', np.ones(5))
# fs.write('R_lr', R12)
# fs.write('t_lr', t12)
# fs.write('E', E)
# fs.write('F', F)
# fs.release()

# EEE = np.array([[2.3423919152048786e-04, 1.7571556921211387e-02,    -7.7595672236738704e-03],
#                 [-2.2257689373438472e-02, -1.4176867341781377e-02, 3.6028904981627927e+00],
#                 [-3.8175729638714552e-02, -3.6027217114401000e+00,    -1.4450165652077501e-02]])

# FFF = np.array([[    -1.8083766043482505e-09, -1.3565950943381042e-07,    1.1236545937199529e-04],
#      [1.7187241215543254e-07, 1.0947552831747728e-07,    -3.1910335965693884e-02],
#       [2.7746062160593159e-04,    3.1797551741755060e-02, 1]])
# R12 = np.array([[0.999926749233609, 0.0120680870553295, -0.000925981604431065],
#                 [-0.0120699382277973, 0.999925114680933, -0.00202030232891710],
#                 [0.000901531077619697, 0.00203133088098873, 0.999997530465235]]).T
# t12 = np.array([[-36.1047485444445, -0.158128589976602, 0.0109828281049081]]).T/10 #cm

mono_err_ori = []
mono_err_pos = []

stereo_err_ori = []
stereo_err_pos = []


def cost2(X, pts1_ob, pts2_ob):
    """
    基础矩阵做代价误差
    """

    # p2 = pts2_homo[:, 0:1] / pts2_homo[2,0:1]
    # p1 = pts1_homo[:, 0:1] / pts1_homo[2,0:1]
    # t1, t2, t3 = t12
    # crossprod = np.array([[0, -t3, t2],
    #                         [t3, 0, -t1],
    #                         [-t2, t1, 0]])
    # print(p2.T @ np.linalg.inv(K2).T @ crossprod @ R12 @ np.linalg.inv(K1) @ p1)
    # print(pts2_homo[:, 0].T @ (F.T) @ pts1_homo[:, 0])
    # print(pts2_homo[:, 0].T @ (F) @ pts1_homo[:, 0])
    
    # err = pts2_homo[:, 0].T @ (F.T) @ pts1_homo[:, 0]


    # 左眼
    R1o, _ = cv2.Rodrigues(X[0:3])
    tvec1o = X[3:6].reshape(3,1)
    T1o = np.hstack((R1o, tvec1o))

    pts1_homo = K1 @ T1o @ Pts
    pts1 = pts1_homo[0:2, :] / pts1_homo[2,:]
    cam1_err = pts1 - pts1_ob

    pts2_ob_homo = np.vstack((pts2_ob, np.ones((1, pts2_ob.shape[1]))))
    cam2_err = pts1_homo.T @ F @ pts2_ob_homo

    pts2_homo = F @ pts1_homo
    pts2 = pts2_homo[0:2, :] / pts2_homo[2,:]
    cam2_err = pts2 - pts2_ob
    To1_44 = np.linalg.inv(np.vstack((T1o, np.array([[0, 0, 0, 1]]))))

    T2o = (T21 @ np.vstack((T1o, np.array([[0, 0, 0, 1]]))))[0:3, :]
    # To2_44 = np.linalg.inv(T2o)
    R2o = T2o[0:3,0:3]
    t2o = T2o[0:3,3]
    pts2_homo = K2 @ T2o @ Pts
    err = np.hstack((cam1_err, cam2_err))
    return np.linalg.norm(err)

def cost1(X, pts1_ob, pts2_ob):
    """
    求重投影误差的方法
    """
    # 左眼
    R1o, _ = cv2.Rodrigues(X[0:3])
    tvec1o = X[3:6].reshape(3,1)
    T1o = np.hstack((R1o, tvec1o))
    # To1_44 = np.linalg.inv(np.vstack((T1o, np.array([[0, 0, 0, 1]]))))

    pts1_homo = K1 @ T1o @ Pts
    pts1 = pts1_homo[0:2, :] / pts1_homo[2,:]
    cam1_err = pts1 - pts1_ob

    T2o = (T21 @ np.vstack((T1o, np.array([[0, 0, 0, 1]]))))[0:3, :]
    # To2_44 = np.linalg.inv(T2o)
    # R2o = T2o[0:3,0:3]
    # t2o = T2o[0:3,3]
    pts2_homo = K2 @ T2o @ Pts
    pts2 = pts2_homo[0:2, :] / pts2_homo[2,:]
    cam2_err = pts2 - pts2_ob

    err = np.hstack((cam1_err, cam2_err))
    # print(np.linalg.norm(err))
    return np.linalg.norm(err)


def cost(X, pts1_ob, pts2_ob):
    """
    求射线夹角的方法
    """
    # 左眼
    R1o, _ = cv2.Rodrigues(X[0:3])
    tvec1o = X[3:6].reshape(3,1)
    T1o = np.hstack((R1o, tvec1o))
    To1_44 = np.linalg.inv(np.vstack((T1o, np.array([[0, 0, 0, 1]]))))

    T2o = (T21 @ np.vstack((T1o, np.array([[0, 0, 0, 1]]))))
    To2_44 = np.linalg.inv(T2o)

    err = 0

    for i in range(Pts.shape[1]):
        W = Pts[0:3, i]
        P = pts1_ob[:, i]
        U = np.linalg.inv(K1) @ np.array([P[0], P[1], 1])
        V = To1_44[0:3, 0:3] @ U
        V2 = W - To1_44[0:3,3]
        err += np.linalg.norm(np.cross(V2, V))

        P = pts2_ob[:, i]
        U = np.linalg.inv(K2) @ np.array([P[0], P[1], 1])
        V = To2_44[0:3, 0:3] @ U
        V2 = W - To2_44[0:3,3]
        err += np.linalg.norm(np.cross(V2, V))

    return err



for i in range(400):

    print(i)
    rvec1o = np.random.random((3,1))
    R1o, _ = cv2.Rodrigues(rvec1o)
    tvec1o = np.random.random((3,1))*50+30
    T1o = np.hstack((R1o, tvec1o))

    pts1_homo = K1 @ T1o @ Pts
    pts1 = pts1_homo[0:2, :] / pts1_homo[2,:]
    noise1 = np.random.normal(0, 7, pts1.shape)
    pts1 = pts1+noise1

    T2o = (T21 @ np.vstack((T1o, np.array([[0, 0, 0, 1]]))))[0:3, :]
    R2o = T2o[:,0:3]
    t2o = T2o[:,3]
    rvec2o, _ = cv2.Rodrigues(R2o)
    pts2_homo = K2 @ T2o @ Pts
    pts2 = pts2_homo[0:2, :] / pts2_homo[2,:]
    noise2 = np.random.normal(0, 7, pts2.shape)
    pts2 = pts2+noise2

    retval, rvec1o_pred, tvec1o_pred = cv2.solvePnP(Pts[0:3,:].T, pts1.T, K1, None)
    # retval, rvec2o_pred, tvec2o_pred = cv2.solvePnP(Pts[0:3,:].T, pts2.T, K2, None)

    X = np.hstack((rvec1o_pred.T, tvec1o_pred.T))
    # print('X initial:', X)
    opts = {'disp': False, 'maxiter': 1e30, 'ftol': 1e-30}
    X_res = minimize(fun=cost1, x0=X, args=(pts1, pts2), method='L-BFGS-B', options=opts)
    
    mono_err_ori.append(np.linalg.norm(rvec1o_pred-rvec1o))
    mono_err_pos.append(np.linalg.norm(tvec1o_pred-tvec1o))
    # print('mono:', np.linalg.norm(tvec1o_pred-tvec1o))

    stereo_err_ori.append(np.linalg.norm(X_res.x[0:3].reshape(3,1)-rvec1o))
    stereo_err_pos.append(np.linalg.norm(X_res.x[3:6].reshape(3,1)-tvec1o))
    # print('stereo:', np.linalg.norm(X_res.x[3:6].reshape(3,1)-tvec1o))


print('.')
print('mono mean: ', np.mean(mono_err_pos))
print('mono std: ', np.std(mono_err_pos))
print('mono range: ', max(mono_err_pos)-min(mono_err_pos))

print('stereo mean: ', np.mean(stereo_err_pos))
print('stereo std: ', np.std(stereo_err_pos))
print('stereo range: ', max(stereo_err_pos)-min(stereo_err_pos))
