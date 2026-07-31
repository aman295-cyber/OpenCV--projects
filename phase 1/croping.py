import cv2

image = cv2.imread(r"spider.png")

(h,w)=image.shape[:2]

cropped = image[100:200, 100:300]

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()