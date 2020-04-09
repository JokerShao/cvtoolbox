% 棋盘格上的三维点
Pts = rand(-15, 15, [3 88]);
% 
% Pts = np.vstack((Pts, np.ones((1, 88))))
% 
% # # 1左眼 2右眼
% # R12 = np.array([[0.999926749233609, 0.0120680870553295, -0.000925981604431065],
% #                 [-0.0120699382277973, 0.999925114680933, -0.00202030232891710],
% #                 [0.000901531077619697, 0.00203133088098873, 0.999997530465235]]).T
% # t12 = np.array([[-36.1047485444445, -0.158128589976602, 0.0109828281049081]]).T/10 #cm
% # T12 = np.vstack((np.hstack((R12, t12)), np.array([[0, 0, 0, 1]])))
% # T21 = np.linalg.inv(T12)
% 
% K1 = np.array([[1139.52250164735, 0, 0],
%                 [0, 1139.44191865558, 0],
%                 [637.318653650454, 313.142770524206, 1]]).T
% 
% # K2 = np.array([[1139.80972146911,	0,	0],
% #                 [0,	1139.71594761323,	0],
% #                 [692.176254393361,	350.117194234653,	1]]).T
% 
% mono_err_ori = []
% mono_err_pos = []
% 
% stereo_err_ori = []
% stereo_err_pos = []
% 
% 
% def cost(X, pts1_ob, pts2_ob):
%     R1o, _ = cv2.Rodrigues(X[0:3])
%     tvec1o = X[3:6].reshape(3,1)
%     T1o = np.hstack((R1o, tvec1o))
% 
%     pts1_ob_homo = np.vstack((pts1_ob, np.ones((1, pts1_ob.shape[1]))))
%     pp = np.linalg.inv(K1) @ pts1_ob_homo
% 
%     cam1_err = pp - Pts[0:3,:]
% 
%     # pts1_homo = K1 @ T1o @ Pts
%     # pts1 = pts1_homo[0:2, :] / pts1_homo[2,:]
% 
%     # T2o = (T21 @ np.vstack((T1o, np.array([[0, 0, 0, 1]]))))[0:3, :]
%     # # R2o = T2o[:,0:3]
%     # # t2o = T2o[:,3]
%     # pts2_homo = K2 @ T2o @ Pts
%     # pts2 = pts2_homo[0:2, :] / pts2_homo[2,:]
% 
%     # cam1_err = pts1-pts1_ob
%     # cam2_err = pts2-pts2_ob
% 
%     # cam1_err_vnorm = np.linalg.norm(cam1_err, axis=0)
%     # cam2_err_vnorm = np.linalg.norm(cam2_err, axis=0)
% 
%     # print(np.linalg.norm(cam1_err_vnorm))
%     # print(np.linalg.norm(cam2_err_vnorm))
% 
%     # err = np.hstack((cam1_err_vnorm, cam2_err_vnorm))
% 
%     print(np.linalg.norm(cam1_err))
%     return np.linalg.norm(cam1_err)
%     # return np.linalg.norm(cam1_err_vnorm) + np.linalg.norm(cam2_err_vnorm)#np.linalg.norm(err)
% 
% 
% for i in range(30):
% 
%     rvec1o = np.random.random((3,1))
%     R1o, _ = cv2.Rodrigues(rvec1o)
%     tvec1o = np.random.random((3,1))*50+30
%     T1o = np.hstack((R1o, tvec1o))
% 
%     pts1_homo = K1 @ T1o @ Pts
%     pts1 = pts1_homo[0:2, :] / pts1_homo[2,:]
%     noise1 = np.random.normal(0, 2, pts1.shape)
%     # print(noise1.max())
%     pts1 = pts1+noise1
% 
%     # T2o = (T21 @ np.vstack((T1o, np.array([[0, 0, 0, 1]]))))[0:3, :]
%     # R2o = T2o[:,0:3]
%     # t2o = T2o[:,3]
%     # rvec2o, _ = cv2.Rodrigues(R2o)
%     # pts2_homo = K2 @ T2o @ Pts
%     # pts2 = pts2_homo[0:2, :] / pts2_homo[2,:]
%     # noise2 = np.random.normal(0, 3, pts2.shape)
%     # # print(noise2.max())
%     # pts2 = pts2+noise2
% 
%     # print(pts1)
%     # print(pts2)
%     retval, rvec1o_pred, tvec1o_pred = cv2.solvePnP(Pts[0:3,:].T, pts1.T, K1, None)
%     # retval, rvec2o_pred, tvec2o_pred = cv2.solvePnP(Pts[0:3,:].T, pts2.T, K2, None)
% 
%     X = np.hstack((rvec1o_pred.T, tvec1o_pred.T))
%     print('X initial:', X)
%     opts = {'disp': False, 'maxiter': 1e20, 'ftol': 1e-20}
%     X_res = minimize(fun=cost, x0=X, args=(pts1, None), method='BFGS', options=opts)
%     
%     # print('gt   rvec1o:', rvec1o.T, 'gt   tvec1o:', tvec1o.T)
%     # print('pred rvec1o:', rvec1o_pred.T, 'pred tvec1o:', tvec1o_pred.T)
%     # print('\n')
%     # print('gt   rvec2o:', rvec2o.T, 'gt   tvec2o:', t2o.T)
%     # print('pred rvec2o:', rvec2o_pred.T, 'pred tvec2o:', tvec2o_pred.T)
%     mono_err_ori.append(np.linalg.norm(rvec1o_pred-rvec1o))
%     mono_err_pos.append(np.linalg.norm(tvec1o_pred-tvec1o))
% 
%     stereo_err_ori.append(np.linalg.norm(X_res.x[0:3]-rvec1o))
%     stereo_err_pos.append(np.linalg.norm(X_res.x[3:6]-tvec1o))
% 
% 
% print('.')
% print('mono mean: ', np.mean(mono_err_pos))
% print('mono std: ', np.std(mono_err_pos))
% print('mono range: ', max(mono_err_pos)-min(mono_err_pos))
% 
% print('stereo mean: ', np.mean(stereo_err_pos))
% print('stereo std: ', np.std(stereo_err_pos))
% print('stereo range: ', max(stereo_err_pos)-min(stereo_err_pos))
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% fc{1,1} = [ 727.103994231518186 ; 728.108732171242991 ];
% cc{1,1} = [ 673.671104028911941 ; 498.391261215287443 ];
% kc{1,1} = [ -0.334105443705504 ; 0.109151714144811 ; 0 ; 0 ; -0.015073857960244 ];
% 
% fc{2,1} = [ 712.913706682467478 ; 713.705256317740009 ];
% cc{2,1} = [ 699.701898409380874 ; 504.481198322692535 ];
% kc{2,1} = [ -0.341642431488352 ; 0.122308506570778 ; 0 ; 0 ; -0.019456930559966 ];
% 
% fc{3,1} = [ 738.700617590930733 ; 738.887801882869667 ];
% cc{3,1} = [ 653.543345286270892 ; 518.612752643385761 ];
% kc{3,1} = [ -0.360991433548094 ; 0.139663369202313 ; 0 ; 0 ; -0.024933870567775 ];
% 
% fc{4,1} = [ 735.558200054117492 ; 735.320267456636884 ];
% cc{4,1} = [ 619.659113346876666 ; 519.355355000901113 ];
% kc{4,1} = [ -0.357342286276954 ; 0.135554703771497 ; 0 ; 0 ; -0.023199305860021 ];
% 
% 
% 
% for i=1:4
%     
% 
%         
%     K{i,1}=[ fc{i}(1),      0     ,  cc{i}(1);...
%                       0    ,   fc{i}(2) ,  cc{i}(2);...
%                       0    ,      0     ,      1    ];
%         
%     invK{i,1}=inv(K{i,1});    
%      
% end
% 
% 
% %%
% load('cabin_floor0319.mat');
% 
% [CameraHouse]=Get_CameraHouse(invK,kc,A1,A2,A3,A4);
% 
% L12=norm(CameraHouse{1}(:,4)-CameraHouse{2}(:,4))
% L23=norm(CameraHouse{3}(:,4)-CameraHouse{2}(:,4))
% L34=norm(CameraHouse{3}(:,4)-CameraHouse{4}(:,4))
% L12=norm(CameraHouse{1}(:,4)-CameraHouse{4}(:,4))
% 
