clc
clear
stacksize('max')

// SEGMENTATION METHODS

// Read new image

I = double(ReadImage("C:\Users\Szymek\Desktop\tutorial\Tonga700.jpg"));

// Split image to different channels

IR = I(:,:,1);
IG = I(:,:,2);
IB = I(:,:,3);

// Find channel from which you will threshold a water
// May be done: visually or by histograms of part of an image where buildings are grouped

figure(1)
ShowImage(uint8(IR), "Red Channel")
figure(2)
ShowImage(uint8(IG), "Green Channel")
figure(3)
ShowImage(uint8(IB), "Blue Channel")

areaRow = [430:1:430+120];
areaCol = [40:1:40+120];
hR = CreateHistogram(uint8(IR(areaRow, areaCol)));
hRbig = CreateHistogram(uint8(IR));
hG = CreateHistogram(uint8(IG(areaRow, areaCol)));
hGbig = CreateHistogram(uint8(IG));
hB = CreateHistogram(uint8(IB(areaRow, areaCol)));
hBbig = CreateHistogram(uint8(IB));

figure(4)
aI = I;
aI(areaRow, areaCol,:) = round(aI(areaRow, areaCol,:)*0.8);
aI = uint8(aI);

ShowColorImage(aI, "ROI")

figure(5)
subplot(611)
plot(hR)
subplot(612)
plot(hRbig)
subplot(613)
plot(hG)
subplot(614)
plot(hGbig)
subplot(615)
plot(hB)
subplot(616)
plot(hBbig)

// Threshold red channel by using dsearch algorithm

threshVector = [30:255];
s = size(IR);
IT = zeros(s(1), s(2));

for i = 1:1:s(1)
    
    ir_vector = IR(i,:);
    [i_bin, counts, outside] = dsearch(ir_vector, threshVector);
    maxIbin = max(i_bin);
    
    if maxIbin == 0 then
        IT(i,:) = i_bin;
    else
        IT(i,:) = ceil(i_bin/maxIbin);
    end
    
end


// Dilate threshed area image

StructureElement = CreateStructureElement('square', 3);
dilatedBinary = DilateImage(IT, StructureElement);
clear IT

figure(6)
ShowImage(dilatedBinary, "Threshed Image");

// Cut islands
dilatedBinary = uint8(dilatedBinary);

IRreg = dilatedBinary .* IR;
IGreg = dilatedBinary .* IG;
IBreg = dilatedBinary .* IB;

clear dilatedBinary

Ireg(:,:,1) = IRreg;
Ireg(:,:,2) = IGreg;
Ireg(:,:,3) = IBreg;

clear IRreg
clear IGreg
clear IBreg

figure(7)
ShowColorImage(Ireg, "Cutted ocean")
