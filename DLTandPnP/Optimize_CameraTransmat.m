function [R,T]=Optimize_CameraTransmat(A,invK,kc,q_init,T_init)


a0=[q_init;T_init];

Data{1,1}=A;
Data{2,1}=invK;
Data{3,1}=kc;


options=optimset('TolX',1e-6,'Algorithm','Levenberg-Marquardt',...
 'Display','iter','MaxIter',20);

[a,~]=lsqnonlin(@Optimizing_CameraTransmat,a0,[],[],options,Data);


q=a(1:4);
q=q/norm(q);
T=a(5:7);
R=quatern2rotMat(q);

%K=a(8:12);

figure
Show_TransMat2(A,invK,R,T,kc);



end




function E=Optimizing_CameraTransmat(a,Data)


q=a(1:4);
q=q/norm(q);
T=a(5:7);


R=quatern2rotMat(q);

A=Data{1};
invK=Data{2};
kc=Data{3};


for i=1:size(A,1)
    
    W=[A(i,1:2),0]';  % 点在世界坐标系下地面的坐标
    P=A(i,3:4);
    U=invK*[P,1]';
    
    U2 =[ comp_distortion_oulu(U(1:2),kc);1];
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%
    V=R*U2;  % 点转到世界坐标系，投影点在世界坐标系下的坐标，这个点一定在射线上
    
    V2=W-T;   % 拿到一条射线方向 世界点到相机
    
    Skew_V2=[  0  ,-V2(3), V2(2);...
             V2(3),  0  ,-V2(1) ;...
            -V2(2), V2(1),  0     ];
        
        % 叉乘
    E(i,1)=norm(Skew_V2*V)^2    ;
    
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%     UU=R'*(W-T);
%     
%     
%     E(2*i-1,1)=UU(1)/UU(3)-U2(1);
%     E(2*i,1)=UU(2)/UU(3)-U2(2);
% 

    
    
end




end