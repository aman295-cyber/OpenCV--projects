import cv2
import numpy as np

image1=np.zeros((300,300),dtype=np.uint8)
image2=np.zeros((300,300),dtype=np.uint8)

cv2.rectangle(image1,(50,50),(250,250),255,-1)
cv2.circle(image2,(200,100),100,255,-1)

bitwise_and=cv2.bitwise_and(image1,image2)

cv2.imshow("Rectangle",image1)
cv2.imshow("Circle",image2)
cv2.imshow("AND",bitwise_and)

cv2.waitKey(0)
cv2.destroyAllWindows()