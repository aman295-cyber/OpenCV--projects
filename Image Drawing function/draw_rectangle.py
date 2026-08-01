import cv2

image = cv2.imread(r"C:\Users\ACER\Downloads\R.jpg")

if image is None:
    print("could not load image")
else:
    print("image loaded succesfully")

    pt1=(500,400)
    pt2=(200,200)
    

    color=(0,0,200)
    thickness=6

    cv2.rectangle(image,pt1,pt2,color,thickness)

    cv2.imshow("Rectangle draw", image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()