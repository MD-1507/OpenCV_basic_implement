import cv2
import numpy as np

img = cv2.imread(r"C:\Users\91982\Desktop\CV\samurai.jpg")
cv2.imshow('Samurai',img)
cv2.waitKey(0)

blank = np.zeros((img.shape[:2]),dtype='uint8')
cv2.imshow('Blank', blank)
cv2.waitKey(0)

mask = cv2.circle(blank.copy(),(blank.shape[1]//2,blank.shape[0]//2),75,255,-1)
cv2.imshow('Mask', mask)
cv2.waitKey(0)

mask2 = cv2.rectangle(blank.copy(),(blank.shape[1]//2,blank.shape[0]//2),(blank.shape[1]//2+100,blank.shape[0]//2+100),255,-1)
cv2.imshow('Mask2', mask2)
cv2.waitKey(0)

masked = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("Masked", masked)
cv2.waitKey(0)

masked2 = cv2.bitwise_and(img,img,mask=mask2)
cv2.imshow("Masked2", masked2)
cv2.waitKey(0)

rect = cv2.rectangle(blank.copy(),(30,30),(275,275), 255, -1)
cv2.imshow('r',rect)
cv2.waitKey(0)

cir = cv2.circle(blank.copy(), (img.shape[1]//2,img.shape[0]//2),50,255,-1)
weird_shape = cv2.bitwise_and(cir, rect)
cv2.imshow('Weird Shape', weird_shape)
cv2.waitKey(0)

masked3 = cv2.bitwise_and(img,img,mask=weird_shape)
cv2.imshow("Masked3", masked3)
cv2.waitKey(0)
