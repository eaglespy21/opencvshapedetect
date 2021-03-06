import cv2
import numpy as np

img = cv2.imread('crop0.jpg',3)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow('img',img)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
#dilation = cv2.dilate(img,kernel,iterations = 1)
#closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
#cv2.imshow('erode1', img)
cv2.imshow('erode', erosion)
#cv2.imwrite('worko.jpg', erosion)
#cv2.imshow('dilate', dilation)
#cv2.imshow('close', closing)
#cv2.imshow('gradient', gradient)
cv2.imwrite('erodedstar.jpg',erosion)
cv2.waitKey(0)
