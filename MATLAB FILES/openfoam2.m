clc 
clear all 
close all 

t = [0:pi()/4:2*pi()];
x = 1*cos(t);
y = 1*sin(t);

coord = zeros(9,3);
coord(:,1) = x';
coord(:,2) = y';
coord;
plot(x,y)
grid on

for i = 1 : 8 
   fprintf('(%d %d %d)\n', coord(i,1),coord(i,2),coord(i,3)) 
end

