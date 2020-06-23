% Give camera intrinsic param, generate virtual control points,
% return Euclidian coordinate.
% Author: Zexi Shao
% Email:  zexishao@foxmail.com
% Date:   2020.05.13

function [Pts, pts, NN, Rwc, twc] = generate_observation(K, N, plane)

    if plane
        Pts = [rand(N,2)-0.5 zeros(N,1)];
    else
        Pts = [rand(N,2)-0.5 rand(N,1)];
    end

    [Rwc, twc] = comp_cam_pose(Pts, 6);
    Rcw = Rwc';
    tcw = -Rcw*twc;

    Pts_homo = [Pts ones(N,1)];
    P = K * [Rcw tcw];
    pts_homo = (P * Pts_homo')';
    pts = pts_homo(:,1:2) ./ pts_homo(:,3);

    imsize = [K(1,3)*2 K(2,3)*2];
    idx = ( (pts(:,1) >= 0) & (pts(:,1) < imsize(1)) & ...
            (pts(:,2) >= 0) & (pts(:,2) < imsize(2)) );

    Pts = Pts(idx, :);
    pts = pts(idx, :);
    NN = size(pts, 1);
end

function [Rwc, twc] = comp_cam_pose(Pts, max_dist)

    centroid = mean(Pts)';
    dmax = max(vecnorm(Pts' - centroid));
    length = dmax*(1.5+rand*max_dist);
    v = [rand(1, 2)-0.5   1+rand*3]';
    v = v / norm(v) * length;
    twc = centroid + v;

    Zc = centroid - twc;
    Zc = Zc / norm(Zc);
    Zw = [0 0 1]';

    theta = acos(Zw'*Zc);
    axis = cross(Zw, Zc);
    axis = axis / norm(axis);
    Rwc = axang2rotm([axis' theta]);
end
