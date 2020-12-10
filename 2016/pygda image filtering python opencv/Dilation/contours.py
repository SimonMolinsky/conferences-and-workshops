#-*- coding: utf-8 -*-

import numpy as np
import cv2

 # cv2.threshold(src, thresh, maxval, type[, dst])

Image = cv2.imread("/home/szymek/Desktop/PythonFiltering/Dilation/HeLa-I.jpg")
cv2.namedWindow("Main", cv2.WINDOW_NORMAL)
cv2.imshow("Main", Image)
cv2.waitKey(0)

# Extraction of Blue channel
b = Image[:,:,0]
cv2.namedWindow("Only Blue Channel", cv2.WINDOW_NORMAL)
cv2.imshow("Only Blue Channel", b)
cv2.waitKey(0)
# Callback Function for Trackbar (but do not any work)
def nothing(*arg):
    pass

 # Generate trackbar Window Name
TrackbarName = "Trackbar"

 # Make Window and Trackbar
cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.createTrackbar(TrackbarName, "window", 0, 250, nothing)

img_threshed = np.zeros(b.shape, np.uint8)

while True:
  # Get kernel size in trackbar
  TrackbarPos = cv2.getTrackbarPos(TrackbarName, "window")
  # Apply dilation
  limit = TrackbarPos
  ret,img_threshed = cv2.threshold(b,limit,255,cv2.THRESH_BINARY)
  # Show in window
  cv2.imshow("window", img_threshed)
  ch = cv2.waitKey(27)
  if ch == 27 or ch == 0x10001b:
     break

# Expanding borders of the objects
kernel = np.ones((9, 9),np.uint8)
img_dilated = cv2.dilate(img_threshed, kernel)
img_dilated = cv2.dilate(img_dilated, kernel)
kernel = np.ones((11, 11),np.uint8)
img_dilated = cv2.erode(img_dilated, kernel)
cv2.namedWindow("Dilatedx2 and Eroded Blue Channel", cv2.WINDOW_NORMAL)
cv2.imshow("Dilatedx2 and Eroded Blue Channel", img_dilated)
cv2.waitKey(0)

# Retrieving contours by subtraction base objects from the expanded objects
img_contours = img_dilated - img_threshed
cv2.namedWindow("Contours", cv2.WINDOW_NORMAL)
cv2.imshow("Contours", img_contours)
cv2.waitKey(0)



cv2.destroyAllWindows()

# About photo (PL):
# HeLa - linia komórkowa wywodząca się z komórek raka szyjki macicy, pobranych od 31-letniej Henrietty Lacks.
# Linia komórkowa HeLa służy do badań biologii komórek nowotworowych. Komórki różnią się znacznie od prawidłowych komórek nabłonkowych szyjki macicy. Uległy one transformacji nowotworowej na skutek zakażenia wirusem brodawczaka (ang. papiloma) HPV 18. Linia charakteryzuje się wybitnie szybkim wzrostem, przewyższającym inne linie komórek nowotworowych. Obecnie całkowita masa komórek HeLa znacznie przekracza wagę chorej, od której pobrano próbkę[1].
# Według niektórych naukowców komórki HeLa stanowią zupełnie nowy, odrębny gatunek organizmów jednokomórkowych, powstały przez zróżnicowanie się kobiecych komórek nabłonka szyjki macicy pod wpływem wirusa brodawczaka. W 1991 roku gatunek ten nazwano Helacyton gartleri[2].
# Odnośnik (ENG): https://en.wikipedia.org/wiki/HeLa
