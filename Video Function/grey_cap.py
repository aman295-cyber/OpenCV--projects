import cv2

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()

    if not ret:
        print("Could Not read Frame")
        break

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("WebCam Feed", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting....")
        break
cap.release()
cv2.destroyAllWindows()