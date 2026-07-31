import cv2

image = cv2.imread(r"C:\Users\ACER\Downloads\spider.jpg")

small=cv2.resize(image,None,fx=0.5,fy=0.5)
large=cv2.resize(image,None, fx=1,fy=0.5)

cv2.imshow("Small", small)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Large", large)
cv2.waitKey(0)
cv2.destroyAllWindows()


# resized=cv2.resize(image,(300,300))