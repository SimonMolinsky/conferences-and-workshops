clc
clear
stacksize('max')

// IMAGE POINT OPERATIONS AND FILTERING EXAMPLES

// Read base image

I = ReadImage("C:\Users\Szymek\Desktop\tutorial\OLI234.jpg");

// Make it brighter with logaritmic operations

c1=255/(log10(256));

Iz = double(I + 1); // avoiding zeros in the matrix

IR1=Iz(:,:,1);
s=size(IR1);

// Stacksize controlling - only rows are processed on-the-fly
for i=1:1:s(1)
    IR1(i,:)=c1*log10(IR1(i,:));
end

IG1=Iz(:,:,2);

// Stacksize controlling - only rows are processed on-the-fly
for i=1:1:s(1)
    IG1(i,:)=c1*log10(IG1(i,:));
end

IB1=Iz(:,:,3);

// Stacksize controlling - only rows are processed on-the-fly
for i=1:1:s(1)
    IB1(i,:)=c1*log10(IB1(i,:));
end
 
I1(:,:,1)=(floor(IR1));
I1(:,:,2)=(floor(IG1));
I1(:,:,3)=(floor(IB1));

figure(1)
ShowColorImage(uint8(I1), "Better");

// Write image
WriteImage(uint8(I1), "C:\Users\Szymek\Desktop\tutorial\B.jpg");

// RGB2Gray, noisy image

G = RGB2Gray(I1);
N = round(rand(s(1),s(2))*255);
GN = (G*0.92 + N*0.08);

figure(2)
ShowImage(GN, "Gray noisy")

// Average (mean) filtering with kernels 3,5,7

kernel3 = ones(3,3).*1/(3^2); // size 3x3, all elements divided by (1/3^2) -> sum of elements must give 1
kernel5 = ones(5,5).*1/(5^2);
kernel7 = ones(7,7).*1/(7^2);

FAv3 = conv2(G, kernel3, "same");
FAv5 = conv2(G, kernel5, "same");
FAv7 = conv2(G, kernel7, "same");

// Median filtering with kernels 3,5,7

FMe3 = MedianFilter(G, [3 3]);
FMe5 = MedianFilter(G, [5 5]);
FMe7 = MedianFilter(G, [7 7]);

// MSE, PSNR between a) base and noisy, b) base and averaged by each filter (7 values for MSE and 7 values for PSNR)

const_s = 1/(s(1) * s(2));
a = const_s * (G - GN).^2;
sum_a = sum(a);
clear GN;

fa1 = const_s * (G - FAv3).^2;
sum_fa1 = sum(fa1);
clear FAv3;

fa2 = const_s * (G - FAv5).^2;
sum_fa2 = sum(fa2);
clear FAv5;

fa3 = const_s * (G - FAv7).^2;
sum_fa3 = sum(fa3);
clear FAv7;

fm1 = const_s * (G - FMe3).^2;
sum_fm1 = sum(fm1);
clear FMe3;

fm2 = const_s * (G - FMe5).^2;
sum_fm2 = sum(fm2);
clear FMe5;

fm3 = const_s * (G - FMe7).^2;
sum_fm3 = sum(fm3);
clear FMe7;

MSE = [sum_a, sum_fa1, sum_fa2, sum_fa3, sum_fm1, sum_fm2, sum_fm3];
maxi_squared = 255^2;

PSNR = 10. * log10(maxi_squared./MSE);

