import cv2
import numpy as np

image = np.zeros((500,500,3), dtype=np.uint8)

cv2.circle(image, (100,100), 50, (255,255,255), -1)
cv2.rectangle(image, (200,50), (350,200), (255,255,255), -1)

triangle = np.array([[100,300],[50,450],[150,450]])
cv2.fillPoly(image, [triangle], (255,255,255))

cv2.imwrite("Shapes.png", image)


cv2.imshow("Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()