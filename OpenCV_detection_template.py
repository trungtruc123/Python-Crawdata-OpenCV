import cv2
import numpy as np

img = cv2.imread('E:/Document_Python/picture/opencv-template-matching-python-tutorial.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('E:/Document_Python/picture/opencv-template-for-matching.jpg',0)# tham so 0 vi picture too small
w,h = template.shape[::-1] #lay -1 vi w,h phai doc nguoc lai : vd Matrix 3x2 w=2,h=3

res = cv2.matchTemplate(img_gray,template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8# nguong : co the thay doi(0.7,0.8,0.9,...)
loc = np.where(res >=threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,125,255),4)# pt[0]+w : vi tri cua no cong chieu rong, pt[1]+h : vi tri chieu cao cua no + chieu cao => ve hinh chu nhat vo
    # (0,125,255): mau sac
    # 4 : widthline
cv2.imshow('Detected',img)
#cv2.destroyAllWindows()
