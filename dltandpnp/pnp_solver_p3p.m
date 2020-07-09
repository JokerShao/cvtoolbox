% Perspective-n-point problem, p3p algorithm.
% Reference: Complete solution classification for the
% perspective-three-point problem 2003.
% part of code from https://github.com/ftdlyc/PnP_Matlab
%
% Input:   Pts  [3 x N] or [4 x N] (world frame)
%          pts  [2 x N] or [3 x N] (camera frame)
%          K    [3 x 3]
%
% Output:  Rcw  [3 x 3]
%          tcw  [3 x 1]
%
% Author:      Zexi Shao
% Email:       zexishao@foxmail.com
% Date:        2020.05.21
% Last modify: 2020.06.15

function [Rcw, tcw] = pnp_solver_p3p(Pts, pts)
    [row_X, col_X] = size(Pts);
    [row_x, col_x] = size(pts);
    if row_X ~= 3 && row_X ~= 4
        fprintf('mat X must be [3 x n] or [4 x n]\n')
        return
    end
    if row_x ~= 2 && row_x ~= 3
        fprintf('mat x must be [2 x n] or [3 x n]\n')
        return
    end
    if col_X ~= col_x
        fprintf('col(x) no equal to col(X)\n')
        return
    end
    n = col_X;
    if n ~= 3
        fprintf('col(x)/col(X) must be 3\n')
        return
    end
    if row_X == 4
        Pts = Pts(1:3, :) ./ Pts(4, :);
    end
    if row_x == 2
        pts(3, :) = ones(1, col_x);
    end

    % verification that world points are not colinear
    if norm(cross(Pts(:, 2) - Pts(:, 1), Pts(:, 3) - Pts(:, 1))) < 1e-5
        fprintf('point A, B, C are colinear\n')
        return;
    end

%% calc point (A, B, C) in camera frame
    pts_norm = pts ./ vecnorm(pts, 2);
    cos_ab = pts_norm(:,1)' * pts_norm(:,2);
    cos_bc = pts_norm(:,2)' * pts_norm(:,3);
    cos_ac = pts_norm(:,1)' * pts_norm(:,3);

    AB = norm(Pts(:,1)-Pts(:,2));
    BC = norm(Pts(:,2)-Pts(:,3));
    AC = norm(Pts(:,1)-Pts(:,3));

    [lengths, n] = solve_lengths([cos_bc cos_ac cos_ab]', [BC AC AB]');

%% SVD solve 3D-3D problem (ICP)
% see: https://zhuanlan.zhihu.com/p/35893884
    Rcw = {};
    tcw = {};

    for i = 1:n
        pts = pts_norm .* lengths(:,i)';
        mu_pts = mean(pts, 2);
        mu_Pts = mean(Pts, 2);
        % p' P' (qi pi)
        ptsd = pts-mu_pts;
        Ptsd = Pts-mu_Pts;

        % i don't know why! 2020.05.24 zexi
        W = ptsd*Ptsd';
%         W = zeros(3, 3);
%         for j = 1:3
%             W = W + ptsd(:, j) * Ptsd(:, j)'; 
%         end

        [U, S, V] = svd(W);

        % https://durant35.github.io/2017/07/21/Algorithms_ICP/
        % Special reflection case
        R = U*V';
        if (det(R) < 0)
            V(:,3) = -V(:,3);
            R = U*V';
        end

        t = mu_pts - R*mu_Pts;
        Rcw{i} = R;
        tcw{i} = t;
    end
end

% Given 3D distances between three points and cosines of 3 angles at the apex 
% calculates the lentghs of the line segments connecting projection center 0 and 
% the three 3D points (A, B, C).
%
% by ftdlyc
%
% Input
% cosines: [cos<b, c>, cos<a, c>, cos<a, b>]'
% distances: [|BC|, |AC|, |AB|]'
%
% Output
% lengths: [3 x n]
%          [|OA| ...
%           |OB| ...
%           |OC| ...]
%
function [lengths, n] = solve_lengths(cosines, distances)

    n = 0;
    lengths = [];

    p = 2 * cosines(1);
    q = 2 * cosines(2);
    r = 2 * cosines(3);
    a = distances(1) * distances(1) / (distances(3) * distances(3));
    b = distances(2) * distances(2) / (distances(3) * distances(3));

    a2 = a * a;
    b2 = b * b;
    q2 = q * q;
    p2 = p * p;
    r2 = r * r;

    coeff4 = a2 + b2 - 2 * a - 2 * b + (2 - r2) * b * a + 1;
    coeff3 = -2 * q * a2 - r * p * b2 + 4 * q * a + (2 * q + p * r) * b ...
            + (r2 * q - 2 * q + r * p) * a * b - 2 * q;
    coeff2 = (2 + q2) * a2 + (p2 + r2 - 2) * b2 - (4 + 2 * q2) * a ...
            - (p * q * r + p2) * b - (p * q * r + r2) * a * b + q2 + 2;
    coeff1 = -2 * q * a2 - r * p * b2 + 4 * q * a + (p * r + q * p2 - 2 * q) * b ...
            + (r * p + 2 * q) * a * b - 2 * q;
    coeff0 = a2 + b2 - 2 * a + (2 - p2) * b - 2 * a * b + 1;
    b1 = b * ((p2 - p * q * r + r2) * a + (p2 - r2) * b - p2 + p * q * r - r2)^2;

    if b1 == 0 || coeff4 == 0
        return
    end

    x_roots = roots([coeff4, coeff3, coeff2, coeff1, coeff0]);

    for i = 1:size(x_roots, 1)
        x = real(x_roots(i));
        if x <= 0
            continue
        end

        b0 = ((1 - a - b) * x^2 + (a - 1) * q * x - a + b + 1) * ( ...
            r^3 * (a2 + b2 - 2 * a - 2 * b + (2 - r2) * a * b + 1) * x^3 ...
            + r^2 * (p + p * a2 - 2 * r * q * a * b + 2 * r * q * b - 2 * r * q ...
                    -2 * p * a - 2 * p * b + p * r2 * b + 4 * r * q * a ...
                    + q * r^3 * a * b - 2 * r * q * a2 + 2 * p * a * b + p * b2 ...
                    - r2 * p * b2) * x^2 ...
            + (r^5 * (b2 - a * b) ...
              - r^4 * p * q * b ...
              + r^3 * (q2 - 4 * a - 2 * q2 * a + q2 * a2 + 2 * a2 - 2 * b2 + 2) ...
              + r^2 * (4 * p * q * a - 2 * p * q * a * b + 2 * p * q * b ...
                      - 2 * p * q - 2 * p * q * a2) ...
              + r * (p2 * b2 - 2 * p2 * b + 2 * p2 * a * b - 2 * p2 * a ...
                    + p2 + p2 * a2)) * x ...
            + (2 * p * r2 - 2 * r^3 * q + p^3 - 2 * p2 * q * r + p * q2 * r2) * a2 ...
            + (p^3 - 2 * p * r2) * b2 ...
            + (4 * q * r^3 - 4 * p * r2 - 2 * p^3 + 4 * p2 * q * r - 2 * p * q2 * r2) * a ...
            + (-2 * q * r^3 + p * r^4 + 2 * p2 * q * r- 2 * p^3) * b ...
            + (2 * p^3 + 2 * q * r^3 - 2 * p2 * q * r) * a * b ...
            + p * q2 * r2 - 2 * p2 * q * r + 2 * p * r2 + p^3 - 2 * r^3 * q ...
            );

        if b0 <= 0
            continue
        end

        y = b0 / b1;
        u = x * x + y * y - x * y * r;

        if u <= 0
            continue
        end

        n = n + 1;
        Z = distances(3) / sqrt(u);
        X = x * Z;
        Y = y * Z;

        lengths(1, n) = X;
        lengths(2, n) = Y;
        lengths(3, n) = Z;
    end
end
