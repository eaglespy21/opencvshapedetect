import numpy as np
import cv2 
img = cv2.imread('workoc.jpg',2)
ret, thresh=cv2.threshold(img, 127, 255,0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv2.moments(cnt)
area = cv2.contourArea(cnt)
print M
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
cv2.imshow('img', img)
cv2.imshow('approx', approx)
