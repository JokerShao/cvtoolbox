% Extract K, R, t from Projection Martix
%
% by ftdlyc
%
% Input
% P: [3 x 4] Camera Projection Martix
%
% K =   k1   k11 k12 k13;
%       k2   k21 k22 k23;
%       k3   k31 k32 k33;
%
%             r1  r2  r3  t
% [ R t ] =   r11 r12 r13 t1;
%             r21 r22 r23 t2;
%             r31 r32 r33 t3;
%
% P =    k1r1 k1r2 k1r3 k1t;
%        k2r1 k2r2 k2r3 k2t;
%        k3r1 k3r2 k3r3 k3t;
%
% Output
% K: [3 x 3] Camera Intrinsic Matrix
% R: [3 x 3] Rotation Matrix
% t: [1 x 3] Translation Vector
%
function [K, R, t] = KRt_from_P(P)
%% QR decomposition
[K, R] = rqGivens(P(1:3, 1:3));

%% ensure that the diagonal is positive
if K(3, 3) < 0
    K = -K;
    R = -R;
end
if K(2, 2) < 0
    S = [1  0  0 
         0 -1  0
         0  0  1];
    K = K * S;
    R = S * R;
end
if K(1, 1) < 0
    S = [-1  0  0 
          0  1  0
          0  0  1];
    K = K * S;
    R = S * R;
end

%% ensure R determinant == 1
t = linsolve(K, P(:, 4));
% tt = K\P(:,4);

if det(R) < 0
    R = -R;
    t = -t;
end

K = K ./ K(3, 3);

end
