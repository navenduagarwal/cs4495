import cv2
import numpy as np
from matplotlib import pyplot as plt

# Color image
img = cv2.imread('img/fruit.png')
cv2.imshow('fruit', img)
cv2.waitKey(0)

# size of the image
print(img.shape)

# all the rows and columns but only 1 plane
img_red = img[:, :, 1]
cv2.imshow('red', img_red)
cv2.waitKey(0)

# size of color channel
print(img_red.shape)
px = img_red[150, :]
print(px)
plt.plot(px)
plt.show()
