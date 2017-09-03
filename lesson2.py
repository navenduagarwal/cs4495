import cv2
import numpy as np
from matplotlib import pyplot as plt

# Gaussian Dist

# load image 1
saturn = cv2.imread('img/saturn.png', 0)
cv2.imshow('saturn', saturn)
cv2.waitKey(0)

im = np.empty(saturn.shape, np.uint8)  # creating empty image
im2 = cv2.randn(im, 0, 100) # sigma of 100
cv2.imshow('noise', im2)
cv2.imshow(' image with noise', saturn + im2)

average_color = np.uint8(np.average(saturn))  # average color
print(average_color)
cv2.waitKey(0)

cv2.destroyAllWindows()  # close all openCV windows
