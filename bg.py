import cv2
import numpy as np

cap=cv2.VideoCapture(0)
img_1=cv2.imread('download.jpg')

while True:
    ret,img=cap.read()
    img=cv2.resize(img,(640,480))
    img_1=cv2.resize(img_1,(640,480))
    upperblack=np.array([104,153,70])
    lowerblack=np.array([30,30,0])
    mask_1=cv2.inRange(img,lowerblack,upperblack)
    result=cv2.bitwise_and(img,img,mask=mask_1)
    f=img-result
    f=np.where(f==0,img_1,f)
    cv2.imshow('Magic',img)
    cv2.imshow('Mask',f)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()