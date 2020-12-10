import numpy as np
import cv2

def doItAgain(sizeOfKernel, howManyTimes, omgIMG):
    for x in range(howManyTimes):
        omgIMG = cv2.medianBlur(omgIMG, sizeOfKernel)
    return omgIMG

img = cv2.imread("/home/szymek/Desktop/PythonFiltering/BlurMedian/photos/NAObrud.jpg")

cv2.namedWindow('Unfiltered Image', cv2.WINDOW_NORMAL)
cv2.imshow('Unfiltered Image',img)
cv2.waitKey(0)
print "Processing..."

# median filter - takes median from group of pixels
# mostly depends on kernel size
# median for sorted vector [1 1 2 2 2 3 4 5 5] is 2

# OpenCV median = cv2.medianBlur(src, ksize[, dst])

FirstTurn = doItAgain(3, 1, img)
cv2.namedWindow('First Turn - kernel size 3x3', cv2.WINDOW_NORMAL)
cv2.imshow('First Turn - kernel size 3x3', FirstTurn)
print "Done!"
cv2.waitKey(0)
