import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('crop0.jpg')

#blur = cv2.blur(img,(5,5))
#blur1 = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
blur2 = cv2.bilateralFilter(img,9,75,75)
plt.subplot(120),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(121),plt.imshow(median),plt.title('Blurredm')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur2),plt.title('Blurredb')
plt.xticks([]), plt.yticks([])
plt.show()
