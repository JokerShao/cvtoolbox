function Show_TransMat2(A,invK,R,T,kc)


hold on
 
plot3([T(1),T(1)+R(1,1)],[T(2),T(2)+R(2,1)],[T(3),T(3)+R(3,1)],'r-','LineWidth',3);
hold on
plot3([T(1),T(1)+R(1,2)*0.5],[T(2),T(2)+R(2,2)*0.5],[T(3),T(3)+R(3,2)*0.5],'g-','LineWidth',3);
hold on
plot3([T(1),T(1)+R(1,3)*2],[T(2),T(2)+R(2,3)*2],[T(3),T(3)+R(3,3)*2],'b-','LineWidth',3);
hold on
plot3([0,1],[0,0],[0,0],'r-','LineWidth',3);
hold on
plot3([0,0],[0,1],[0,0],'g-','LineWidth',3);
    


for i=1:size(A,1)
    
    
    
    hold on

    
    P=A(i,4:5);
    U=invK*[P,1]';
    
    U2 =[ comp_distortion_oulu(U(1:2),kc);1];
    
%     r=norm(U(1:2));
%     U2=[U(1:2)*(1+k1*r+k2*r^2+k3*r^3+k4*r^4+k5*r^5);1];
    V=R*U2;
    
    V=V*T(3)*abs(1/V(3));
    
    
    
    plot3(A(i,1),A(i,2),A(i,3),'r*',...
           [T(1),T(1)+V(1)],[T(2),T(2)+V(2)],[T(3),T(3)+V(3)],'c-');
    
    
   
    
    
end

axis equal

view(59, 67);

end