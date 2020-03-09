import numpy as np
import cv2

img = cv2.imread('picture.jpg',-1)
cv2.line(img,(0,0),(200,300),(0,0,0),5)#para: where, toa do bd, toa do kt,color,widthline
cv2.rectangle(img,(100,200),(200,400),(0,0,255),15)
cv2.circle(img,(100,63),63,(0,0,0),-1)
pts = np.array([[100,50],[200,300],[700,200],[500,100]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),3)
font =cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!',(0,350),font,4,(200,255,155),13,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
