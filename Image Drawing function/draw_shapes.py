import cv2

image = cv2.imread(r"C:\Users\ACER\Downloads\R.jpg")

#line

cv2.line(image,(300,400),(600,400),(90,200,100),3)

#rectangle

cv2.rectangle(image,(300,300),(500,200),(78,120,250),4)

#circle

cv2.circle(image,(300,400),100,(100,15,200),-1)

cv2.imshow("All Shapes draw", image)
    
cv2.waitKey(0)
cv2.destroyAllWindows()