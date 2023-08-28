import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\91982\Desktop\CV\samurai.jpg')
cv2.imshow("Samurai", img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)

# Gray Histogram
gray_hist = cv2.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('Gray Histogram')
plt.plot(gray_hist)
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.xlim([0,250])
plt.show()
cv2.waitKey(0)

blank = np.zeros((img.shape[:2]), dtype='uint8')
cv2.imshow('Blank', blank)
cv2.waitKey(0)

circle = cv2.circle(blank.copy(), (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
cv2.imshow('Circle', circle)
cv2.waitKey(0)

mask = cv2.bitwise_and(gray,gray,mask=circle)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

hist2 = cv2.calcHist([gray],[0],mask,[256],[0,256])

plt.figure()
plt.title('Histogram 2')
plt.plot(hist2)
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.xlim([0,250])
plt.show()
cv2.waitKey(0)

masked = cv2.bitwise_and(img,img,mask=circle)
cv2.imshow("Masked", masked)
cv2.waitKey(0)

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
colors = ('r','g','b')
for i,col in enumerate(colors):
    hist = cv2.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim = [0,256]
plt.show()
cv2.waitKey(0)

