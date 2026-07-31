import cv2

image = cv2.imread(r"C:\Users\ACER\Downloads\spider.jpg")

if image is not None:
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Grayscale image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Error: could not load image")