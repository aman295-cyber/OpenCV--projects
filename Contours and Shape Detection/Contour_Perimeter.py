import cv2

image=cv2.imread(r"C:\Users\ACER\Downloads\triangle_PNG82.png")

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_, thresh=cv2.threshold(gray,140,255,cv2.THRESH_BINARY)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

Perimeter=cv2.arcLength(contours[0],True)
print("Perimeter:",Perimeter)


cv2.drawContours(image,contours,-1,(100,150,100),2)

cv2.imshow("THRESHOLD",thresh)
cv2.imshow("Contours",image)

cv2.waitKey(0)
cv2.destroyAllWindows()