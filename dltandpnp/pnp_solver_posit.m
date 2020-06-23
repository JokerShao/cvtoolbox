% Perspective-n-Point problem
% Pose from Orthography and Scaling with Iterations algorithm.
% see: https://blog.csdn.net/App_12062011/article/details/52040016?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522159220491419195264564845%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=159220491419195264564845&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_v1~rank_blog_v1-5-52040016.pc_v1_rank_blog_v1&utm_term=%E7%9B%B8%E6%9C%BA%E5%A7%BF%E6%80%81%E4%BC%B0%E8%AE%A1
% Input:  Pts [3 x N]
%         pts [2 x N]
% Output: Rcw, tcw
%
% Author:      Zexi Shao
% Email:       zexishao@foxmail.com
% Date:        2020.06.15
% Last modify: 2020.06.15

function [R, t] = pnp_solver_posit(Pts, pts, f)

    N = size(Pts, 2);
    Pts_homo = [Pts; ones(1, N)];

    R = [];
    t = [];

    %% initial
    A = zeros(2*N, 8);
    b = zeros(2*N, 1);
    w = 1;

    for i = 1:N
        A(2*i-1:2*i,:) = [Pts_homo(:,i)' zeros(1,4);
                          zeros(1,4) Pts_homo(:,i)'];
        b(2*i-1:2*i, 1) = w*pts(:,i);
    end

    x = linsolve(A, b);

    sR1 = x(1:3,1);
    sR2 = x(4:6,1);
    sTxy = x(7:8,1);

    s1 = norm(sR1);
    s2 = norm(sR2);
    s = sqrt(s1*s2);

    R1 = sR1 / norm(sR1);
    R2 = sR2 / norm(sR2);
    R3 = cross(R1, R2);
    R3 = R3 / norm(R3);
    R = [R1'; R2'; R3'];

    Txy = sTxy/s;
    Tz = f / s;
    t = [Txy; Tz];
    
    %% iteration
    for i = 1:100
        A = zeros(2*N, 8);
        b = zeros(2*N, 1);

        for i = 1:N
            
            Zc = [R3' Tz] * Pts_homo(:,i);
            w = Zc / Tz;

            A(2*i-1:2*i,:) = [Pts_homo(:,i)' zeros(1,4);
                              zeros(1,4) Pts_homo(:,i)'];
            b(2*i-1:2*i, 1) = w*pts(:,i);
        end

        x = linsolve(A, b);

        sR1 = x(1:3,1);
        sR2 = x(4:6,1);
        sTxy = x(7:8,1);

        s1 = norm(sR1);
        s2 = norm(sR2);
        s = sqrt(s1*s2);

        R1 = sR1 / norm(sR1);
        R2 = sR2 / norm(sR2);
        R3 = cross(R1, R2);
        R = [R1'; R2'; R3'];

        Txy = sTxy/s;
        Tz = f / s;
        t = [Txy; Tz];
    end

        

end

