% compute fundamental matrix from matchedPoints, Eight-point-algorithm
% see: Multiple View Geometry 1st edition, P193 (Chinese)
%
% Input:   pts1       [ 2 x N ]
%          pts2       [ 2 x N ]
% Output:  fundamental matrix
%
% Author:  Zexi Shao
% Email:   zexishao@foxmail.com
% Date:    2020.05.17

function F = normalized_eight_point_solver_OK(pts1, pts2)

    [pts_normalized1, T] = normalizing_transform_OK(pts1);
    [pts_normalized2, Td] = normalizing_transform_OK(pts2);

    N = size(pts1, 2);
    A = zeros(N, 9);

    for i = 1:N
        x = pts_normalized1(1, i);
        y = pts_normalized1(2, i);
        xd = pts_normalized2(1, i);  % x'
        yd = pts_normalized2(2, i);  % y'

        A(i,:) = [xd*x xd*y xd yd*x yd*y yd x y 1];
    end

    [~, ~, V] = svd(A, 'econ');
    F_v = V(:, end);
    % MATLAB stores these elements with a column-major array layout.
    F = reshape(F_v, 3, 3)';

    % the singularity constraint
    [U, D, V] = svd(F, 'econ');
    F = U*diag([D(1,1), D(2,2), 0])*V';
    F = Td'*F*T;

    F = F / F(3,3);
end
