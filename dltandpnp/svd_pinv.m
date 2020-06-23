
% d = rand(5,1);
% D = diag(d);
% Dinv = inv(D);
% 
% A = rand(10,7)
% 
% [U, D, V] = svd(A, 'econ');
% 
% U*D*V'
% 
% 
% myApinv = V*inv(D)*U';
% Apinv = pinv(A);
% 
% A*Apinv
% Apinv*A

K = [700 0 1280/2;
     0 700 720/2;
     0 0 1];
I = eye(3);

P = K * [I zeros(3,1)];

Pplus = P'*inv(P*P')
P*Pplus

normPplus = inv(P'*P)*P'
P*normPplus






% 奇异值分解
% [U，S，V]=SVD（X）产生一个对角线矩阵S，其维数与X相同，且非负对角线元素按降序排列，酉矩阵U和V使得X=U*S*V'。
% S=SVD（X）返回包含奇异值的向量。
%
% [U，S，V]=SVD（X，0）产生“经济规模”分解。如果X是m>n的m-by-n，则只计算U的前n列，S是n-by-n。对于m<=n，SVD（X，0）等于SVD（X）。
%
% [U，S，V]=SVD（X，'econ'）也会产生“经济规模”分解。如果X是m-by-n且m>=n，则它等价于SVD（X，0）。对于m<n，只计算V的前m列，S是m-by-m。
%
% 另见SVD、GSVD。
% 版权所有1984-2005 The MathWorks，Inc。
% 内置功能。

% 广义逆矩阵计算 多视几何第一版 节A3.4 P410
clear;
clc;

A = rand(8, 5);

Aplus = pinv(A)

[U, D, V] = svd(A, 'econ');
myAplus = V*inv(D)*U'

othermyAplus = inv(A'*A)*A'

Aplus*A
myAplus*A
othermyAplus*A