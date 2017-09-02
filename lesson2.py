import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load and display an image
img = cv2.imread('img/dolphin.png', 0)  # 0 for grayscale
# cv2.imshow('dolphin', img)
# cv2.waitKey(0)
#
# # Image Size
# print(img.shape)
#
# # Class of Image
# print(img.dtype)

# value at given location
print(img[50, 100])

# value for entire row
print(img[50, :])
plt.plot(img[50, :])
plt.show()
