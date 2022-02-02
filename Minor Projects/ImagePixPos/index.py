import cv2 as cv
from cv2 import WINDOW_NORMAL
from cv2 import resize
import numpy as np

def mouse_Event(event,x,y,flag,param):

    if event == cv.EVENT_LBUTTONDOWN:
        text = "x = " + str(x) + ",y " + str(y)
        cv.putText(img,text,(x,y),cv.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)

    if event == cv.EVENT_RBUTTONDOWN:
        b = img[x , y , 0] #for blue channel is 0
        g = img[x , y , 1] #for green channel is 1
        r = img[x , y , 2] #for red channel is 2

        color_bgr = ". " + str(b) + ", " + str(g) + ", " + str(r)
        cv.putText(img,color_bgr,(x,y),cv.FONT_HERSHEY_COMPLEX,0.4,(152,255,130),1)

cv.namedWindow("Res",WINDOW_NORMAL)
cv.setMouseCallback("Res",mouse_Event)

img = cv.imread("abhi1.png")
img = cv.resize(img,0,960,1080)
while True:
    cv.imshow("Res",img)
    if cv.waitKey(1) & 0xff == ord('q'):
     break

cv.destroyAllWindows()