import cv2
import numpy as np
from matplotlib import pyplot as plt

# Color image
img = cv2.imread('img/fruit.png')
cv2.imshow('fruit', img)
cv2.waitKey(0)

# size of the image
print(img.shape)