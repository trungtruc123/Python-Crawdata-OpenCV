import cv2
import numpy as np

cap = cv2.VideoCapture(0);#0,1,or video save
fourcc =cv2.VideoWriter_fourcc(*'XVID')
out  = cv2.VideoWriter('outputVideo.avi',fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()#return , frame
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#cvtColor = convert color
    out.write(frame)
    cv2.imshow('frame_oring',frame)
    cv2.imshow('frame_gray',gray)
    
    if cv2.waitKey(1)&0xFF ==ord('q'):
        break
cap.release()
out.release()#release: giai phong
cv2.destroyAllWindows()
