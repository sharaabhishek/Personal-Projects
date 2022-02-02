import cv2 as cv
import numpy as np

def cross():
    pass

img1 = cv.imread("iron.jpg")
img1 = cv.resize(img1,(600,800))
img2 = cv.imread("root.jpg")
img2 = cv.resize(img2,(600,800))

# cv.imshow("Iron",img1)
# cv.imshow("Root",img2)
#main  trackingWindow
cv.namedWindow("Win")
img = np.zeros((600,800,3),np.uint8)

cv.createTrackbar("alpha","Win",0,100,cross)
cv.createTrackbar("0:ON\1:OFF","Win",0,1,cross)

while True:

    #getting details of trackBars of alpha
     n = cv.getTrackbarPos("alpha","Win")
     p = float(n/100)
     
     #getting details of trackBars for on and off
     s = cv.getTrackbarPos("0:ON\1:OFF","Win")

     if s == 0:
         dst = img
     else:
      dst = cv.addWeighted(img1,1-p,img2,p,0)
      cv.putText(dst,"alpha : " + str(n),(20,50),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            
     cv.imshow("Image",dst)
     if cv.waitKey(1) & 0xff == ord("q"):
            break
     

cv.waitKey(0)
cv.destroyAllWindows()