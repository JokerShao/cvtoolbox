x=-8:0.5:8;                               % x范围                     
y=-8:0.5:8;                               % y范围
[xx,yy]=meshgrid(x,y);                      %构成格点矩阵
p=1;
z=sqrt((xx.^2)./(2*p)+(yy.^2))./(2*p);
surf(xx,yy,z);title('椭圆抛物面');                  %子图1，绘制三维图形