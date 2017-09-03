import cv2
import numpy as np
from matplotlib import pyplot as plt

# adding filters

# load image 1
saturn = cv2.imread('img/saturn.png', 0)
cv2.imshow('saturn', saturn)
cv2.waitKey(0)

# add some noise
im = np.empty(saturn.shape, np.uint8)  # creating empty image
noise_sigma = 25
im2 = cv2.randn(im, 0, noise_sigma)  # sigma of 100
cv2.imshow('noise', im2)
cv2.waitKey(0)
noisy_image = saturn + im2
cv2.imshow(' image with noise', noisy_image)
cv2.waitKey(0)

# Averaging
avging = cv2.blur(noisy_image, (11, 11))  # You can change the kernel size as you want
cv2.imshow('Averaging', avging)
cv2.waitKey(0)

# gaussian filter
filter_size = 11
filter_sigma = 2
im = cv2.GaussianBlur(noisy_image, (filter_size, filter_size), filter_sigma)
cv2.imshow('gaussian blurring', im)
cv2.waitKey(0)

cv2.destroyAllWindows()  # close all openCV windows
