% Give camera intrinsic param, generate virtual control points in stereo camera.
% Author: Zexi Shao
% Email:  zexishao@foxmail.com
% Date:   2020.05.15

% 1: left 2: right, measure in meter
function [Pts, pts1, pts2, NN, Rw1, tw1, R21, t21, E, F] = generate_stereo_observation(K1, K2, baseline, N)

    Pts = [rand(N,2)-0.5 rand(N,1)];
    Pts_homo = [Pts ones(N,1)];

    [Rwc, twc] = comp_cam_pose(Pts, 6);
    
    [Rw1, tw1, Rw2, tw2] = comp_stereo_from_mono(Pts, Rwc, twc, baseline)

    
    Show_TransMat2_Stereo([Pts zeros(size(Pts,1), 2)], inv(K1), Rw1, tw1, zeros(1,5));
    Show_TransMat2_Stereo([Pts zeros(size(Pts,1), 2)], inv(K1), Rw2, tw2, zeros(1,5));
    
    
    Tw1 = [Rw1 tw1; [0 0 0 1]];
    T1w = inv(Tw1);

    t12 = [1.3 0 0]';
    R12 = axang2rotm([0 1 0 -pi/9]);
    T12 = [R12 t12; [0 0 0 1]];
    
%     T2w = inv(T12) * T1w;
    T2w = T12 \ T1w;

    P1 = K1 * T1w(1:3,:);
    P2 = K2 * T2w(1:3,:);
    pts1_homo = (P1 * Pts_homo')';
    pts2_homo = (P2 * Pts_homo')';
    pts1 = pts1_homo(:,1:2) ./ pts1_homo(:,3);
    pts2 = pts2_homo(:,1:2) ./ pts2_homo(:,3);
    
    E = skew(t12) * R12;
    F = inv(K1)' * E * K2';

    NN = N;
%     imsize = [K1(1,3)*2 K1(2,3)*2];
%     idx = ( (pts1(:,1) >= 0) & (pts(:,1) < imsize(1)) & ...
%             (pts(:,2) >= 0) & (pts(:,2) < imsize(2)) );
% 
%     Pts = Pts(idx, :);
%     pts = pts(idx, :);
%     NN = size(pts, 1);
end

function [Rwc, twc] = comp_cam_pose(Pts, max_dist)

    centroid = mean(Pts)';
    dmax = max(vecnorm(Pts' - centroid));
    length = dmax*(1.5+rand*max_dist);
    v = [1+rand*3 rand-0.5 1+rand]';
    v = v / norm(v) * length;
    twc = centroid + v;

    Zc = centroid - twc;
    Zc = Zc / norm(Zc);
    Zw = [0 0 1]';

    theta = acos(Zw'*Zc);
    axis = cross(Zw, Zc);
    axis = axis / norm(axis);
    Rwc = axang2rotm([axis' theta]);
    Rwc = Rwc * axang2rotm([0 0 1 pi/2]);
end

function [Rw1, tw1, Rw2, tw2] = comp_stereo_from_mono(Pts, Rwc, twc, baseline)

    centroid = mean(Pts)';

    tc1 = [-baseline/2 0 0]';
    tc2 = [baseline/2 0 0]';

    tw1 = Rwc * tc1 + twc;
    tw2 = Rwc * tc2 + twc;

    Z1 = centroid - tw1;
    Z1 = Z1 / norm(Z1);
    Zw = [0 0 1]';
    theta = acos(Zw'*Z1);
    axis = cross(Zw, Z1);
    axis = axis / norm(axis);
    Rw1 = axang2rotm([axis' theta]);
    Rw1 = Rw1 * axang2rotm([0 0 1 pi/2]);
    
    Z2 = centroid - tw2;
    Z2 = Z2 / norm(Z2);
    Zw = [0 0 1]';
    theta = acos(Zw'*Z2);
    axis = cross(Zw, Z2);
    axis = axis / norm(axis);
    Rw2 = axang2rotm([axis' theta]);
%     Rw2 = Rw2 * axang2rotm([0 0 1 pi/2]);



end






