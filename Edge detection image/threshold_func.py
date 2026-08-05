import cv2

image=cv2.imread(r"C:\Users\ACER\Downloads\flower.jpg",cv2.IMREAD_GRAYSCALE)

ret,thres_image=cv2.threshold(image,100,255,cv2.THRESH_BINARY)

cv2.imshow("Original Image",image)
cv2.imshow("Edges",thres_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
