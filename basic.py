import cv2

img = cv2.imread(r"C:\Users\91982\Desktop\CV\samurai.jpg")
cv2.imshow('Samurai',img)

# Converting to GrayScale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

cv2.waitKey(0)

# Blur
blur = cv2.GaussianBlur(img, (5,5), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)

cv2.waitKey(0)

# Edge Cascade
canny = cv2.Canny(img, 125, 175)
cv2.imshow('Cascade Edges', canny)

cv2.waitKey(0)

# canny = cv2.Canny(blur, 125, 175)
# cv2.imshow('Cascade Edges', canny)

# cv2.waitKey(0)


# Dilating the image
dilated = cv2.dilate(canny, (7,7), iterations=4)
cv2.imshow('Dilated', dilated)

cv2.waitKey(0)

#Erode
eroded = cv2.erode(canny, (3,3), iterations=1)
cv2.imshow('Eroded', eroded)

cv2.waitKey(0)

#Resize
resized = cv2.resize(img,(600,600))
cv2.imshow('Resized',resized)

cv2.waitKey(0)

# resized1 = cv2.resize(img,(600,600),interpolation=cv2.INTER_CUBIC)
# cv2.imshow('Resized1',resized1)

# cv2.waitKey(0)

# resized2 = cv2.resize(img,(600,600),interpolation=cv2.INTER_LINEAR)
# cv2.imshow('Resized2',resized2)

# cv2.waitKey(0)

# resized3 = cv2.resize(img,(600,600),interpolation=cv2.INTER_AREA)
# cv2.imshow('Resized3',resized3)

# cv2.waitKey(0)

# Cropped
cropped = img[50:200, 300:400]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)
