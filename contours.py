import cv2
import numpy as np

img = cv2.imread(r"C:\Users\91982\Desktop\CV\samurai.jpg")
cv2.imshow('Samurai', img)
cv2.waitKey(0)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow('Blank', blank)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

cv2.waitKey(0)

# blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
# cv2.imshow('Blur_on_gray', blur)

# cv2.waitKey(0)

# canny = cv2.Canny(blur, 125,175)
# cv2.imshow('Canny Edges_on_blur_on_gray', canny)

# cv2.waitKey(0)

ret,thresh = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
cv2.imshow('Thresh', thresh)
cv2.waitKey(0)

contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

cv2.drawContours(blank, contours, -1, (0,0,255), 2)
cv2.imshow('Contours Drawn', blank)
cv2.waitKey(0)

