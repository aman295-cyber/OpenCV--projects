
           #========================IMAGE FILTER MENU===========================

import cv2

image=cv2.imread(r"C:\Users\ACER\Downloads\Animal.jpg")

if image is None:
    print("Could Not Load image")
    exit()


while True:
    print("1. Average Blur")
    print("2. Gaussian Blur")
    print("3. Median Blur")
    print("4. Exit")

    


    choice=input("Enter Choice:")

    if choice == "1":

        kernel = int(input("Enter odd kernel size (3,5,7,9,11): "))

        average=cv2.blur(image,(kernel,kernel))

        cv2.imshow("Original Image",image)
        cv2.imshow("Average_Blur Image",average)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == "2":
        kernel = int(input("Enter odd kernel size (3,5,7,9,11): "))
        gaussian=cv2.GaussianBlur(image,(kernel,kernel),2)

        cv2.imshow("Original Image",image)
        cv2.imshow("Gaussian_Blur Image",gaussian)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == "3":
        kernel = int(input("Enter odd kernel size (3,5,7,9,11): "))
        median=cv2.medianBlur(image,kernel)

        cv2.imshow("Original Image",image)
        cv2.imshow("Median_Blur Image",median)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == "4":
        print("Thank You !!!!")
        break

    else:
        print("Inavalid choice!!!!")
