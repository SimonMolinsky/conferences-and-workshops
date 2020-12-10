import numpy as np
import cv2
img = cv2.imread("/home/szymek/Desktop/PythonFiltering/BilateralFilteringImages/surykatka.jpg")
cv2.namedWindow('Unfiltered Image', cv2.WINDOW_NORMAL)
cv2.imshow('Unfiltered Image',img)
cv2.waitKey(0)

# Bilateral Filtering - removing noise - cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]])
# http://people.csail.mit.edu/sparis/bf_course/slides/03_definition_bf.pdf

height, width, channels = img.shape  #size needed for sigmaSpace = 2% of img diagonal
diag = np.sqrt(width**2 + height**2)
sigmaSpace = 30
sigmaColor = 30

bSurykatka = cv2.bilateralFilter(img, 5, 210, 30)
bSurykatka = cv2.bilateralFilter(bSurykatka, 5, 210, 30)
bSurykatka = cv2.bilateralFilter(bSurykatka, -1, sigmaColor, sigmaSpace)
bSurykatka = cv2.bilateralFilter(bSurykatka, -1, sigmaColor, sigmaSpace)
cv2.namedWindow('Cartooned Image', cv2.WINDOW_NORMAL)
cv2.imshow('Cartooned Image', bSurykatka)
cv2.waitKey(0)
