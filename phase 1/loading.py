import cv2

image = cv2.imread(r"C:\Users\ACER\Downloads\spider.jpg")

if image is None:
    print("Error :image is not found")
else:
    print("image successfully loaded")    