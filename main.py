import cv2
import pickle
import cvzone
import numpy as np
from itertools import zip_longest
import time

class main(listnya,vidnya):
    cap = cv2.VideoCapture('miniatur_park.mp4')

    with open('tempList','rb') as f:
     posList = pickle.load(f)

width, height = 80,105
objectDetect = cv2.createBackgroundSubtractorMOG2()

def thePark(resize,img):
    for i in posList:
        x,y = i
        imgCrop = img[y:y+height,x:x+width]
        count = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(resize,str(count),(x,y+height-5),scale = 1,thickness=1,offset=0)

        if count < 400:
            color = (0,0,255)
            thickness = 5
        else:
            color = (0,255,0)
            thickness = 2
        cv2.rectangle(resize,i,(i[0]+width,i[1]+height),(color),thickness)

while True : 

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    success, img = cap.read()

    resize = cv2.resize(img, (700, 500))
    imgGray = cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),2)
    imgTreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,35,5)
    imgMedian = cv2.medianBlur(imgTreshold,5)
    kernel = np.ones((3,3),np.uint8)
    imDial = cv2.dilate(imgMedian,kernel,iterations=1)

 
    thePark(resize,imDial) 

    cv2.imshow('resize',resize)
    cv2.imshow('imDial',imDial)
    cv2.waitKey(20)