% compute a normalizing transform, for better DLT result.
% see Multiple View Geometry 1st edition, P67 (Chinese)
%
% Input:   pts               [ 2 x N ]
% Output:  pts_normalized    [ 2 x N ]
%          transform_matrix  [ 3 x 3 ]
%
% Author:  Zexi Shao
% Email:   zexishao@foxmail.com
% Date:    2020.05.17

function [pts_normalized, T] = normalizing_transform_OK(pts)

    cc = mean(pts, 2);
    vv = pts - cc;

    s = sqrt(2) / (sum(vecnorm(vv))/size(pts, 2));

    pts_normalized = vv * s;
    T = [ s 0 -s*cc(1);
          0 s -s*cc(2);
          0 0 1];
end
