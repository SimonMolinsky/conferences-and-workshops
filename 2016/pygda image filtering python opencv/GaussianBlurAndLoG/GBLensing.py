import numpy as np
import cv2

def doItAgain(sizeOfKernel, howManyTimes, omgIMG, sigmax):
    for x in range(howManyTimes):
        omgIMG = cv2.GaussianBlur(omgIMG, sizeOfKernel, sigmax)
    return omgIMG

#Photo (my)
img = cv2.imread("/home/szymek/Desktop/PythonFiltering/GaussianBlurAndLoG/junior.jpg")

cv2.namedWindow('Unfiltered Image', cv2.WINDOW_NORMAL)
cv2.imshow('Unfiltered Image',img)
cv2.waitKey(0)
print "Processing..."


#Python: cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])
#    Parameters:
#        src: input image; the image can have any number of channels, which are processed independently, but the depth should be CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
#        dst: output image of the same size and type as src.
#        ksize: Gaussian kernel size. ksize.width and ksize.height can differ but they both must be positive and odd. Or, they can be zeros and then they are computed from sigma.
#        sigmaX: Gaussian kernel standard deviation in X direction.
#        sigmaY: Gaussian kernel standard deviation in Y direction; if sigmaY is zero, it is set to be equal to sigmaX, if both sigmas are zeros, they are computed from ksize.width and ksize.height , respectively (see getGaussianKernel() for details); to fully control the result regardless of possible future modifications of all this semantics, it is recommended to specify all of ksize, sigmaX, and sigmaY.
#        borderType: pixel extrapolation method (see borderInterpolate for details).

TR = doItAgain((29,29), 1, img, 0)
hat = img[364:484, 422:542]
TR[364:484, 422:542] = hat

cv2.namedWindow('Filtered one time, kernel size 29', cv2.WINDOW_NORMAL)
cv2.imshow('Filtered one time, kernel size 29', TR)
print "Done!"
cv2.waitKey(0)
