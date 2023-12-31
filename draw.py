import cv2
import numpy as np

# img = cv2.imread(r"C:\Users\91982\Desktop\CV\samurai.jpg")
# cv2.imshow('Samurai',img)
# cv2.waitKey(0)

blank = np.zeros((500,500,3),dtype='uint8')
cv2.imshow('Blank',blank)
cv2.waitKey(0)

# 1) Paint the image a certain colour
# blank[200:300, 300:400]=0,255,0 # B G R channel values 
# cv2.imshow('Green',blank)

# cv2.waitKey(0)

# blank[:]=0,0,255 # R G B channel values 
# cv2.imshow('Red',blank)

# cv2.waitKey(0)

# 2) Draw a Rectangle
# cv2.rectangle(blank,(0,0),(250,250),(0,0,255),thickness = 2)
# cv2.imshow('Rectangle',blank)

# cv2.waitKey(0)

# cv2.rectangle(blank,(0,0),(250,250),(0,0,255),thickness = cv2.FILLED)
# cv2.imshow('Rectangle',blank)

# cv2.waitKey(0)

# cv2.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,255,0),thickness = -1)
# cv2.imshow('Rectangle',blank)

# cv2.waitKey(0)

# 3) Draw a circle 
# cv2.circle(blank, (blank.shape[0]//2,blank.shape[1]//2),40,(255,0,0),thickness=3)
# cv2.imshow('Circle',blank)

# cv2.waitKey(0)

# 4) Draw a line
# cv2.line(blank, (0,0), (blank.shape[0]//2,blank.shape[1]//2),(255,255,255), thickness=3)
# cv2.imshow('Line',blank)

# cv2.waitKey(0)

# cv2.line(blank, (100,250),(300,400),(255,255,255), thickness=3)
# cv2.imshow('Line',blank)

# cv2.waitKey(0)

# 5) Write text
# cv2.putText(blank, 'HELLO', (255,255), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
# cv2.imshow('Text', blank)

# cv2.waitKey(0)

cv2.putText(blank, 'Hello, my name is Mayank', (0,255), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv2.imshow('Text', blank)

cv2.waitKey(0)