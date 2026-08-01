import cv2

image=cv2.imread(r"C:\Users\ACER\Downloads\R.jpg")

if image is None:
    print("Error: Image Not Found")
    exit()

while True:
 print("1. Draw Line")
 print("2. Draw Rectangle")
 print("3. Draw Circle")
 print("4. Write Text")
 print("5. Save Image")
 print("6. Show Current Image")
 print("7. Exit")

 choice = input("Enter Choice:" )
   #--------------Line--------------#
 if choice=="1":
    x1=int(input("Enter x1: "))
    y1=int(input("Enter y1: "))
    x2=int(input("Enter x2: "))
    y2=int(input("Enter y2: "))

    cv2.line(image,(x1, y1), (x2, y2), (50,100,250), 3)

    print("Line Drawn Successfully")

    #--------------- Rectangle--------------#

 elif choice == "2":
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    cv2.rectangle(image, (x1,y1), (x2,y2), (50,200,50), 3)

    print("Rectangle Drawn Successfully")
     #-----------------Circle----------------#
 elif choice == "3":
    x1=int(input("Enter x1: "))
    y1=int(input("Enter y1: "))
    r=int(input("Radius: "))

    cv2.circle(image,(x1,y1), r, (70,90,200), 3 )

    print("Circle Drawn Successfully")

      #----------------Text----------------#

 elif choice == "4":

    text=input("Enter Text: ")
    x=int(input("X Position: "))
    y=int(input("Y Position: "))

    cv2.putText(image, text, (x,y), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (222,100,150), 4)

    print("Text Added Successfully")

     #-----------------Save Image------------#

 elif choice == "5":
    filename=input("Enter File Name:")

    if"." not in filename:
       filename += ".jpg"

    cv2.imwrite(filename,image)

    print("Image saved Successfully")

     #--------------------Show Image-----------------#

 elif choice == "6":
    cv2.imshow("Drawing Tool",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #---------------------Exit----------------------------

 elif choice == "7":
    print("Thank You !!!!")
    exit()

else:
   print("Invalid Choice !!!!!")
    


