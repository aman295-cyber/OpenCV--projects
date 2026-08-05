import cv2
import numpy as np

image=np.zeros((300,300),dtype=np.uint8)


cv2.rectangle(image,(50,50),(250,250),255,-1)


bitwise_not=cv2.bitwise_not(image)

cv2.imshow("Rectangle",image)
cv2.imshow("AND",bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()