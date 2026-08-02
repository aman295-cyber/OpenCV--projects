import cv2
from datetime import datetime
cap=cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps=cap.get(cv2.CAP_PROP_FPS)

print("Width : ",width)
print("Height : ",height)
print("FPS : ",fps)

gray_mode=False


while True:
    ret, frame=cap.read()

    if not ret:
        print("Could Not read Frame")
        break

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    if gray_mode:
        display = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
       display = frame.copy()

    cv2.putText(
        display,
        current_time,
        (10,30),
        cv2.FONT_HERSHEY_PLAIN,
        1,
        (100,100,100),
        1
    )

    cv2.putText(
        display,
        f"Resolution : {width} x {height}",
        (10, 60),
        cv2.FONT_HERSHEY_PLAIN,
        1,
        255,
        1
    )

    cv2.putText(
        display,
        f"FPS : {fps:.0f}",
        (10, 90),
        cv2.FONT_HERSHEY_PLAIN,
        1,
        255,
        1
    )

    cv2.imshow("Live Camera", display)


  
    key = cv2.waitKey(1) & 0xFF

    if key == ord('g'):
        gray_mode= not gray_mode

    elif key== ord('s'):

        if gray_mode:

            cv2.imwrite("Gray_Photo.jpg",display)
        else:
           
           cv2.imwrite("Color_Photo.jpg", frame)

        print("Photo Saved!!!")

    elif key == ord('q'):
        print("Quitting.....")

        break

cap.release()
cv2.destroyAllWindows()