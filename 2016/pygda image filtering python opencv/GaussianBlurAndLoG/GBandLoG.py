import numpy as np
import cv2

def doItAgain(sizeOfKernel, howManyTimes, omgIMG, sigmax):
    for x in range(howManyTimes):
        omgIMG = cv2.GaussianBlur(omgIMG, sizeOfKernel, sigmax)
    return omgIMG

#Photo (my)
img = cv2.imread("/home/szymek/Desktop/PythonFiltering/GaussianBlurAndLoG/parrot.jpg")

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



FR = doItAgain((3,3), 1, img, 0)

cv2.namedWindow('Filtered one time, kernel size 3x3', cv2.WINDOW_NORMAL)
cv2.imshow('Filtered one time, kernel size 3x3', FR)
cv2.waitKey(0)
print "Processing..."

SR = doItAgain((9,9), 11, img, 0)

cv2.namedWindow('Filtered eleven times, kernel size 9x9', cv2.WINDOW_NORMAL)
cv2.imshow('Filtered eleven times, kernel size 9x9', SR)
cv2.waitKey(0)
print "Processing..."

TR = doItAgain((31,31), 1, img, 0)

cv2.namedWindow('Filtered one time, kernel size 29', cv2.WINDOW_NORMAL)
cv2.imshow('Filtered one time, kernel size 29', TR)
print "Done - Phase One!"
cv2.waitKey(0)
print "Phase two - Laplacian of Gaussian LoG"

# Python: cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]])
#
#    src: Source image.
#    dst: Destination image of the same size and the same number of channels as src .
#    ddepth: Desired depth of the destination image.
#    ksize: Aperture size used to compute the second-derivative filters. See getDerivKernels() for details. The size must be positive and odd.
#    scale: Optional scale factor for the computed Laplacian values. By default, no scaling is applied. See getDerivKernels() for details.
#    delta: Optional delta value that is added to the results prior to storing them in dst .
#    borderType: Pixel extrapolation method. See borderInterpolate for details.

gray_image = cv2.cvtColor(TR, cv2.COLOR_BGR2GRAY)
LoGimg = cv2.Laplacian(gray_image,cv2.CV_64F)

cv2.namedWindow('LoG Operator', cv2.WINDOW_NORMAL)
cv2.imshow('LoG Operator', LoGimg)
print "Done - Second Phase!"
cv2.waitKey(0)
print "Phase three - better LoG"

moreGaussian = doItAgain((29,29),9,TR,0)

cv2.namedWindow('Filtered ten times, kernel size 29', cv2.WINDOW_NORMAL)
cv2.imshow('Filtered ten times, kernel size 29', moreGaussian)
cv2.waitKey(0)
print "Processing..."

gray_image = cv2.cvtColor(moreGaussian, cv2.COLOR_BGR2GRAY)
LoGimg = cv2.Laplacian(gray_image,cv2.CV_64F)

cv2.namedWindow('LoG Operator - applied to more blurred image', cv2.WINDOW_NORMAL)
cv2.imshow('LoG Operator - applied to more blurred image', LoGimg)
print "Done - Third Phase! End of processing"
cv2.waitKey(0)
