import cv2

image=cv2.imread(r"C:\Users\ACER\Downloads\Animal.jpg")


blur=cv2.GaussianBlur(image,(5,5),2)

cv2.imshow("Original Image",image)
cv2.imshow("Blurred Image",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()



    