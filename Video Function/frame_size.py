import cv2

cap=cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("Width:", width)
print("Height:", height)

while True:
    ret, frame=cap.read()

    if not ret:
        print("Could Not read Frame")
        break
    cv2.imshow("WebCam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting....")
        break
    
cap.release()
cv2.destroyAllWindows()