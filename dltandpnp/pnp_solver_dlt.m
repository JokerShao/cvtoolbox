% Perspective-n-Point problem, Direct linear transform(DLT) algorithm.
% The solution will degenerate in the plane case.
% see: Multiple View Geometry 1st edition. P122 (Chinese).
%
% Input:  Pts [3 x N]
%         pts [2 x N]
% Output: Perspective matrix
%
% Author:      Zexi Shao
% Email:       zexishao@foxmail.com
% Date:        2020.05.13
% Last modify: 2020.06.15

function P = pnp_solver_dlt(Pts, pts)

    N = size(Pts, 2);
    A = zeros(2*N, 12);

    for i = 1:N
        P_homo = [Pts(:, i)' 1];
        u1 = pts(1,i);
        v1 = pts(2,i);

        A(2*i-1:2*i,:) = [ P_homo      zeros(1, 4)   -u1*P_homo;
                           zeros(1, 4) P_homo        -v1*P_homo];
    end

    [~, ~, V] = svd(A, 'econ');
    T_v = V(:, end);
    % MATLAB stores these elements with a column-major array layout.
    P = reshape(T_v, 4, 3)';

end

% function P = pnp_solver_dlt(Pts, pts, invK)
% 
%     N = size(Pts, 2);
%     A = zeros(2*N, 12);
% 
%     for i = 1:N
%         P_homo = [Pts(:, i)' 1];
%         p = invK*[pts(:, i); 1];
%         u1 = p(1)/p(3);
%         v1 = p(2)/p(3);
% 
%         A(2*i-1:2*i,:) = [ P_homo      zeros(1, 4)   -u1*P_homo;
%                            zeros(1, 4) P_homo        -v1*P_homo];
%     end
% 
%     [~, ~, V] = svd(A, 'econ');
%     T_v = V(:, end);
%     % MATLAB stores these elements with a column-major array layout.
%     T = reshape(T_v, 4, 3)';
%     
%     P = T;
% % 
% %     if det(T(:,1:3)) < 0
% %         T = -T;
% %     end
% % 
% %     [R, r] = qr(T(:, 1:3));
% %     for i=1:3
% %         R(:,i) = R(:,i) * sign(r(i,i));
% %     end
% % 
% %     t = T(:, 4) / abs(r(1,1));
% end