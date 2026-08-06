import cv2

image=cv2.imread(r"Shapes.png")

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_, thresh=cv2.threshold(gray,140,255,cv2.THRESH_BINARY)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


count = 1

for contour in contours:

    area = cv2.contourArea(contour)

    if area > 500:

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)

        cv2.putText(
            image,
            f"Object {count}",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0,0,255),
            2
        )

        count += 1

cv2.imshow("Bounding Rectangle",image)

cv2.waitKey(0)
cv2.destroyAllWindows()