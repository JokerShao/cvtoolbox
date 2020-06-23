% see: Multiple View Geometry 1st edition. P217 (Chinese)
%
% x = PX     x' = P'X
%
% Author:  Zexi Shao
% Email:   zexishao@foxmail.com
% Date:    2020.05.17

function X = linear_triangulation_methods(pts, P, ptsd, Pd)

    N = size(pts, 2);
    A = zeros(4*N, 4);

    for i = 1:N
        x = pts(i,1);    % x
        y = pts(i,2);    % y
        xd = ptsd(i, 1); % x'
        yd = ptsd(i, 2); % y'

        A(i*4-1:i*4, :) = [ x*P(3,:)'-P(1,:)';
                            y*P(3,:)'-P(2,:)';
                            xd*Pd(3,:)'-Pd(1,:)';
                            yd*Pd(3,:)'-Pd(2,:)'];
    end
    
    [~, ~, V] = svd(A, 'econ');
    
    X = V(:,end);
    X = X / X(end);
end







