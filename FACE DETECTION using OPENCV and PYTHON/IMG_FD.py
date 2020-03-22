import cv2
import numpy as np 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Get the image 
img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),16)

#Display the output

cv2.namedWindow('PROCESSED IMAGE', cv2.WINDOW_NORMAL)
cv2.imshow('PROCESSED IMAGE', img)
#cv2. resizeWindow('PROCESSED IMAGE',1827,1539)

cv2.waitKey()
cv2. destroyAllWindows()

