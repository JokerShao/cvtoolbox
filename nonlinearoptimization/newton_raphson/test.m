x0 = 10.5;
epsilon = 1e-20;
max1 = 1000;
delta = 1e-20;
f = 'fun';
% df = 'derivative';
% df = 'autoderivative';

[x, err, k, y] = newton(f, x0, delta, epsilon, max1)
