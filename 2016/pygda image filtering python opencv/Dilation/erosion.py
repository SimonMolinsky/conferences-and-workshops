#-*- coding: utf-8 -*-

import numpy as np
import cv2


# Python: cv2.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])

Image = cv2.imread("/home/szymek/Desktop/PythonFiltering/Dilation/HeLa-I.jpg")

# Callback Function for Trackbar (but do not any work)
def nothing(*arg):
    pass

 # Generate trackbar Window Name
TrackbarName = "Trackbar"

 # Make Window and Trackbar
cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.createTrackbar(TrackbarName, "window", 0, 50, nothing)

 # Allocate destination image
img_eroded = np.zeros(Image.shape, np.uint8)

while True:
  # Get kernel size in trackbar
  TrackbarPos = cv2.getTrackbarPos(TrackbarName, "window")
  # Apply erosion
  kernel = np.ones((2*TrackbarPos+1, 2*TrackbarPos+1),np.uint8)
  img_eroded = cv2.erode(Image, kernel)
  # Show in window
  cv2.imshow("window", img_eroded)
  ch = cv2.waitKey(27)
  if ch == 27 or ch == 0x10001b:
     break

cv2.destroyAllWindows()

# About photo (PL):
# HeLa - linia komórkowa wywodząca się z komórek raka szyjki macicy, pobranych od 31-letniej Henrietty Lacks.
# Linia komórkowa HeLa służy do badań biologii komórek nowotworowych. Komórki różnią się znacznie od prawidłowych komórek nabłonkowych szyjki macicy. Uległy one transformacji nowotworowej na skutek zakażenia wirusem brodawczaka (ang. papiloma) HPV 18. Linia charakteryzuje się wybitnie szybkim wzrostem, przewyższającym inne linie komórek nowotworowych. Obecnie całkowita masa komórek HeLa znacznie przekracza wagę chorej, od której pobrano próbkę[1].
# Według niektórych naukowców komórki HeLa stanowią zupełnie nowy, odrębny gatunek organizmów jednokomórkowych, powstały przez zróżnicowanie się kobiecych komórek nabłonka szyjki macicy pod wpływem wirusa brodawczaka. W 1991 roku gatunek ten nazwano Helacyton gartleri[2].
# Odnośnik (ENG): https://en.wikipedia.org/wiki/HeLa
