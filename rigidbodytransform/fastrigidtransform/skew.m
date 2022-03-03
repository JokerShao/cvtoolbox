function S = skew(v)
    % input 3x1 vector
    S = [0 -v(3,1) v(2,1);
         v(3,1) 0 -v(1,1);
         -v(2,1) v(1,1) 0;
        ];
end

