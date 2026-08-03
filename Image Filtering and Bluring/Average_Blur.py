import cv2

image=cv2.imread(r"C:\Users\ACER\Downloads\Animal.jpg")

if image is None:
    print("Could not load the image")

else:

    blur=cv2.blur(image,(5,5))

    cv2.imshow("Original Image",image)

    cv2.imshow("Blur Image",blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
