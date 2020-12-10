clc
clear

m = round(rand(128,128)*255);

figure(1)
ShowImage(m, "Image");

M = zeros(128,128,3);
M(:,:,1) = m;

figure(2)
ShowColorImage(M, "Color Image");

v = 0:1:255;
sv = length(v);
W = zeros(150, sv ,3);

for i = 1:1:150
    if i < 51 then
        
        W(i,:,1) = v;
        
    elseif i < 101 then
        
        W(i,:,2) = v;
        
    else
        
        W(i,:,3) = v;
    
    end
end

figure(3)
ShowColorImage(W, "Color Scales - reversed");

W = uint8(W);
figure(4)
ShowColorImage(W, "Color Scales - proper");

W = (double(W))/255;
figure(5)
ShowColorImage(W, "Color Scales - proper");




//example_row = [1 2 3 4 5 1 2 3 9];
//L = length(example_row);
//for i = 1:1:L
//if example_row(i) == 1 then
//disp("first")
//elseif example_row(i) == 2 then
//disp("second")
//else
//disp("else")
//end
//end
