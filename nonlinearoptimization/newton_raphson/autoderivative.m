function df = autoderivative(x)
    df = (fun(x+x*1e-2+1e-9) - fun(x)) / (x*1e-2+1e-9);
end