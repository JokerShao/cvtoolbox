function axang = frvec2axang(rvec)
    x=rvec(1,1); y=rvec(1,2); z=rvec(1,3);
    theta = sqrt(x*x+y*y+z*z);
    axang = [x/theta y/theta z/theta theta];
end

