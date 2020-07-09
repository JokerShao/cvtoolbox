% Perspective-n-Point problem, ap3p algorithm.
% Reference: http://openaccess.thecvf.com/content_cvpr_2017/papers/Ke_An_Efficient_Algebraic_CVPR_2017_paper.pdf
%
% Input:   Pts  [3 x N]
%          pts  [2 x N]
%
% Output:  Rcw  [3 x 3]
%          tcw  [3 x 1]
%
% Author:      Zexi Shao
% Email:       zexishao@foxmail.com
% Date:        2020.06.15
% Last modify: 2020.06.15

function pnp_solver_ap3p(Pts, pts)

    Pg1 = Pts(:,1);
    Pg2 = Pts(:,2);
    Pg3 = Pts(:,3);
    bc1 = pts(:,1);
    bc2 = pts(:,2);
    bc3 = pts(:,3);
    
    k1 = Pg1-Pg2;
    k1 = k1 / norm(k1);
    
    k3 = cross(bc1, bc2);
    k3 = k3/ norm(k3);
    
    k2 = cross(k1, k3);
    k2 = k2 / norm(k2);
    
    theta2_1 = acos(k1'*k3) + pi/2;
    theta2_2 = acos(k1'*k3) - pi/2;
    
    u1 = Pg1 - Pg3;
    u2 = Pg2 - Pg3;
    v1 = cross(bc1, bc3);
    v2 = cross(bc2, bc3);
    
    Ck2theta2 = rodrigues(k2, theta2_1);
    
    v1d = Ck2theta2 * v1;
    v2d = Ck2theta2 *v2;
    k3d = Ck2theta2*k3;
    
    delta = norm(u1*k1)
    
    ;;








end








