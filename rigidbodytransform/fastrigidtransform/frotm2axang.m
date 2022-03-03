function axang = frotm2axang(R)
    r11=R(1,1); r12=R(1,2); r13=R(1,3);
    r21=R(2,1); r22=R(2,2); r23=R(2,3);
    r31=R(3,1); r32=R(3,2); r33=R(3,3);

    theta = acos((r11+r22+r33-1)/2);
    tmp = 1/(2*sin(theta));
    x=tmp*(r32-r23); y=tmp*(r13-r31); z=tmp*(r21-r12);
    norm = sqrt(x*x+y*y+z*z);
    axang = [x/norm y/norm z/norm theta];
end

