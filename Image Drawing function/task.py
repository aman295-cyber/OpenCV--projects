import cv2

image = cv2.imread(r"C:\Users\ACER\Downloads\R.jpg")

cv2.rectangle(image, (80, 60), (450, 180), (0, 255, 0), 3)

cv2.putText(
    image,
    "OpenCV Learning",
    (100, 120),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 0, 0),
    2
)

cv2.imshow("OpenCV", image)
cv2.waitKey(0)
cv2.destroyAllWindows()