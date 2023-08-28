import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\91982\Desktop\CV\samurai.jpg')
cv2.imshow('Samurai',img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)

# Simple Thresholding 

threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Image', thresh)
cv2.waitKey(0)

threshold2, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Threshold Image 2', thresh_inv)
cv2.waitKey(0)

# Adaptive Thresholding

adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
cv2.imshow('Adaptive Threshold', adaptive_thresh)
cv2.waitKey(0)

adaptive_thresh_inv = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 9)
cv2.imshow('Adaptive Threshold_INV', adaptive_thresh_inv)
cv2.waitKey(0)

