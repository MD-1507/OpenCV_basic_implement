import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\91982\Desktop\CV\samurai.jpg")
cv2.imshow('Samurai',img)
cv2.waitKey(0)

# plt.imshow(img)
# plt.show()

# BGR to GrayScale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)

# BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)
cv2.waitKey(0)

# BGR to L*a*b
lab =  cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)
cv2.waitKey(0)

# BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)
cv2.waitKey(0)

# HSV to BGR
hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('HSV to BGR', hsv_bgr) 
cv2.waitKey(0)

# LAB to BGR
lab_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow('LAB to BGR', lab_bgr) 
cv2.waitKey(0)

plt.imshow(rgb)
plt.show()

