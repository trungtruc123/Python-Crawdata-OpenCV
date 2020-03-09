import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)# hue saturation value: bao hoa gia tri mau

    lower_red =np.array([30,0,0])
    upper_red =np.array([180,255,255])

    mask = cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(frame, frame, mask =mask)
    cv2.imshow('origin',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)#result
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
