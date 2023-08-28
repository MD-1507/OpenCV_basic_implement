import cv2

#
# img = cv2.imread(r"C:\Users\91982\Desktop\samurai.jpg",1)

# print(img)

# cv2.waitKey(0)

# cv2.imshow('Samurai',img)
# cv2.waitKey(5000)

def rescaleFrame(frame,scale=0.20):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


#
capture = cv2.VideoCapture(r"C:\Users\91982\Desktop\CV\CV_vid.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv2.imshow('Video',frame)
    cv2.imshow('Video_Resized',frame_resized)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()

cv2.waitKey(0)