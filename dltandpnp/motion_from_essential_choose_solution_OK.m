% Choose one of the four possible motion solutions from an essential matrix.
% see: Multiple View Geometry 1st edition. P175 (Chinese).
%
% Input:   RR1    [ 3 x 3 ]
%          RR2    [ 3 x 3 ]
%          tt     [ 3 x 1 ]
% Output:  R21    [ 3 x 3 ]
%          t21    [ 3 x 1 ]
%
% Author:  Zexi Shao
% Email:   zexishao@foxmail.com
% Date:    2020.05.17

function [R, t] = motion_from_essential_choose_solution_OK(RR1, RR2, tt)

    PP = [0 0 1 1]';
    perspective_matrix{1} = [RR1 tt];
    perspective_matrix{2} = [RR1 -tt];
    perspective_matrix{3} = [RR2 tt];
    perspective_matrix{4} = [RR2 -tt];

    for i=1:4
        pp = perspective_matrix{i} * PP;
        if pp(3) > 0
            break
        end
    end

    R = perspective_matrix{i}(:,1:3);
    t = perspective_matrix{i}(:,4);
end
