import cv2
import numpy as np

image=cv2.imread(r"C:\Users\ACER\Downloads\image.jpg",0)

_,thresh=cv2.threshold(image,127,255,cv2.THRESH_BINARY)

kernel=np.ones((25,25),np.uint8)
opened=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)

cv2.imshow("Original Image",thresh)
cv2.imshow("Opening",opened)

cv2.waitKey(0)
cv2.destroyAllWindows()