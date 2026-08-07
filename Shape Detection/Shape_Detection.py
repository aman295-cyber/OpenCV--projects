
# =========================Automatic Shape Detector======================


import cv2

image=cv2.imread(r"Shapes.png")

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_, thresh=cv2.threshold(gray,140,255,cv2.THRESH_BINARY)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image,contours,-1,(0,250,0),2)

for contour in contours:
    area = cv2.contourArea(contour)

    if area < 500:
     continue

    approx=cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,True),True)
    corner=len(approx)
    print(len(approx))

    if corner == 3:
        shape_name="Triangle"

    elif corner == 4:
        
        x, y, w, h= cv2.boundingRect(approx)
        ratio=w/h
        if 0.95 <= ratio <= 1.05:
            shape_name = "Square"
        else:
            shape_name = "Rectangle"

    elif corner == 5:
        shape_name="Pentagon"

    elif corner == 6:
        shape_name="Hexagon"

    elif corner > 6:
        shape_name="Circle"

    else:
        shape_name="Unknown"
    
    cv2.drawContours(image,[approx],-1,(0,250,0),2)

    x, y, w, h = cv2.boundingRect(approx)

    cv2.putText(
    image,
    shape_name,
    (x, y - 10),
    cv2.FONT_HERSHEY_COMPLEX,
    0.6,
    (0,0,255),
    2
)

cv2.imshow("Shape Detector",image)

cv2.waitKey(0)
cv2.destroyAllWindows()