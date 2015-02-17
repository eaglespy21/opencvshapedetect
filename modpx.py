import cv2
import numpy as np

img = cv2.imread('dips.jpg')
px = img[100,100]
print px

blue = img[255,255,255]
print blue

print img.shape
