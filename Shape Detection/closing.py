import cv2
import numpy as np

image=cv2.imread(r"C:\Users\ACER\Downloads\image.jpg",0)

_,thresh=cv2.threshold(image,127,255,cv2.THRESH_BINARY)

kernel=np.ones((105,105),np.uint8)
closed=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)

cv2.imshow("Original Image",thresh)
cv2.imshow("Closing",closed)

cv2.waitKey(0)
cv2.destroyAllWindows()