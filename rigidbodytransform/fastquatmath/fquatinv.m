function qinv = fquatinv(q)
    % 1x4 w x y z order
    q0=q(1,1); q1=q(1,2); q2=q(1,3); q3=q(1,4);
    norm2 = (q0*q0+q1*q1+q2*q2+q3*q3);
    qinv = [q0/norm2 -q1/norm2 -q2/norm2 -q3/norm2];
end

