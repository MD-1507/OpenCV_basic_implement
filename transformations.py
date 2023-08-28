import cv2
import numpy as np

img  = cv2.imread(r"C:\Users\91982\Desktop\CV\samurai.jpg")

cv2.imshow('Samurai', img)

cv2.waitKey(0)

# Translation
def translation(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

# -x --> left
# x --> right
# -y --> down
# y --> up

translated = translation(img,100,100)
cv2.imshow('Translation', translated)

cv2.waitKey(0)

# Rotation

def rotation(img , angle, rotPoint=None):
    (height,width)= img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotMat, dimensions)

rotated = rotation(img, 45)
cv2.imshow('Rotation', rotated)

cv2.waitKey(0)

# Resize
resized = cv2.resize(img, (500,500), interpolation= cv2.INTER_CUBIC)
cv2.imshow('Resized',resized)

cv2.waitKey(0)

# Flip
flip = cv2.flip(img, 1)
cv2.imshow('Flip', flip)

cv2.waitKey(0)

# flip2 = cv2.flip(img, -1)
# cv2.imshow('Flip2', flip2)

# cv2.waitKey(0)

#Crop
cropped = img[200:300,300:400]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)


