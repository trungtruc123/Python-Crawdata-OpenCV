import sys
import dlib
import cv2
from skimage import io

# image_path= sys.argv[1] #input parameter của script

img = io.imread('E:\\Document_Python\\picture\\ngu.jpg')
win = dlib.image_window()
win.clear_overlay()
win.set_image(img)

#
detector = dlib.get_frontal_face_detector() #Load face detector
dets = detector(img, 2)  #Xác định vị trí khuôn mặt trong bức ảnh
print(dets)
win.add_overlay(dets) #Vẽ khung hình bao quanh khuôn mặt
# Chuyển đổi từ (top, left, bottom, right) sang (x, y, w, h)
def dlib_to_opencv(rect):
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y
 
	# return a tuple of (x, y, w, h)
	return (x, y, w, h)
predictor = dlib.shape_predictor('E:\Document_Python\picture\shape_predictor_68_face_landmarks.dat')
for k, d in enumerate(dets):
    # Xác định facial landmark trên khuôn mặt thánh nữ
    print("k:{}, d:{}".format(k,d))
    shape = predictor(img, d)
    # Vẽ facial landmark lên bức ảnh
    win.add_overlay(shape)
cv2.imshow('picture',img)
cv2.waitKey(0)
cv2.destroyAllWindows()