import cv2
import numpy as np
from matplotlib import pyplot as plt

# Crop an image
img = cv2.imread('img/bicycle.png', 0)  # 0 for grayscale
cv2.imshow('bicycle', img)
cv2.waitKey(0)

# Check Image Size
print(img.shape)  # when cropping limits should be within this range

cropped = img[109:310, 9:160]  # using different range as compared to octave here end rows and columns are not included
cv2.imshow('cropped', cropped)
cv2.waitKey(0)
print(cropped.shape)
