function q = faxang2quat(axang)
    x=axang(1,1); y=axang(1,2); z=axang(1,3); theta=axang(1,4);
    sth = sin(theta/2);
    q = [cos(theta/2) x*sth y*sth z*sth];
end

