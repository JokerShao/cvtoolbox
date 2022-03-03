function p1 = fquatrotate(q, p)
    % p: [x y z] 3x1 vector
    % use formula: p1 = q*p*q^-1    p1 = R*p
    % Note: This is different with matlab!
    % matlab builtin function use formula:
    % p: [x y z] 1x3 vector
    % p1 = p*R
    q0=q(1,1); q1=q(1,2); q2=q(1,3); q3=q(1,4);
    norm = sqrt(q0*q0+q1*q1+q2*q2+q3*q3);
    q0=q0/norm; q1=q1/norm; q2=q2/norm; q3=q3/norm;

    x=p(1,1); y=p(2,1); z=p(3,1);

    p1 = [(1-2*q2*q2-2*q3*q3)*x + (2*q1*q2-2*q0*q3)*y + (2*q1*q3+2*q0*q2)*z;
          (2*q1*q2+2*q0*q3)*x + (1-2*q1*q1-2*q3*q3)*y + (2*q2*q3-2*q0*q1)*z;
          (2*q1*q3-2*q0*q2)*x + (2*q2*q3+2*q0*q1)*y + (1-2*q1*q1-2*q2*q2)*z;
         ];
end

