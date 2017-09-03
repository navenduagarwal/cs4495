import cv2
import numpy as np
from matplotlib import pyplot as plt

# Image Difference

# load image 1
dolphin = cv2.imread('img/dolphin.png', 0)
cv2.imshow('dolphin', dolphin)
cv2.waitKey(0)

im = np.empty(dolphin.shape, np.uint8)  # creating empty image
cv2.randn(im, 0, 50) # converted to gaussian noise
cv2.imshow('noise', im)
cv2.imshow(' image witj noise', dolphin + im)
cv2.waitKey(0)

cv2.destroyAllWindows()  # close all openCV windows
