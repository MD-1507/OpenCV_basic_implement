import cv2
import numpy as np
import matplotlib.pyplot as plt

img  = cv2.imread(r"C:\Users\91982\Desktop\CV\samurai.jpg")
cv2.imshow('Samurai', img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)

# Laplacian

lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('Laplacian',lap)
cv2.waitKey(0)

# Sobel

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1,0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0,1)

cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)

cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)

combined_sobel = cv2.bitwise_or(sobelx,sobely)
cv2.imshow('Combined Sobel', combined_sobel)
cv2.waitKey(0)

canny = cv2.Canny(gray, 150, 175)
cv2.imshow('Canny Edges', canny)
cv2.waitKey(0)