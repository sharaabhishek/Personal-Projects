import cv2 as cv
from cv2 import imshow
from cv2 import waitKey
import pyautogui as p
import numpy as np

#creating resolution
rs = p.size()

# creating fps
fps = 20.0

focuscc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('Output.avi',focuscc,fps,rs)

#create recording module

cv.namedWindow("Live Recording",cv.WINDOW_NORMAL)
cv.resizeWindow("Live Recording",(600,400))

while True:
    img = p.screenshot()
    
    frame = np.array(img)
    frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    out.write(frame)
    cv.imshow("Live Recording",frame)
    if waitKey(1) == ord("q"):
     break

out.release()
cv.destroyAllWindows()

