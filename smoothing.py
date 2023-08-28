import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\91982\Desktop\CV\samurai.jpg')
cv2.imshow('Samurai', img)
cv2.waitKey(0)

#Averaging 
avg = cv2.blur(img, (3,3))
cv2.imshow('Average Blur',avg)
cv2.waitKey(0)

#Gaussian Blur
gauss = cv2.GaussianBlur(img,(7,7),cv2.BORDER_DEFAULT)
cv2.imshow('Gaussian Blur', gauss)
cv2.waitKey(0)

#Median Blur
median = cv2.medianBlur(img,3)
cv2.imshow('Median Blur', median)
cv2.waitKey(0)

#Bilateral Filter
bilateral=cv2.bilateralFilter(img,5,15,15)
cv2.imshow('Bilateral Filter', bilateral)
cv2.waitKey(0)

