function R = faxang2rotm(axang)
    % convert use rodrigues' formula
    x=axang(1,1); y=axang(1,2); z=axang(1,3); theta=axang(1,4);
    ctheta=cos(theta); stheta=sin(theta);
    ctheta_d1 = 1-ctheta;

    R = [ctheta+ctheta_d1*x*x   ctheta_d1*x*y-stheta*z ctheta_d1*x*z+stheta*y;
         ctheta_d1*y*x+stheta*z ctheta+ctheta_d1*y*y   ctheta_d1*y*z-stheta*x;
         ctheta_d1*z*x-stheta*y ctheta_d1*z*y+stheta*x ctheta+ctheta_d1*z*z;
        ];
end

