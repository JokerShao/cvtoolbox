%%
clc;
clear;

addpath('fastrigidtransform');


%%
A = rand(3,3)
[R, ~] = qr(A)
p = rand(3,1)

Rtoquat = frotm2quat(R)
quattoaxang = fquat2axang(Rtoquat)
axangtorotm = faxang2rotm(quattoaxang)
rotmtoaxang = frotm2axang(axangtorotm)
axangtoquat = faxang2quat(rotmtoaxang)
quattorotm = fquat2rotm(axangtoquat)

Rtoquat_ = rotm2quat(R)
quattoaxang_ = quat2axang(Rtoquat_)
axangtorotm_ = axang2rotm(quattoaxang_)
rotmtoaxang_ = rotm2axang(axangtorotm_)
axangtoquat_ = axang2quat(rotmtoaxang_)
quattorotm_ = quat2rotm(axangtoquat_)


p1 = R*p
p2 = fquatrotate(axangtoquat, p)


%% test rvec
rvec = rand(1,3)

rvectoaxang = frvec2axang(rvec)
axangtorvec = faxang2rvec(rvectoaxang)

rvectoquat = frvec2quat(rvec)
quattorvec = fquat2rvec(rvectoquat)

rvectorotm = frvec2rotm(rvec)
rotmtorvec = frotm2rvec(rvectorotm)


%%
clc;
clear;
close all;

times = 50000;
axang = rand(1,4);
quat = rand(1,4);
A = rand(3,3);
[R, ~] = qr(A);
rvec = rand(1,3);

time_begin = clock;
for i=1:times
%     x = faxang2quat(quat);
%     x = faxang2rotm(quat);
%     x = faxang2rvec(quat);

%     x = fquat2axang(axang);
%     x = fquat2rotm(axang);

%     x = frotm2axang(R);
%     x = frotm2quat(R);
    x = frotm2rvec(R);
end
time_end = clock;
t1 = etime(time_end,time_begin)*1000/times

time_begin = clock;
for i=1:times
%     x = axang2quat(quat);
%     x = axang2rotm(quat);
%     x = axang2rvec(quat);

%     x = quat2axang(axang);
%     x = quat2rotm(axang);

%     x = rotm2axang(R);
%     x = rotm2quat(R);
end
time_end = clock;
t1 = etime(time_end,time_begin)*1000/times

