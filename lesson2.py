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

# a slice of image
slice = img[100:103, 200:203]  # note in open cv we have to change a range a little bit to include boundaries
print(slice)
