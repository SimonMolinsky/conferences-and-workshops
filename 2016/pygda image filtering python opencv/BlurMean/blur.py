import numpy as np
import cv2

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

doingItWrong_FirstRelease = doItAgain((3,3), 1, img)

cv2.namedWindow('You are doing it wrong', cv2.WINDOW_NORMAL)
cv2.imshow('You are doing it wrong', doingItWrong_FirstRelease)
cv2.waitKey(0)
print "Processing..."

doingItWrong_SecondRelease = doItAgain((9,9), 1, img)

cv2.namedWindow('You are doing it wrong... Again...', cv2.WINDOW_NORMAL)
cv2.imshow('You are doing it wrong... Again...', doingItWrong_SecondRelease)
cv2.waitKey(0)
print "Processing..."

doingItWrong_LastRelease = doItAgain((3,3), 3, img)

cv2.namedWindow('You are doing it wrong... Again and again', cv2.WINDOW_NORMAL)
cv2.imshow('You are doing it wrong... Again and again', doingItWrong_LastRelease)
cv2.waitKey(0)
print "Processing..."

# Filtering only part of the image

x1 = 120
y1 = 70
dp = 50
noise = img[y1:y1+dp, x1:x1+dp]

cv2.namedWindow('Noise region', cv2.WINDOW_NORMAL)
cv2.imshow('Noise region', noise)
cv2.waitKey(0)
print "Processing..."

windowMean = doItAgain((5,5), 9, noise)

cv2.namedWindow('Noise region?', cv2.WINDOW_NORMAL)
cv2.imshow('Noise region?', windowMean)
cv2.waitKey(0)
print "Processing..."

img[y1:y1+dp, x1:x1+dp] = windowMean
cv2.namedWindow('Is there any noise on this image?', cv2.WINDOW_NORMAL)
cv2.imshow('Is there any noise on this image?', img)
cv2.waitKey(0)
print "Done!"
