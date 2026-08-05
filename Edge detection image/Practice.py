import cv2
import numpy as np

image1=np.zeros((300,300),dtype=np.uint8)
image2=np.zeros((300,300),dtype=np.uint8)

cv2.rectangle(image1,(50,50),(250,250),255,-1)
cv2.circle(image2,(200,100),100,255,-1)

while True:
    print("1.Bitwise_OR")
    print("2.Bitwise_AND")
    print("3.Bitwise_NOT")
    print("4.Bitwise_XOR")
    print("5.exit")

    choice=input("Enter Choice : ")

    if choice=="1":
        bitwise_or=cv2.bitwise_or(image1,image2)

        cv2.imshow("Rectangle",image1)
        cv2.imshow("Circle",image2)
        cv2.imshow("OR",bitwise_or)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice=="2":
        bitwise_and=cv2.bitwise_and(image1,image2)

        cv2.imshow("Rectangle",image1)
        cv2.imshow("Circle",image2)
        cv2.imshow("AND",bitwise_and)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == "3":
        bitwise_not=cv2.bitwise_not(image1)
        bitwise_not=cv2.bitwise_not(image2)

        cv2.imshow("Rectangle",image1,)
        
        cv2.imshow("Rectangle",image2,)
        cv2.imshow("NOT",bitwise_not)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == "4":

        bitwise_xor=cv2.bitwise_xor(image1,image2)
        cv2.imshow("Rectangle",image1)
        cv2.imshow("Circle",image2)
        cv2.imshow("XOR",bitwise_xor)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice =="5":
        print("Thank You!!!!!!!!!!!!")
        break

    else:
        print("Invalid Choice!!!!!!!!!!!!!!")



