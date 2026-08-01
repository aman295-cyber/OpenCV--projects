import cv2

image = cv2.imread(r"C:\Users\ACER\Downloads\R.jpg")
print(image.shape)

if image is None:
    print("could not load image")
else:
    print("image loaded succesfully")

    cv2.putText(
        image,
        "Jabra Fan Spider Man",
        (100,100),
        cv2.FONT_HERSHEY_COMPLEX,
        1.2,
        (10,20,250),
        4
        )

    cv2.imshow("Adding text over image", image)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()
