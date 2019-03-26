t = [0:pi()/4:2*pi()]
x = 0.5*cos(t);
y = 0.5*sin(t);

coord = zeros(9,2);
coord(:,1) = x';
coord(:,2) = y';
coord
plot(x,y)
grid on
