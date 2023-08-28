import cv2

img = cv2.imread(r'C:\Users\91982\Desktop\CV\samurai.jpg',-1)
img_gs = cv2.imread(r'C:\Users\91982\Desktop\CV\samurai.jpg',0)
img_og = cv2.imread(r'C:\Users\91982\Desktop\CV\samurai.jpg',1)

print(img)

cv2.imshow('Samurai',img)
cv2.waitKey(0)

cv2.imshow('Samurai',img_gs)
cv2.waitKey(0)

cv2.imshow('Samurai',img_og)
cv2.waitKey(0)

cap = cv2.VideoCapture(r'C:\Users\91982\Desktop\CV\CV_vid.mp4')
while True:
    isTrue, frame = cap.read()
    cv2.imshow('Video', frame)

    if cv2.waitKey(20) & 0xFF == ord('f'):
        break

cap.release()
cv2.destroyAllWindows()
