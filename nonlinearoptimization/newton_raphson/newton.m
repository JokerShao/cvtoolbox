function [x0, err, k, y] = newton(f, x0, delta, epsilon, max1)
    for k = 1:max1
        x1 = x0 - feval(f, x0) / autoderivative(x0);
        err = abs(x1-x0);
        relerr = 2*err/(abs(x1)+delta);
        x0 = x1;
        y = feval(f, x0);
        if (err<delta) | (relerr<delta) | (abs(y)<epsilon), break, end
    end
end