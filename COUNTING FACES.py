import cv2
import numpy as np

face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#face_eye=cv2.CascadeClassifier("haarcascade_eye.xml")
cap=cv2.VideoCapture(0)

while cap.isOpened():
    _,img=cap.read()

    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(img,1.1,5) # x,y,w,h values
    

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h) ,(125,0,255),4)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        #cv2.putText(roi_color,'harsh',(30,35),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        '''
        eye=face_eye.detectMultiScale(roi_gray,1.1,5)
        for (ex,ey,ew,eh) in eye:
            a=cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh) ,(125,142,0),4)
            #if bool(a) == False:
             #   print('blink')q
             '''

    c=len(faces)
    
    cv2.putText(img,str(c)+' faces',(400,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    cv2.imshow("image",img)
    if cv2.waitKey(1)==27:
        break
print(c)
cap.release()
cv2.destroyAllWindows()



