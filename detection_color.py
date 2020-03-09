import numpy as np
import pandas as pd
import cv2
# import argparse
# ap = argparse.ArgumentParser()
# ap.add_argument('-i','--image',required =True , help ="Image Path")
# args = vars(ap.parse_args())
# # print(args)
# img_path = args['image']
# img = cv2.imread(img_path)

img = cv2.imread('colorpic.jpg')
#  global variable (used after)
clicked =False
r = g= b = xpos = ypos =0

# read csv
index =['color','color_name','hex','R','G','B']
csv = pd.read_csv('‪‪colors.csv',header = None, names =index)

def draw_function(event, x,y,flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global r,g,b, xpos, ypos, clicked
        clicked =True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        r = int(r)
        b = int(b)
        g = int(g)
#  function getColorName trả về tên màu ( so sánh (r,g,b) khi kích chuột vào ảnh với từng giá trị trong csv, lấy sai lệch nhỏ nhất => cname)
def getColorName(R,G,B):
    minimum =10000
    j=0 # Biến lưu vị trí c_name
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, 'R'])) + abs ( G - int(csv.loc[i,'G'])) + abs( B - int(csv.loc[i,'B']))
        if d< minimum:
            minimum =d
            j = i
    cname = csv.loc[j,'color_name']
    return cname
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)
while(1):
    cv2.imshow('image',img)
    if(clicked):
        #rectangle ( img, (x,y),(x+w,y+h),(color),thickness) thickness =-1 : fill entirely rectangle
        cv2.rectangle(img, (20,20),(750,60),(b,g,r), -1)
        #create text diplay name color , value RGB
        text = getColorName(r,g,b) + 'R:' + str(r) +'G:'+ str(g)+ 'B:'+ str(b)
         #cv2.putText(img,text,start,font(0-7), fontScale, color, thickness, lineType, (optional bottomLeft bool) 
        cv2.putText(img, text, (50,50),2,0.8,(255,255,255),2,cv2.line_AA)
        # if color light => background color :dark
        if(r+g+b>=600):
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.line_AA)
    clicked = False
    if cv2.waitKey(20) & 0xFF ==27:
        # ESC to exit
        break
cv2.destroyAllWindows()


