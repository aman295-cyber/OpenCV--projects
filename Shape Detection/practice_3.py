import cv2
import numpy as np

# Read image in grayscale
image = cv2.imread(r"Shapes.png", 0)

if image is None:
    print("Could not load image!")
    exit()

# Binary Threshold
_, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

while True:

    print("\n===== OPENING AND CLOSING MENU =====")
    print("1. Kernel 3 x 3")
    print("2. Kernel 5 x 5")
    print("3. Kernel 7 x 7")
    print("4. Kernel 15 x 15")
    print("5. Kernel 25 x 25")
    print("6. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        kernel = np.ones((3, 3), np.uint8)

    elif choice == "2":
        kernel = np.ones((5, 5), np.uint8)

    elif choice == "3":
        kernel = np.ones((7, 7), np.uint8)

    elif choice == "4":
        kernel = np.ones((15, 15), np.uint8)

    elif choice == "5":
        kernel = np.ones((25, 25), np.uint8)

    elif choice == "6":
        print("Thank You!!!!!!!!!")
        break

    else:
        print("Invalid Choice!!!!!!!!")
        continue

        
    # Apply Opening
    opened=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)

    #Apply Closing
    closed=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
   
    # Display Images
    cv2.imshow("Original Image", thresh)
    cv2.imshow("Opening",opened)
    cv2.imshow("Closing",closed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()