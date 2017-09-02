import cv2
import numpy as np
from matplotlib import pyplot as plt

# Adding two images

# load image 1
dolphin = cv2.imread('img/dolphin.png', 0)
cv2.imshow('dolphin', dolphin)
cv2.waitKey(0)

# load image 2
bicycle = cv2.imread('img/bicycle.png', 0)
cv2.imshow('bicyle', bicycle)
cv2.waitKey(0)

# check image size is equal
print('{} image size: {}'.format('Dolphin', dolphin.shape))
print('{} image size: {}'.format('Bicycle', bicycle.shape))

summed = dolphin + bicycle
average = dolphin / 2 + bicycle / 2  # Dividing values by 2 to make maximum intensity values same as source values.
average_alt = (dolphin + bicycle) / 2
cv_summed = cv2.add(dolphin, bicycle)
cv_average = cv2.addWeighted(dolphin, 0.5, bicycle, 0.5, 0)

cv2.imshow('summed', summed)
cv2.waitKey(0)

cv2.imshow('average', average)
cv2.waitKey(0)

cv2.imshow('average_alt', average_alt)
cv2.waitKey(0)

cv2.imshow('cv add', cv_summed)
cv2.waitKey(0)

cv2.imshow('cv add weighed', cv_average)
cv2.waitKey(0)

cv2.destroyAllWindows()  # close all openCV windows
