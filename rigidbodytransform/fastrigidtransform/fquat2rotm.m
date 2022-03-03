function R = fquat2rotm(q)
    q0=q(1,1); q1=q(1,2); q2=q(1,3); q3=q(1,4);

    R = [1-2*q2*q2-2*q3*q3 2*q1*q2-2*q0*q3   2*q1*q3+2*q0*q2;
         2*q1*q2+2*q0*q3   1-2*q1*q1-2*q3*q3 2*q2*q3-2*q0*q1;
         2*q1*q3-2*q0*q2   2*q2*q3+2*q0*q1   1-2*q1*q1-2*q2*q2;
        ];
end

