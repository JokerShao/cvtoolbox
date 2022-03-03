function qnorm = fquatnormalize(q)
    % 1x4 w x y z order
    q0 = q(1,1);
    q1 = q(1,2);
    q2 = q(1,3);
    q3 = q(1,4);
    norm = sqrt(q0*q0+q1*q1+q2*q2+q3*q3);
    qnorm = q/norm;
end

