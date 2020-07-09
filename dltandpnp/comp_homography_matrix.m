% Input:    Pts    [ 2 x N ]
%           pts    [ 2 x N ]
% Output:   homography matrix
%
% Author:  Zexi Shao
% Email:   zexishao@foxmail.com
% Date:    2020.05.19

function H = comp_homography_matrix(Pts, pts)

    N = size(Pts, 2);
    A = zeros(2*N, 8);
    
    for i = 1:N
        u1 = Pts(1,i);
        v1 = Pts(2,i);
        u2 = pts(1,i);
        v2 = pts(2,i);
        A(i*2-1:i*2,:) = [ u1 v1 1 0 0 0 -u1*u2 -v1*u2;
                           0 0 0 u1 v1 1 -u1*v2 -v1*v2];
    end
    
    [~, ~, V] = svd(A, 'econ');
    H_v = V(:,end);
    H = reshape(H_v, 3, 3)';
end




