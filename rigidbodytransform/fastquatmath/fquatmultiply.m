function q = fquatmultiply(q1, q2)
    sa = q1(1,1);
    xa = q1(1,2);
    ya = q1(1,3);
    za = q1(1,4);
    sb = q2(1,1);
    xb = q2(1,2);
    yb = q2(1,3);
    zb = q2(1,4);

    q = [sa*sb-xa*xb-ya*yb-za*zb ...
         sa*xb+xa*sb+ya*zb-za*yb ...
         sa*yb-xa*zb+ya*sb+za*xb ...
         sa*zb+xa*yb-ya*xb+za*sb ...
        ];
end

