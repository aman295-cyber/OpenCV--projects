import cv2

image = cv2.imread(r"C:\Users\ACER\Downloads\spider.jpg")

if image is not None:
    cv2.imshow("Image showing",image) #open the window
    cv2.waitKey(0) # wait for key
    cv2.destroyAllWindows() # close the window
else:
    print("could not load the image")    