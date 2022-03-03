%%
clc;
clear;

addpath('fastquatmath');


%%
q = rand(1,4)
q1 = rand(1,4)
q2 = rand(1,4)
p = rand(3,1)

qconj = fquatconj(q)
qconj_ = quatconj(q)

qinv = fquatinv(q)
qinv_ = quatinv(q)
qequ = fquatmultiply(qinv, q)
qequ_ = quatmultiply(qinv_, q)

qmultiply = fquatmultiply(q1, q2)
qmultiply_ = quatmultiply(q1, q2)

p1 = fquatrotate(q, p)
p1_ = quatrotate(quatinv(q), p')


%%
times = 50000;


time_begin = clock;
for i=1:times
    q_inv = quatconj(q);
end
time_end = clock;
quatconj_average = etime(time_end,time_begin)*1000/times

time_begin = clock;
for i=1:times
    q_inv = fquatconj(q);
end
time_end = clock;
quatconj_average = etime(time_end,time_begin)*1000/times


time_begin = clock;
for i=1:times
    q_inv = quatinv(q);
end
time_end = clock;
quatinv_average = etime(time_end,time_begin)*1000/times

time_begin = clock;
for i=1:times
    q_inv = fquatinv(q);
end
time_end = clock;
quatinv_average = etime(time_end,time_begin)*1000/times


time_begin = clock;
for i=1:times
    q_normalized = quatnormalize(q);
end
time_end = clock;
quatnormalize_average = etime(time_end,time_begin)*1000/times

time_begin = clock;
for i=1:times
    q_normalized = fquatnormalize(q);
end
time_end = clock;
quatnormalize_average = etime(time_end,time_begin)*1000/times


time_begin = clock;
for i=1:times
    q_prod = quatmultiply(q1, q2);
end
time_end = clock;
quatmultiply_average = etime(time_end,time_begin)*1000/times

time_begin = clock;
for i=1:times
    q_prod = fquatmultiply(q1, q2);
end
time_end = clock;
quatmultiply_average = etime(time_end,time_begin)*1000/times


time_begin = clock;
for i=1:times
    p_new = quatrotate(q, p');
end
time_end = clock;
quatrotate_average = etime(time_end,time_begin)*1000/times

time_begin = clock;
for i=1:times
    p_new = fquatrotate(q, p);
end
time_end = clock;
quatrotate_average = etime(time_end,time_begin)*1000/times






