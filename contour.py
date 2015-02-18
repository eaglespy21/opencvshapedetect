import numpy as np 
import cv2 
im = cv2.imread('worko.jpg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy =cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
cv2.drawContours(im, [cnt], 0, (0,255,0), 3)
cv2.imshow("hello", im)
#cv2.imshow("contours",contours)
cv2.imshow("cnt[0]",cnt[1])
cv2.imwrite('workoc.jpg', im)
cv2.waitKey(0)
