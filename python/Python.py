#Face tracker using OpenCV and Arduino
#by Shubham Santosh

import cv2
import serial
import time
face_cascade= cv2.CascadeClassifier('data.xml')
cap=cv2.VideoCapture(0)
#fourcc= cv2.VideoWriter_fourcc(*'XVID')
ArduinoSerial=serial.Serial('com30' , 9600 , timeout=0.1)
#out= cv2.VideoWriter('face detection4.avi',fourcc,20.0,(640,480))
time.sleep(1)

while cap.isOpened():
    ret, frame= cap.read()
    frame=cv2.flip(frame,1)  #mirror the image
    #print(frame.shape)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray,1.1,6)  #detect the face

    if len(faces)>=1:
       print('1')
       ArduinoSerial.write(b'1')
    else:
        print('0')
        ArduinoSerial.write(b'0')




    for x,y,w,h in faces:
        
        if len(faces)>=1:
           ArduinoSerial.write(b'1')
        elif len(faces)==0:
            ArduinoSerial.write(b'0')
        #plot the center of the face
        cv2.circle(frame,(x+w//2,y+h//2),2,(0,255,0),2)
        #plot the roi
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
      
    
    cv2.imshow('img',frame)
    #cv2.imwrite('output_img.jpg',frame)
    '''for testing purpose
    read= str(ArduinoSerial.readline(ArduinoSerial.inWaiting()))
    time.sleep(0.05)
    print('data from arduino:'+read)
    '''
    # press q to Quit
    if cv2.waitKey(10)&0xFF== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()