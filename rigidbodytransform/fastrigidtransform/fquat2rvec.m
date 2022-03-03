function rvec = fquat2rvec(q)
    q0=q(1,1); q1=q(1,2); q2=q(1,3); q3=q(1,4);
    norm = sqrt(q0*q0+q1*q1+q2*q2+q3*q3);
    q0=q0/norm; q1=q1/norm; q2=q2/norm; q3=q3/norm;

    theta = acos(q0)*2;
    if theta < 1e-10
        rvec = [1 0 0];
    else
        sth = sin(theta/2);
        x=q1/sth; y=q2/sth; z=q3/sth;
        rvec = [x*theta y*theta z*theta];
    end
end

