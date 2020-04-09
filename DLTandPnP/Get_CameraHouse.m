function [CameraHouse]=Get_CameraHouse(invK,kc,A1,A2,A3,A4)









[R1_init,T1_init]=Get_inital_R_T(A1,invK{1},kc{1});
q1_init= rotMat2qRichard(R1_init)';

[R2_init,T2_init]=Get_inital_R_T(A2,invK{2},kc{2});
q2_init= rotMat2qRichard(R2_init)';

[R3_init,T3_init]=Get_inital_R_T(A3,invK{3},kc{3});
q3_init= rotMat2qRichard(R3_init)';

[R4_init,T4_init]=Get_inital_R_T(A4,invK{4},kc{4});
q4_init= rotMat2qRichard(R4_init)';

%%

[R1,T1]=Optimize_CameraTransmat(A1,invK{1},kc{1},q1_init,T1_init);
%%

[R2,T2]=Optimize_CameraTransmat(A2,invK{2},kc{2},q2_init,T2_init);
%%


[R3,T3]=Optimize_CameraTransmat(A3,invK{3},kc{3},q3_init,T3_init);
%%

[R4,T4]=Optimize_CameraTransmat(A4,invK{4},kc{4},q4_init,T4_init);


%%
figure
Show_TransMat2(A1,invK{1},R1,T1,kc{1});
Show_TransMat2(A2,invK{2},R2,T2,kc{2});
Show_TransMat2(A3,invK{3},R3,T3,kc{3});
Show_TransMat2(A4,invK{4},R4,T4,kc{4});

%%

CameraHouse{1,1}=[R1,T1];
CameraHouse{2,1}=[R2,T2];
CameraHouse{3,1}=[R3,T3];
CameraHouse{4,1}=[R4,T4];










end



function E=Get_CameraHouse_Loss(a,Data)

data=Data{1};
invK=Data{2};
R1=Data{3};
T1=Data{4};

q2=a(1:4);
q2=q2/norm(q2);
R2=quatern2rotMat(q2);
T2=a(5:7);
q3=a(8:11);
q3=q3/norm(q3);
R3=quatern2rotMat(q3);
T3=a(12:14);
q4=a(15:18);
q4=q4/norm(q4);
R4=quatern2rotMat(q4);
T4=a(19:21);


T2(1)=2;

CameraHouse{1,1}=[R1,T1];
CameraHouse{2,1}=[R2,T2];
CameraHouse{3,1}=[R3,T3];
CameraHouse{4,1}=[R4,T4];

L_shoulder=0.41;
L_upperarm=0.26;
L_forearm=0.24;
L_Lap=0.38;
L_shank=0.35;
L_hip=0.26;


Joint_id=[3,4,5,6,7,8,10,11,12,13,14,15];
%         1,2,3,4,5,6, 7, 8, 9,10,11,12




for i=1:size(data{1},1)
    for j=1:length(Joint_id)
        
        id=Joint_id(j);
        for s=1:length(data)
        
            P{s}=data{s}(i,id*3-2:id*3-1);
       
        end
        
        X(:,j)=Location_Joint(CameraHouse,P,invK);
        
        E_VML(:,j)=Vector_Meet_Loss(CameraHouse,P,invK);
        
    
    end
    
    left_upperarm=norm(X(:,1)-X(:,2));
    left_forearm=norm(X(:,2)-X(3));
    shoulder=norm(X(:,1)-X(:,4));
    right_upperarm=norm(X(:,4)-X(:,5));
    right_forearm=norm(X(:,5)-X(:,6));
    hip=norm(X(:,7)-X(:,10));
    left_lap=norm(X(:,7)-X(:,8));
    left_shank=norm(X(:,8)-X(:,9));
    right_lap=norm(X(:,10)-X(:,11));
    right_shank=norm(X(:,11)-X(:,12));
    
%     E(i,1)=left_upperarm-L_upperarm;
%     E(i,2)=left_forearm-L_forearm;
%     E(i,3)=shoulder-L_shoulder;
%     E(i,4)=right_upperarm-L_upperarm;
%     E(i,5)=right_forearm-L_forearm;
%     E(i,6)=hip-L_hip;
%     E(i,7)=left_lap-L_Lap;
%     E(i,8)=left_shank-L_shank;
%     E(i,9)=right_lap-L_Lap;
%     E(i,10)=right_shank-L_shank;
    
    E(i,1)=0;
    E(i,2)=0;
    E(i,3)=0;
    E(i,4)=0;
    E(i,5)=0;
    E(i,6)=0;
    E(i,7)=0;
    E(i,8)=0;
    E(i,9)=0;
    E(i,10)=0;
    
    E(i,11:82)=reshape(E_VML,1,72);
    
    
    
    
end



E=reshape(E,size(data{1},1)*82,1);






end





