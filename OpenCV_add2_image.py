import cv2
import numpy as np

img1 =cv2.imread('C:/Users/tieut/Desktop/Document_Python/picture/3D-Matplotlib.png')
img2 =cv2.imread('C:/Users/tieut/Desktop/Document_Python/picture/mainsvmimage.png')
img3 =cv2.imread('C:/Users/tieut/Desktop/Document_Python/picture/mainlogo.png')
# add = img1 +img2
#add = cv2.add(img1.img2)
##add = cv2.addWeighted(img1,0.6,img2,0.4,0)
##cv2.waitKey(0)
##cv2.destroyWindows()
# I want put logo on top-left corner, SO I create a ROI
rows,cols,channels = img3.shape
roi=img1[0:rows,0:cols]
#Now create a mask of logo and create its inverse mask
img3gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
#add a threshold
ret ,mask = cv2.threshold(img3gray,220,255,cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)
#Now black -out the area of logo in ROI
img1_bg =cv2.bitwise_and(roi,roi,mask=mask_inv)
#Take only region of logo from logo image

img3_fg = cv2.bitwise_and(img3,img3, mask=mask)
dst = cv2.add(img1_bg,img3_fg)
img1[0:rows,0:cols]=dst
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
