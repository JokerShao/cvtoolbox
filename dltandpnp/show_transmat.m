function show_transmat(A,invK,Rwc,twc,kc)


hold on

camX = [1 0 0]'
camY = [0 1 0]'
camZ = [0 0 1]'

camX_inworld = (Rwc * camX)*0.5 + twc;
camY_inworld = (Rwc * camY)*0.5 + twc;
camZ_inworld = (Rwc * camZ)*3 + twc;




 
plot3([twc(1), camX_inworld(1)], [twc(2), camX_inworld(2)], [twc(3), camX_inworld(3)],'r-','LineWidth',3);
hold on
plot3([twc(1), camY_inworld(1)], [twc(2), camY_inworld(2)], [twc(3), camY_inworld(3)],'g-','LineWidth',3);
hold on
plot3([twc(1), camZ_inworld(1)], [twc(2), camZ_inworld(2)], [twc(3), camZ_inworld(3)],'b-','LineWidth',3);
hold on

plot3([0,1],[0,0],[0,0],'r-','LineWidth',3);
hold on
plot3([0,0],[0,1],[0,0],'g-','LineWidth',3);

axis equal



for i=1:size(A,1)
    
    
    
    hold on

    
    P=A(i,3:4);
    
    
    U=invK*[P,1]';
    
    U2 =[ comp_distortion_oulu(U(1:2),kc);1];
    
%     r=norm(U(1:2));
%     U2=[U(1:2)*(1+k1*r+k2*r^2+k3*r^3+k4*r^4+k5*r^5);1];
    V=Rwc*U2;
    
    V=V/abs(V(3))*twc(3);
    
    
    
    plot3(A(i,1),A(i,2),0,'r*',...
           [twc(1),twc(1)+V(1)],[twc(2),twc(2)+V(2)],[twc(3),twc(3)+V(3)],'c-');
    
    
   
    
    
end

axis equal

view(59, 67);

end