import cv2
import numpy as np

image=cv2.imread(r"C:\Users\ACER\Downloads\image.jpg",0)

_,thresh=cv2.threshold(image,127,255,cv2.THRESH_BINARY)

kernel=np.ones((15,15),np.uint8)

dilated = cv2.dilate(image, kernel, iterations=3)

cv2.imshow("Original Image",thresh)
cv2.imshow("Dilation",dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()