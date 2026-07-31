import cv2

image_path=input("Enter image path:")
image=cv2.imread(image_path)

if image is not None:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    output_name=input("Enter Output image name:")

    if cv2.imwrite(output_name, gray):
     
     print(f"Image saved Successfully as '{output_name}' ")

    else:
     
     print("Failed to save the image")
     
else:
    print("Error:could not load the image")

