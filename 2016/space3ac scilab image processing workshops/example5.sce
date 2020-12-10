clc
clear
stacksize('max')

// SEGMENTATION METHODS 2

// Read old image (preprocessed in the exercise 3)

I = double(ReadImage("C:\Users\Szymek\Desktop\tutorial\B.jpg"));
I = RGB2Gray(I);

figure(1)
ShowImage(I, "Base Image")


// Edge detection and gradient image

global EDGE_SOBEL;
gradientImage = EdgeFilter(I, EDGE_SOBEL);

figure(2)
ShowImage(gradientImage, "Gradient Image");

edges = ~SegmentByThreshold(gradientImage, 40)

figure(3)
ShowImage(edges, "Edges Image");

// Distance transform

distance = DistanceTransform(edges);

figure(4)
distance = double(distance);
ShowImage(distance, "Distance Image", jetcolormap(32));


// Blob detection

thresholdImg = SegmentByThreshold(distance, 2);

marker = SearchBlobs(thresholdImg);

figure(5)
ShowImage(marker, 'Result of Blob Detection');

water = Watershed(uint8(gradientImage), marker);

figure(6);

ColorMapLength = length(unique(water));

ShowImage(double(water), ...
          'Result of Watershed Transform', ...
          jetcolormap(ColorMapLength));
