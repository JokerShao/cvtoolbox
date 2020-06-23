% compute essential matrix from matchedPoints, normalized-eight-point-algorithm
%
% Input:   pts1 pts2 normalized matched points. [ 2 x N ]
% Output:  essential matrix
%
% Author:  Zexi Shao
% Email:   zexishao@foxmail.com
% Date:    2020.05.17

function E = comp_essential_matrix_OK(pts1, pts2, K1, K2)

    F = normalized_eight_point_solver_OK(pts1, pts2);
    E = K2' * F * K1;
end
