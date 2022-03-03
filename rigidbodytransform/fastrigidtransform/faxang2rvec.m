function rvec = faxang2rvec(axang)
    x=axang(1,1); y=axang(1,2); z=axang(1,3); theta=axang(1,4);
    rvec = [x*theta y*theta z*theta];
end

