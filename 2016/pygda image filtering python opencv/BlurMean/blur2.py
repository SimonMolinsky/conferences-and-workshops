import numpy as np
import cv2

# Select Noise Region!!! <----------------------

def doItAgain(sizeOfKernel, howManyTimes, omgIMG):
    for x in range(howManyTimes):
        omgIMG = cv2.blur(omgIMG, sizeOfKernel)
    return omgIMG

#Photo (my)
img = cv2.imread("/home/szymek/Desktop/PythonFiltering/BlurMean/NAObrud.jpg")

cv2.namedWindow('Unfiltered Image', cv2.WINDOW_NORMAL)
cv2.imshow('Unfiltered Image',img)
cv2.waitKey(0)
print "Processing..."

# blurring == mean of the pixel and his neighbourhood
# Simple blur kernel (3x3):
# A = [1 1 1
#  1 1 1
#  1 1 1]
# B = 1 / (kernelSize.height * kernelSize.width)
# KERNEL = B * A

# OpenCV blur: cv2.blur(src, ksize[, dst[, anchor[, borderType]]])
# Filtering only part of the image

x1 = 300
y1 = 40
dp = 50
noise = img[y1:y1+dp, x1:x1+dp] # wiersze, kolumny

cv2.namedWindow('Noise region', cv2.WINDOW_NORMAL)
cv2.imshow('Noise region', noise)
cv2.waitKey(0)
print "Processing..."

noiseReduction = doItAgain((3,3),2,noise)

cv2.namedWindow('Reduced noise region', cv2.WINDOW_NORMAL)
cv2.imshow('Reduced noise region', noiseReduction)
cv2.waitKey(0)
print "Processing..."

img[y1:y1+dp, x1:x1+dp] = noiseReduction
cv2.namedWindow('How this looks on the image', cv2.WINDOW_NORMAL)
cv2.imshow('How this looks on the image', img)
cv2.waitKey(0)
print "Done!"
