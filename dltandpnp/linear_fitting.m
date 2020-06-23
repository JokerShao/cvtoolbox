close all;
clear;
clc;

% Ax = b
% kx1 + b = y1
% A (x1, 1)
% x (k, b)'
k = 2.56;
b = 8.33;

x1 = linspace(0, 200, 200)';
y1 = k*x1 + b;
noise_y1 = y1 + normrnd(0, 100, size(x1, 1), 1);

line(x1, y1);
hold on;

scatter(x1, noise_y1, 'b', 'x');
hold on;

A = [x1 ones(size(x1,1), 1)];

% 最小二乘
lq_x = inv(A'*A)*A'*y1

% 最小二乘
lq_x = A\y1

% 广义逆矩阵解法
lq_x = pinv(A)*y1

% svd解法
[U, D, V] = svd(A', 'econ')





% A = [x y];

% noise_A = A + normrnd(0, 3, size(x1, 1), 2);
% 
% 
% % V = [a1 a2]'
% [U, D, V] = svd(A, 'econ');
% 
% X = V(:,end);
% 
% scatter(A(:,1), A(:,2), 'b');
% hold on;
% 
