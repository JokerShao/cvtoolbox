function show_stereo_cam(Pts, Rw1, tw1, Rw2, tw2)


    for i=1:size(Pts,1)
        plot3(Pts(i,1), Pts(i,2), Pts(i,3), 'r*');
        hold on;
    end
    
hold on;
plot3([tw1(1),tw1(1)+Rw1(1,1)*0.5],[tw1(2),tw1(2)+Rw1(2,1)*0.5],[tw1(3),tw1(3)+Rw1(3,1)*0.5],'r-','LineWidth',3);
hold on
plot3([tw1(1),tw1(1)+Rw1(1,2)*0.5],[tw1(2),tw1(2)+Rw1(2,2)*0.5],[tw1(3),tw1(3)+Rw1(3,2)*0.5],'g-','LineWidth',3);
hold on
plot3([tw1(1),tw1(1)+Rw1(1,3)*2],[tw1(2),tw1(2)+Rw1(2,3)*2],[tw1(3),tw1(3)+Rw1(3,3)*2],'b-','LineWidth',3);


hold on;
plot3([tw2(1),tw2(1)+Rw2(1,1)*0.5],[tw2(2),tw2(2)+Rw2(2,1)*0.5],[tw2(3),tw2(3)+Rw2(3,1)*0.5],'r-','LineWidth',3);
hold on
plot3([tw2(1),tw2(1)+Rw2(1,2)*0.5],[tw2(2),tw2(2)+Rw2(2,2)*0.5],[tw2(3),tw2(3)+Rw2(3,2)*0.5],'g-','LineWidth',3);
hold on
plot3([tw2(1),tw2(1)+Rw2(1,3)*2],[tw2(2),tw2(2)+Rw2(2,3)*2],[tw2(3),tw2(3)+Rw2(3,3)*2],'b-','LineWidth',3);




% 
% hold on
% plot3([0,1],[0,0],[0,0],'r-','LineWidth',3);
% hold on
% plot3([0,0],[0,1],[0,0],'g-','LineWidth',3);

axis equal

end



