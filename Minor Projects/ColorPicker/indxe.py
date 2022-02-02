import cv2 as cv
import numpy as np


def cross():
    pass

img = np.zeros((300,512,3),np.uint8)
cv.namedWindow("Color picking")

#switch trackBar
str = "0:OFF\n1:ON"
cv.createTrackbar(str,"Color picking",0,1,cross)

#creating rgb trackBar
r = "R"
g = "G"
b = "B"
cv.createTrackbar(r,"Color picking",0,255,cross)
cv.createTrackbar(g,"Color picking",0,255,cross)
cv.createTrackbar(b,"Color picking",0,255,cross)


while True:
    cv.imshow("Color picking",img)
    if cv.waitKey(1) & 0xff == ord('q'):
       break

    #get trackPositions
    s = cv.getTrackbarPos(str,"Color picking")
    r1 = cv.getTrackbarPos(r,"Color picking")
    g1 = cv.getTrackbarPos(g,"Color picking")
    b1 = cv.getTrackbarPos(b,"Color picking")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [r1,g1,b1]

cv.destroyAllWindows()