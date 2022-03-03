function q = frotm2quat(R)
    r11=R(1,1); r12=R(1,2); r13=R(1,3);
    r21=R(2,1); r22=R(2,2); r23=R(2,3);
    r31=R(3,1); r32=R(3,2); r33=R(3,3);

    q0 = sqrt(1+r11+r22+r33)/2;
    if q0<1e-8
        if max([r11,r22,r33])==r11
            t = sqrt(1+r11-r22-r33);
            q = [(r32-r23)/t t/4 (r13+r31)/t (r12+r21)/t];
        elseif max([r11,r22,r33])==r22
            t = sqrt(1-r11+r22-r33);
            q = [(r13-r31)/t (r12+r21)/t t/4 (r32+r23)/t];
        else
            t = sqrt(r11-r22+r33);
            q = [(r21-r12)/t (r13+r31)/t (r23-r32)/t t/4];
        end
    else
        q = [q0 (r32-r23)/(4*q0) (r13-r31)/(4*q0) (r21-r12)/(4*q0)];
    end
end

