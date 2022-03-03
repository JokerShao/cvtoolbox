function q = frvec2quat(rvec)
    x=rvec(1,1); y=rvec(1,2); z=rvec(1,3);
    theta = sqrt(x*x+y*y+z*z);
    sht = sin(theta/2);
    q = [cos(theta/2) x/theta*sht y/theta*sht z/theta*sht];
end

