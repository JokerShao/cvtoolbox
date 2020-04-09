function [R,T]=Get_inital_R_T(A,invK,kc)

B=[];

for i=1:size(A,1)
    
    W=[A(i,1:2),1];
    P=A(i,3:4);
    U=invK*[P,1]';
    
    U2 = comp_distortion_oulu(U(1:2),kc);
    
    
    temp_B=[  W   ,[0,0,0],-U2(1)*W;...
           [0,0,0],   W   ,-U2(2)*W];
    
    
    B=[B;temp_B];  
    
    
end

AA=B'*B;

[UU,SS,VV] = svd(AA);

t=UU(:,end);

%B*T


R1=[t(1);t(4);t(7)];
temp_T=[t(3);t(6);t(9)]/norm(R1);
R1=R1/norm(R1);
R2=[t(2);t(5);t(8)];
R2=R2-(R1'*R2)*R1;
R2=R2/norm(R2);
R3=cross(R1,R2);
R=[R1,R2,R3]';

T=-R*temp_T;

end