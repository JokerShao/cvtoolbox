function R = frvec2rotm(rvec)
    x=rvec(1,1); y=rvec(1,2); z=rvec(1,3);
    theta = sqrt(x*x+y*y+z*z);
    x=x/theta; y=y/theta; z=z/theta;
    ctheta=cos(theta); stheta=sin(theta);
    ctheta_d1 = 1-ctheta;

    R = [ctheta+ctheta_d1*x*x   ctheta_d1*x*y-stheta*z ctheta_d1*x*z+stheta*y;
         ctheta_d1*y*x+stheta*z ctheta+ctheta_d1*y*y   ctheta_d1*y*z-stheta*x;
         ctheta_d1*z*x-stheta*y ctheta_d1*z*y+stheta*x ctheta+ctheta_d1*z*z;
        ];
end

