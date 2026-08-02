import cv2
from datetime import datetime

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()

    if not ret:
        print("Could Not read Frame")
        break

    current_time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    cv2.putText(
        frame,current_time,
        (10,30),
        cv2.FONT_HERSHEY_PLAIN,
        1,
        (100,100,100),
        1
    )

    cv2.imshow("Live Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting....")
        break
cap.release()
cv2.destroyAllWindows()