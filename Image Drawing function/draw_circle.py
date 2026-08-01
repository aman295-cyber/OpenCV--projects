import cv2

image = cv2.imread(r"C:\Users\ACER\Downloads\R.jpg")
print(image.shape)

if image is None:
    print("could not load image")
else:
    print("image loaded succesfully")

    cv2.circle(image,(500,300),200,(0,165,255),-1)
    cv2.imshow("Circle draw", image)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()
