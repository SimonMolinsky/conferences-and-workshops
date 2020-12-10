import numpy as np
import cv2

#Photo from Michigan Tech University
img = cv2.imread("/home/szymek/Desktop/PythonFiltering/BilateralFilteringImages/aurora.jpg")

cv2.namedWindow('Unfiltered Image', cv2.WINDOW_NORMAL)
cv2.imshow('Unfiltered Image',img)
cv2.waitKey(0)
print "Processing..."

# Bilateral Filtering - removing noise - cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]])
# http://people.csail.mit.edu/sparis/bf_course/slides/03_definition_bf.pdf

height, width, channels = img.shape  #size needed for sigmaSpace = 2% of img diagonal
diag = np.sqrt(width**2 + height**2)
sigmaSpace = 0.02 * diag
sigmaColor = 40

bilateralAurora = cv2.bilateralFilter(img, -1, sigmaColor, sigmaSpace)
cv2.namedWindow('Filtered Image', cv2.WINDOW_NORMAL)
cv2.imshow('Filtered Image', bilateralAurora)
cv2.waitKey(0)
print "Processing..."

dst = cv2.add(bilateralAurora, img)
cv2.namedWindow('Added images', cv2.WINDOW_NORMAL)
cv2.imshow('Added images',dst)
cv2.waitKey(0)
print "Processing..."

dst2 = cv2.addWeighted(bilateralAurora,0.7,img,0.3,0)
cv2.namedWindow('Added images - 0.7 / 0.3', cv2.WINDOW_NORMAL)
cv2.imshow('Added images - 0.7 / 0.3',dst2)
cv2.waitKey(0)
print "Processing..."

dst3 = cv2.addWeighted(bilateralAurora,0.3,img,0.7,0)
cv2.namedWindow('Added images - 0.3 / 0.7', cv2.WINDOW_NORMAL)
cv2.imshow('Added images - 0.3 / 0.7',dst3)
cv2.waitKey(0)
print "Done!"
