clc // Clears console window
clear // clears variables from memory
stacksize('max') // Max stacksize for operations

I = ReadImage("C:\Users\Szymek\Desktop\tutorial\OLI234.jpg");

// Show image

figure(1)
ShowColorImage(I, "Original Image");

// Make image gray and show it in the new window
gray_I = RGB2Gray(I);
gray_I = double(gray_I);

figure(2)
ShowImage(gray_I, "Gray Image");

// Add some noise to the gray image
// a) create matrix of random values from 0 to 255 (of the same size as the base image, only integers)
// b) add random matrix to the base image and divide them by 2 (remeber about rounding values)
// c) create 3 histograms: one for the base image, one for the noise, one for the added noise and base image
// d) show image with added noise

size_image = size(gray_I);
noisy_matrix = (round(rand(size_image(1), size_image(2))*255));
noisy_image = round((0.98*(gray_I) + 0.02*(noisy_matrix)));

figure(3)
ShowImage(noisy_image,  "noisy image")

hist_base = CreateHistogram(uint8(gray_I)); // Important! Change the type of the image to the uint8 to get the proper values
hist_noise = CreateHistogram(uint8(noisy_matrix));
hist_output = CreateHistogram(uint8(noisy_image));

figure(4)
subplot(311)
plot(hist_base)
subplot(312)
plot(hist_noise)
subplot(313)
plot(hist_output)


// Create two more noisy images where noise about 5 and 10 percent of the image content 

noisy2 = round((0.95*(gray_I) + 0.05*(noisy_matrix)));
noisy3 = round((0.9*(gray_I) + 0.1*(noisy_matrix)));

// Calculate MSE and PSNR between original image and noisy images

const_size = 1/(size_image(1) * size_image(2));
a = const_size * (gray_I - noisy_image).^2;
sum_a = sum(a);
b = const_size * (gray_I - noisy2).^2;
sum_b = sum(b);
c = const_size * (gray_I - noisy3).^2;
sum_c = sum(c);

MSE = [sum_a, sum_b, sum_c];

maxi_squared = 255^2;

PSNR = 10. * log10(maxi_squared./MSE);
