% see: https://zhuanlan.zhihu.com/p/76361026
%      https://blog.csdn.net/jessecw79/article/details/82945918
% https://blog.csdn.net/App_12062011/article/details/82182489
%      https://zhuanlan.zhihu.com/p/59070440


function [Rcw, tcw] = pnp_solver_epnp(Pts, pts)

    % Cw:  control point in world frame
    % Cc:  control point in camera frame
    % Pw : point in world frame
    % Pc:  point in camera frame
    % p:   pixel position
%% check data
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
%% select control points
    Cw(:,1) = mean(Pts, 2);
    A = Pts'-Cw(:,1)';
    
    [V, D] = eig(A'*A);
    
    n = size(Pts, 2);
    
    for j=2:4
        Cw(:,j) = Cw(:,1) + sqrt(D(j-1, j-1)/n)*V(:,j-1);
    end
    
        
    plot3(Pts(1,:), Pts(2,:), Pts(3,:), 'b*')
    hold on
    plot3(Cw(1,:), Cw(2,:), Cw(3,:), 'r*');
    

%% compute barycentric coordinates
% alpha: 4 x n matrix
% [P; 1] = [Cw; 1] * alpha
alpha = inv([Cw; ones(1, 4)]) * [Pts; ones(1, n)];

%% compute Cc
fx = 1;
fy = 1;
cx = 0;
cy = 0;
M = zeros(2 * n, 12);
for i = 1:n
    M(2 * i - 1, :) = [alpha(1, i) * fx, 0, alpha(1, i) * (cx - pts(1, i)) ...
                       alpha(2, i) * fx, 0, alpha(2, i) * (cx - pts(1, i)) ...
                       alpha(3, i) * fx, 0, alpha(3, i) * (cx - pts(1, i)) ...
                       alpha(4, i) * fx, 0, alpha(4, i) * (cx - pts(1, i))];
    M(2 * i, :) = [0, alpha(1, i) * fy, alpha(1, i) * (cy - pts(2, i)) ...
                   0, alpha(2, i) * fy, alpha(2, i) * (cy - pts(2, i)) ...
                   0, alpha(3, i) * fy, alpha(3, i) * (cy - pts(2, i)) ...
                   0, alpha(4, i) * fy, alpha(4, i) * (cy - pts(2, i))];
end

[~, S, V] = svd(M, 'econ');


%% compute V
% compute L_6x10 and rho
% betas10 = [b11 b12 b22 b13 b23 b33 b14 b24 b34 b44]
% beta = [b11 b12 b22 b13 b23 b33 b14 b24 b34 b44]  bij = bi*bj
% L = [l12'; l13'; l14'; l23'; l24'; l34';]
v = zeros(12, 4);
v(:, 1) = V(:, 12);
v(:, 2) = V(:, 11);
v(:, 3) = V(:, 10);
v(:, 4) = V(: , 9);

s = cell(4, 6);
for i = 1:4
    vtmp1 = v(1:3, i);
    vtmp2 = v(4:6, i);
    vtmp3 = v(7:9, i);
    vtmp4 = v(10:12, i);
    s{i, 1} = vtmp1 - vtmp2;
    s{i, 2} = vtmp1 - vtmp3;
    s{i, 3} = vtmp1 - vtmp4;
    s{i, 4} = vtmp2 - vtmp3;
    s{i, 5} = vtmp2 - vtmp4;
    s{i, 6} = vtmp3 - vtmp4;
end

% L_6x10 * beta_10x1 = rho_6x1
L = zeros(6, 10);
for i = 1:6
    L(i, :) = [    s{1, i}' * s{1, i} ...
               2 * s{1, i}' * s{2, i} ...
                   s{2, i}' * s{2, i} ...
               2 * s{1, i}' * s{3, i} ...
               2 * s{2, i}' * s{3, i} ...
                   s{3, i}' * s{3, i} ...
               2 * s{1, i}' * s{4, i} ...
               2 * s{2, i}' * s{4, i} ...
               2 * s{3, i}' * s{4, i} ...
                   s{4, i}' * s{4, i}];
end

% 12 13 14 23 24 34
rho = [ norm(Cw(:,1)-Cw(:,2));
        norm(Cw(:,1)-Cw(:,3));
        norm(Cw(:,1)-Cw(:,4));
        norm(Cw(:,2)-Cw(:,3));
        norm(Cw(:,2)-Cw(:,4));
        norm(Cw(:,3)-Cw(:,4))];

err = 1e88;
%% case N=1
% compute beta (N = 1)
% find betas
betas = zeros(4, 1);
b1 = linsolve(L(:, 1), rho);
betas(1) = sqrt(abs(b1));

betas = gauss_newton(L, rho, betas);

Xc = compute_Xc(alpha, betas, v);
[R1, t1] = compute_Rt(Pts, Xc);
err1 = reproject_error(Pts, pts(1:2,:), R1, t1);

if err1 < err
    err = err1;
    R = R1;
    t = t1;
end

%% compute beta (N = 2)
% betas10 = [b11 b12 b22 b13 b23 b33 b14 b24 b34 b44]
% b3      = [b11 b12 b22]
% find beta
betas = zeros(4, 1);
b3 = linsolve(L(:, 1:3), rho);
betas(1) = sqrt(abs(b3(1)));
betas(2) = sqrt(abs(b3(3))) * sign(b3(2)) * sign(b3(1));

betas = gauss_newton(L, rho, betas);

Xc = compute_Xc(alpha, betas, v);
[R2, t2] = compute_Rt(Pts, Xc);

err2 = reproject_error(Pts, pts(1:2,:), R2, t2);
if err2 < err
    err = err2;
    R = R2;
    t = t2;
end

%% compute beta (N = 3)
% b6      = [b11 b12 b22 b13 b23 b33]
% find beta
betas = zeros(4, 1);
b6 = linsolve(L(:, 1:6), rho);
betas(1) = sqrt(abs(b6(1)));
betas(2) = sqrt(abs(b6(3))) * sign(b6(2)) * sign(b6(1));
betas(3) = sqrt(abs(b6(6))) * sign(b6(4)) * sign(b6(1));

betas = gauss_newton(L, rho, betas);

Xc = compute_Xc(alpha, betas, v);
[R3, t3] = compute_Rt(Pts, Xc);

err3 = reproject_error(Pts, pts(1:2,:), R3, t3);
if err3 < err
    err = err3;
    R = R3;
    t = t3;
end

% case N = 4
%% compute beta (N = 4)
% betas10 = [b11 b12 b22 b13 b23 b33 b14 b24 b34 b44]
% b4      = [b11 b12     b13         b14]
% find beta
betas = zeros(4, 1);
b4 = linsolve([L(:, 1), L(:, 2), L(:, 4), L(:, 7)], rho);
betas(1) = sqrt(abs(b4(1)));
betas(2) = b4(2) / betas(1);
betas(3) = b4(3) / betas(1);
betas(4) = b4(4) / betas(1);

betas = gauss_newton(L, rho, betas);

Xc = compute_Xc(alpha, betas, v);
[R4, t4] = compute_Rt(Pts, Xc);

err4 = reproject_error(Pts, pts(1:2,:), R4, t4);
if err4 < err
    err = err4;
    R = R4;
    t = t4;
end

Rcw = R;
tcw = t;



    
    
    



end


function betas = gauss_newton(L, rho, betas)
n_iter = 5;
for i = 1:n_iter
    % 6 x 10
    % err 12, 13, 14, 23, 24, 34
    % betas 11 12 22 13 23 33 14 24 34 44
    J = zeros(6, 4);
    for j = 1:6
        J(j, 1) = 2 * L(j, 1) * betas(1) +     L(j, 2) * betas(2) +     L(j, 4) * betas(3) +     L(j, 7) * betas(4);
        J(j, 2) =     L(j, 2) * betas(1) + 2 * L(j, 3) * betas(2) +     L(j, 5) * betas(3) +     L(j, 8) * betas(4);
        J(j, 3) =     L(j, 4) * betas(1) +     L(j, 5) * betas(2) + 2 * L(j, 6) * betas(3) +     L(j, 9) * betas(4);
        J(j, 4) =     L(j, 7) * betas(1) +     L(j, 8) * betas(2) +     L(j, 9) * betas(3) + 2 * L(j, 10) * betas(4);
    end
    
    % 6 x 1
    % err 12, 13, 14, 23, 24, 34
    r = zeros(6, 1);
    for j = 1:6
        r(j) = rho(j) ...
             - L(j, 1) * betas(1) * betas(1) ...
             - L(j, 2) * betas(1) * betas(2) ...
             - L(j, 3) * betas(2) * betas(2) ...
             - L(j, 4) * betas(1) * betas(3) ...
             - L(j, 5) * betas(2) * betas(3) ...
             - L(j, 6) * betas(3) * betas(3) ...
             - L(j, 7) * betas(1) * betas(4) ...
             - L(j, 8) * betas(2) * betas(4) ...
             - L(j, 9) * betas(3) * betas(4) ...
             - L(j, 10) * betas(4) * betas(4);
    end 
    
    A = J' * J;
    b = J' * r;
    dbetas = linsolve(A, b);
    
    betas = betas + dbetas;
end
end

function Xc = compute_Xc(alpha, betas, v)
x = betas(1) * v(:, 1) + betas(2) * v(:, 2) + betas(3) * v(:, 3) + betas(4) * v(:, 4);
C = [x(1:3, 1), x(4:6, 1), x(7:9, 1), x(10:12, 1)];
Xc = C * alpha;
end

function [R, t] = compute_Rt(Xw, Xc)
mean_Xw = mean(Xw, 2);
mean_Xc = mean(Xc, 2);

new_Xw = Xw - mean_Xw;
new_Xc = Xc - mean_Xc;

W = zeros(3, 3);
for j = 1:size(Xw, 2)
    W = W + new_Xc(:, j) * new_Xw(:, j)'; 
end
    
[U, ~, V] = svd(W);
R = U * V';
t = mean_Xc - R * mean_Xw;
end

function err = reproject_error(X, x, R, t)
x2 = R * X + t;
for i = 1:size(X, 2)
    x2(:, i) = x2(:, i) ./ x2(3, i);
end
x2 = x2(1:2, :);
err = mean(sqrt(sum((x2 - x).^2, 1)));
end
