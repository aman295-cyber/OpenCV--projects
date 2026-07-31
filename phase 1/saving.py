import cv2

image = cv2.imread(r"C:\Users\ACER\Downloads\download.png")

if image is not None:
    success=cv2.imwrite("spider.png",image) # output image
    if success:
        print("Image saved successfully as 'output.jpg'")
    else:
        print("failed to save image")
else:
    print("Error: could not load image")
