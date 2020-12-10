#-*- coding: utf-8 -*-

import numpy as np
import cv2

# Callback Function for Trackbar (but do not any work)
def nothing(*arg):
    pass

#####   #####   #####
# Tick Photo
img = cv2.imread("/home/szymek/Desktop/PythonFiltering/SkryptBonusowy/Hyalomma_marginatum.jpg")

#Photo to Gray
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', gray_img)
cv2.waitKey(0)

# Detection of the edges
# Based on the Canny Detector
# cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])

cannyTrackbar1 = "Lower thresh limit"
cannyTrackbar2 = "Upper thresh limit"

cv2.namedWindow("Canny", cv2.WINDOW_NORMAL)
cv2.createTrackbar(cannyTrackbar1, "Canny", 0, 250, nothing)
cv2.createTrackbar(cannyTrackbar2, "Canny", 0, 250, nothing)

canny_img = np.zeros(gray_img.shape, np.uint8)

# Choosing of the proper edges

while True:
  # Get threshold limits in trackbar
  posLower = cv2.getTrackbarPos(cannyTrackbar1, "Canny")
  posUpper = cv2.getTrackbarPos(cannyTrackbar2, "Canny")
  # Apply dilation
  canny_img = cv2.Canny(gray_img, posLower, posUpper)
  # Show in window
  cv2.imshow("Canny", canny_img)
  ch = cv2.waitKey(27)
  if ch == 27 or ch == 0x10001b:
     break

cv2.destroyAllWindows()

# Preparation of 'comic' Image by bilateralFilter
# Bilateral Filtering - removing noise - cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]])
# http://people.csail.mit.edu/sparis/bf_course/slides/03_definition_bf.pdf

height, width, channels = img.shape  #size needed for sigmaSpace = 2% of img diagonal
diag = np.sqrt(width**2 + height**2)
sigmaSpace = 30
sigmaColor = 30

cartooned_img = cv2.bilateralFilter(img, 5, 210, 30)
cartooned_img = cv2.bilateralFilter(cartooned_img, 5, 210, 30)
cartooned_img = cv2.bilateralFilter(cartooned_img, -1, sigmaColor, sigmaSpace)
cartooned_img = cv2.bilateralFilter(cartooned_img, -1, sigmaColor, sigmaSpace)

cv2.namedWindow('Cartooned Image', cv2.WINDOW_NORMAL)
cv2.imshow('Cartooned Image', cartooned_img)
cv2.waitKey(0)

# Dilation and Adding edges to cartooned Image

inv_canny = 255 - canny_img

canny_3d = np.zeros(img.shape, np.uint8)
canny_3d[:,:,0] = inv_canny
canny_3d[:,:,1] = inv_canny
canny_3d[:,:,2] = inv_canny

trackbarErosion = "Erosion"

 # Make Window and Trackbar
cv2.namedWindow("Erosion Window", cv2.WINDOW_NORMAL)
cv2.createTrackbar(trackbarErosion, "Erosion Window", 0, 50, nothing)

 # Allocate destination image
img_eroded = np.zeros(img.shape, np.uint8)

while True:
  # Get kernel size in trackbar
  erodePos = cv2.getTrackbarPos(trackbarErosion, "Erosion Window")
  # Apply dilation
  kernel = np.ones((2*erodePos+1, 2*erodePos+1),np.uint8)
  img_eroded = cv2.erode(canny_3d, kernel)
  # Show in window
  cv2.imshow("Erosion Window", img_eroded)
  ch = cv2.waitKey(27)
  if ch == 27 or ch == 0x10001b:
     break

cv2.destroyAllWindows()

norm_inverse = img_eroded/255

# Multiplaction

result_img = cv2.multiply(norm_inverse, cartooned_img)
cv2.namedWindow('Result Image', cv2.WINDOW_NORMAL)
cv2.imshow('Result Image', result_img)
cv2.waitKey(0)
