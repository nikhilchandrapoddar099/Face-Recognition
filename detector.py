import cv2,os
import numpy as np
from PIL import Image
import pickle

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)
path = 'dataSet'

cam = cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)

        if(nbr_predicted==1):
             nbr_predicted='Nikhil'
        elif (nbr_predicted == 2):
            nbr_predicted = 'Harsh'
        elif(nbr_predicted==3):
            nbr_predicted='pranab'
        elif (nbr_predicted == 4):
            nbr_predicted = 'Vickey'
        elif (nbr_predicted == 5):
            nbr_predicted = 'priyanshu'
        else:
            nbr_predicated = 'unknown'

        cv2.putText(im,str(nbr_predicted)+"--"+str(conf),(x,y+h),font,0.55,(0,255,0),1)
        cv2.imshow('im',im)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()



