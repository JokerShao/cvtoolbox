clear;
clc;
close all;


% load extrinsic parameters
load('transmat.mat');

Tw1 = [Tw1; [0 0 0 1]];
Tw2 = [Tw2; [0 0 0 1]];
T1w = inv(Tw1);
T2w = inv(Tw2);

T21 = T2w * Tw1;
R21 = T21(1:3,1:3)
t21 = T21(1:3,4)

T12 = inv(T21);
R12 = T12(1:3,1:3);
t12 = T12(1:3, 4);












N = 30;
K = [700 0 1280/2;
     0 700 720/2;
     0 0 1];
invK = inv(K);

Pts = [(rand(2,N)-0.5)*1.5; rand(1,N)];
Pts_homo = [Pts; ones(1,N)];


pts1_homo = K * T1w(1:3,:) * Pts_homo;
pts1 = pts1_homo(1:2,:) ./ pts1_homo(3,:);

pts2_homo = K * T2w(1:3,:) * Pts_homo;
pts2 = pts2_homo(1:2,:) ./ pts2_homo(3,:);

imsize = [1280 720];
idx1 = ( (pts1(1, :) >= 0) & (pts1(1, :) < imsize(1)) & ...
        (pts1(2, :) >= 0) & (pts1(2, :) < imsize(2)) );
idx2 = ( (pts2(1, :) >= 0) & (pts2(1, :) < imsize(1)) & ...
    (pts2(2, :) >= 0) & (pts2(2, :) < imsize(2)) );
idx = idx1 & idx2;

pts1 = pts1(:, idx);
pts2 = pts2(:, idx);


% A1 = sortrows(A1, 1);
% A2 = sortrows(A2, 1);
% pts1 = A1(:, 3:4)';
% pts2 = A2(:, 3:4)';
% csvwrite('/Users/zexi/Desktop/cvtoolbox/pts_matched.txt', [pts1; pts2])


R21
t21

E = skew(t21) * R21;

[RR1, RR2, tt] = decompose_essential_matrix_OK(E);


[R, t] = motion_from_essential_choose_solution_OK(RR1, RR2, tt)







F_real = inv(K') * skew(t21) * R21 * inv(K);
F_real = F_real / F_real(3,3)

F_mine = normalized_eight_point_solver(pts1, pts2)

F_opencv = [ 1.12001323e-06  1.14968529e-06 -5.94228021e-04;
             9.33134413e-07  1.88030393e-06 -2.88715994e-03;
             -5.40662805e-04 -8.29995015e-04  1.00000000e+00]

pp1 = [pts1(:, 1); 1];
pp2 = [pts2(:, 1); 1];

pp2'*F_real*pp1

pp2'*F_mine*pp1

pp2'*F_opencv*pp1




[U, S, V] = svd(E, 'econ')
[R_calc, t_calc] = DLT_OK(Pts, pts, invK);
[R_calc t_calc]


N_p = 50;

P = [rand(2, N_p)-0.5;
     1+rand(1, N_p)];
K1 = eye(3);
K2 = eye(3);
R = eye(3);
t = [5.2 0 0]';


generate_stereo_observation(K1, K2, 0.4, N_p)




p1_homo = K1 * P;
p2_homo = K2 * (R * P + t);

x1 = inv(K1) * p1_homo;
x1 = x1 / norm(x1);
x2 = inv(K2) * p2_homo;
x2 = x2 / norm(x2);

E = skew(t) * R;
[U, S, V] = svd(E, 'econ')
EE = U * diag([1 1 0]) * V';


E_calc = comp_essential_matrix(x1(1:2,:), x2(1:2, :));






% compute use matlab
IntrinsicMatrix = K;
radialDistortion = [0 0];
cameraParams = cameraParameters('IntrinsicMatrix',IntrinsicMatrix,'RadialDistortion',radialDistortion); 

[E_calc, inlierIdx, status] = estimateEssentialMatrix(pts1', pts2', cameraParams);


% N = 10;
% pts = rand(2, N);
% 
% [pts_normalized, T] = normalizing_transform(pts)
% 
% 
% pts_homo = [pts; ones(1, N)];
% pts_calc_homo = T*pts_homo;
% pts_calc = pts_calc_homo(1:2,:) ./ pts_calc_homo(3,:)
% 
% 
% plot(0, 0, 'ro');
% hold on;
% plot(pts(1,:), pts(2,:), 'b*');
% hold on;
% plot(pts_calc(1,:), pts_calc(2,:), 'r*');
% 
% grid on;





% 
% x2(:,1)' * EE * x1(:,1)
% x2(:,1)' * E_calc * x1(:,1)
% x2(:,1)' * E * x1(:,1)


% skew(t) * x2
% cross(t,x2)
% 
% norm(x2)
% rad2deg(acos(t'*x2/(norm(t)*norm(x2))))
% 
% % 
% vv = skew(t) * x2
% vv = vv / norm(vv)
% 
% x2' * vv%skew(t) * x2
% acos(x2' * vv)
% 
% 
% [U, D, V] = svd(E, 'econ');
% EE = U * diag([1 1 0]) * V';
% % 
% x2' * E * x1
% x2' * EE * x1


% 
% p2
% 
% 
% 
% R12 = axang2rotm([0 1 0 -pi/6]);
% t12 = [2.2 0.1 0.3]';
% T12 = [R12 t12;
%        [0 0 0 1]];
% T21 = inv(T12);
% 
% R21 = T21(1:3,1:3);
% t21 = T21(1:3,4);
% 
% 
% 
% pts1 = K1 * Pts;
% pts2 = K2 * (R21 * Pts + t21);
% x1s = pts1;
% x2s = pts2;
% 
% x1s = x1s ./ x1s(3,:);
% x2s = x2s ./ x2s(3,:);
% 
% E = skew(t21) * R21;
% E = E / E(3,3)
% 
% x1s(:,1)'*E*x2s(:,1)
% 
% pts1(:,1)'*E*pts2(:,1)
% 
% 
% E_calc = comp_essential_matrix(x2s, x1s);
% E_calc = E_calc / E_calc(3,3)
% 
% 
% % 
% 
% 
% P1 = K1 * T1w(1:3, :);
% P2 = K2 * T2w(1:3, :);
% 
% Pts_homo = [Pts; ones(1, 8)];
% 
% pts1_homo = P1 * Pts_homo;
% pts2_homo = P2 * Pts_homo;
% 
% pts1 = pts1_homo(1:2, :) ./ pts1_homo(3,:);
% pts2 = pts2_homo(1:2, :) ./ pts2_homo(3,:);
% 
% 
% E = skew(t21)*R21;
% 
% % E = skew(t12) * R12;
% E = E / E(3,3)
% 
% E_calc = comp_essential_matrix(pts1, pts2);
% E_calc = E_calc / E_calc(3,3)
% 
% % T12_calc = [R12_calc t12_calc;
% %             [0 0 0 1]];
% % 
% % Tw1 = eye(4);
% % Rw1 = eye(3);
% % tw1 = zeros(3,1);
% % 
% % Tw2 = Tw1 * T12_calc;
% % Rw2 = Tw2(1:3,1:3);
% % tw2 = Tw2(1:3,4);
% 
% 
% % Tw1 = [Rw1 tw1; [0 0 0 1]];
% % T12 = [R12 t12; [0 0 0 1]];
% % Tw2 = Tw1*T12;
% % Rw2 = Tw2(1:3,1:3);
% % tw2 = Tw2(1:3,4);
% % 
% % show_stereo_cam(Pts, Rw1, tw1, Rw2, tw2);
% % [Pts, pts1, pts2, NN, Rw1, tw1, R12, t12, E, F] = generate_stereo_observation(K1, K2, N);
% 

% % % points num
% % N = 50;
% % K1 = [700 0 1280/2;
% %       0 700 720/2;
% %       0 0 1];
% % K2 = K1;