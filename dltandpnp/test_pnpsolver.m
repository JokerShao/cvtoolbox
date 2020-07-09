%% test perspective-n-point problem
% see: https://blog.csdn.net/App_12062011/article/details/52039981?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522159220491419195264564845%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=159220491419195264564845&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_v1~rank_blog_v1-4-52039981.pc_v1_rank_blog_v1&utm_term=%E7%9B%B8%E6%9C%BA%E5%A7%BF%E6%80%81%E4%BC%B0%E8%AE%A1
clc;
clear;

fprintf('---------------------------PNP test---------------------------\n\n');

A = rand(3, 3);
t = rand(3, 1);
[R, ~] = qr(A);
P = [R, t];

npoints = 6;
X = rand(3, npoints);
X(4, :) = ones(1, npoints);

x = P * X;
for i = 1:npoints
    x(:, i) = x(:, i) ./ x(3, i);
end

errors = zeros(npoints, 4);

fprintf('number of points = %d\n', npoints);

%% add noise
std = 0.000;
noise = normrnd(0, std, 3, npoints);
X_noise = X;
X_noise(1:3, :) = X_noise(1:3, :) + noise;

% P_norm = P ./ P(3, 4);
fprintf('noise std = %f\n\n', std);

%% PNP DTL
fprintf('---------------------------PNP DLT---------------------------\n\n');

P_est = pnp_solver_dlt(X_noise(1:3,:), x(1:2,:));
[K_est, R_est, t_ests] = KRt_from_P(P_est);

display(R, t, R_est, t_ests);

x_est = [R_est, t_ests] * X;
for i = 1:npoints
    x_est(:, i) = x_est(:, i) ./ x_est(3, i);
end
errors(:, 1) = sqrt(sum((x_est  - x).^2, 1))';
fprintf('reproject error = %f\n\n', mean(errors(:, 1)));

%% PNP POSIT
fprintf('---------------------------PNP POSIT---------------------------\n\n');

[R_est, t_ests] = pnp_solver_posit(X_noise(1:3,:), x(1:2,:), 1);

display(R, t, R_est, t_ests);

x_est = [R_est, t_ests] * X;
for i = 1:npoints
    x_est(:, i) = x_est(:, i) ./ x_est(3, i);
end
errors(:, 2) = sqrt(sum((x_est  - x).^2, 1))';
fprintf('reproject error = %f\n\n', mean(errors(:, 2)));

%% PNP P3P
fprintf('---------------------------PNP P3P---------------------------\n\n');

[R_ests, t_ests] = pnp_solver_p3p(X_noise(:, 1:3), x(:, 1:3));

if size(R_ests, 1) ~= 0
    min_err = 1e10;
    min_i = 0;
    for i = 1:size(R_ests, 2)
        R_est = R_ests{i};
        t_est = t_ests{i};

        angle_axis = rodrigues(R);
        angle_axis_est = rodrigues(R_est);
        err = sum(sum((angle_axis - angle_axis_est).^2)) + sum((t - t_est).^2);
        if err < min_err
            min_i = i;
            min_err = err;
        end
    end

    display(R, t, R_ests{min_i}, t_ests{min_i});

    x_est = [R_ests{min_i}, t_ests{min_i}] * X;
    for i = 1:npoints
        x_est(:, i) = x_est(:, i) ./ x_est(3, i);
    end
    errors(:, 3) = sqrt(sum((x_est  - x).^2, 1))';
    fprintf('reproject error = %f\n\n', mean(errors(:, 3)));
else
    fprintf('p3p failed\n\n');
end

%{
%% PNP EPnP
[Rcw, tcw] = pnp_solver_epnp(X, x);
angle_axis = rodrigues(R);
angle_axis_est = rodrigues(Rcw);

fprintf('angle_axis = \n')
disp(angle_axis')
fprintf('angle_axis_est = \n')
disp(angle_axis_est')
fprintf('t = \n')
disp(t')
fprintf('t_est = \n')
disp(tcw')


fprintf('---------------------------PNP EPnP---------------------------\n\n')

P_est = solve_pnp_epnp(X_noise, x);
[K_est, R_est, t_ests] = KRt_from_P(P_est);

angle_axis = rodrigues(R);
angle_axis_est = rodrigues(R_est);

fprintf('angle_axis = \n')
disp(angle_axis')
fprintf('angle_axis_est = \n')
disp(angle_axis_est')
fprintf('t = \n')
disp(t')
fprintf('t_est = \n')
disp(t_ests')

x_est = [R_est, t_ests] * X;
for i = 1:npoints
    x_est(:, i) = x_est(:, i) ./ x_est(3, i);
end
errors(:, 3) = sqrt(sum((x_est  - x).^2, 1))';
fprintf('reproject error = %f\n\n', mean(errors(:, 3)))
%}

%% PNP AP3P
fprintf('---------------------------PNP AP3P---------------------------\n\n')

P_est = solve_pnp_ap3p(X_noise(:, 1:3), x(:, 1:3));

if size(P_est, 1) ~= 0
    min_err = 1e10;
    min_i = 0;
    for i = 1:size(P_est, 2)
        [~, R_est, t_ests] = KRt_from_P(P_est{i});

        angle_axis = rodrigues(R);
        angle_axis_est = rodrigues(R_est);
        err = sum(sum((angle_axis - angle_axis_est).^2)) + sum((t - t_ests).^2);
        if err < min_err
            min_i = i;
            min_err = err;
        end
    end
    
    [K_est, R_est, t_ests] = KRt_from_P(P_est{min_i});
    
    angle_axis = rodrigues(R);
    angle_axis_est = rodrigues(R_est);
    
    fprintf('angle_axis = \n')
    disp(angle_axis')
    fprintf('angle_axis_est = \n')
    disp(angle_axis_est')
    fprintf('t = \n')
    disp(t')
    fprintf('t_est = \n')
    disp(t_ests')

    x_est = [R_est, t_ests] * X;
    for i = 1:npoints
        x_est(:, i) = x_est(:, i) ./ x_est(3, i);
    end
    errors(:, 4) = sqrt(sum((x_est  - x).^2, 1))';
    fprintf('reproject error = %f\n\n', mean(errors(:, 4)))
else
    fprintf('ap3p failed\n\n')
end

boxplot(errors)


function display(R, t, R_est, t_est)

    angle_axis = rodrigues(R);
    angle_axis_est = rodrigues(R_est);

    fprintf('ground truth angle_axis, t\n');
    disp([angle_axis' t']);
    fprintf('estimate angle_axis, t\n');
    disp([angle_axis_est' t_est']);
    
%     fprintf('angle_axis = \n');
%     disp(angle_axis');
%     fprintf('angle_axis_est = \n');
%     disp(angle_axis_est');
%     fprintf('t = \n');
%     disp(t');
%     fprintf('t_est = \n');
%     disp(t_est');
end




