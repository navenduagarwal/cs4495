import cv2
import numpy as np
from matplotlib import pyplot as plt

# Image Difference

# load image 1
dolphin = cv2.imread('img/dolphin.png', 0)
cv2.imshow('dolphin', dolphin)
cv2.waitKey(0)

# load image 2
bicycle = cv2.imread('img/bicycle.png', 0)
cv2.imshow('bicycle', bicycle)
cv2.waitKey(0)

# difference
diff = dolphin - bicycle
cv2.imshow('diff', diff)
cv2.waitKey(0)

# difference with cv
diff_cv = cv2.subtract(dolphin, bicycle)
cv2.imshow('diff_cv', diff_cv)
cv2.waitKey(0)

cv2.destroyAllWindows()  # close all openCV windows
