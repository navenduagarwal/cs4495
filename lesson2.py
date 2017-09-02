import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load and display an image
img = cv2.imread('img/dolphin.png',0)
cv2.imshow('dolphin',img)
cv2.waitKey(0)