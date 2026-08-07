import cv2
import numpy as np

image=cv2.imread(r"C:\Users\ACER\Downloads\image.jpg",0)

_,thresh=cv2.threshold(image,127,255,cv2.THRESH_BINARY)

kernel=np.ones((3,3),np.uint8)

gradient=cv2.morphologyEx(thresh,cv2.MORPH_GRADIENT,kernel)

cv2.imshow("Original Image",thresh)
cv2.imshow("Gradient",gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()