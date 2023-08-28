import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\91982\Desktop\CV\samurai.jpg')
cv2.imshow('Samurai', img)
cv2.waitKey(0)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow('Blank', blank)
cv2.waitKey(0)

b,g,r = cv2.split(img)

cv2.imshow('Blue',b)
cv2.imshow('Green',g)
cv2.imshow('Red',r)
cv2.waitKey(0)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv2.merge([b,g,r])
cv2.imshow('Merged image', merged)
cv2.waitKey(0)

blue = cv2.merge([b,blank,blank])
green = cv2.merge([blank,g,blank])
red = cv2.merge([blank,blank,r])

cv2.imshow('Blue2',blue)
cv2.imshow('Green2',green)
cv2.imshow('Red2',red)
cv2.waitKey(0)