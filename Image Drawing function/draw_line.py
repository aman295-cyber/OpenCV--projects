import cv2

image = cv2.imread(r"C:\Users\ACER\Downloads\R.jpg")

if image is None:
    print("could not load image")
else:
    print("image loaded succesfully")

    pt1=(50,100)
    pt2=(300,100)

    color=(255,100,255)
    thickness=4

    cv2.line(image,pt1,pt2,color,thickness)
    cv2.imshow("Line draw", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()