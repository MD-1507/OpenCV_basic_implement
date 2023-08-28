import cv2
import numpy as np
import matplotlib.pyplot  as plt

img =cv2.imread(r"C:\Users\91982\Desktop\CV\face 1.jpg")
cv2.imshow('Face', img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)

haar_cascade = cv2.CascadeClassifier(r'C:\Users\91982\Desktop\CV\haar_faces.xml')

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)
print('NUmber of faces = ',len(face_rect))

for (x,y,w,h) in face_rect:
      rect = cv2.rectangle(img, (x,y), (x+h,y+w), (0,255,0), thickness = 2)

cv2.imshow('Detected Images', img)
cv2.waitKey(0)