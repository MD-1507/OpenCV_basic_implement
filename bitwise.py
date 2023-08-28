import cv2
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv2.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv2.circle(blank.copy(),(200,200),200,255,-1)

cv2.imshow('Rectangle', rectangle)
cv2.imshow('Circle', circle)

cv2.waitKey(0)

# BITWISE AND --> intersecting regions
bitwise_and = cv2.bitwise_and(circle,rectangle)
cv2.imshow('Bitwise And', bitwise_and)
cv2.waitKey(0)

# BITWISE OR --> non intersecting and intersecting regions
bitwise_or = cv2.bitwise_or(circle,rectangle)
cv2.imshow('Bitwise Or', bitwise_or)
cv2.waitKey(0)

# BITWISE XOR --> non intersecting regions
bitwise_xor = cv2.bitwise_xor(circle,rectangle)
cv2.imshow('Bitwise XOR', bitwise_xor)
cv2.waitKey(0)

# BITWISE NOT --> complement region
bitwise_not_rectangle = cv2.bitwise_not(rectangle)
cv2.imshow('Bitwise NOT Rectangle', bitwise_not_rectangle)
cv2.waitKey(0)

# BITWISE NOT --> complement region
bitwise_not_circle = cv2.bitwise_not(circle)
cv2.imshow('Bitwise NOT Circle', bitwise_not_circle)
cv2.waitKey(0)