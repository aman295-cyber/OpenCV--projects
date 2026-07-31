import cv2

image = cv2.imread(r"spider.png")

if image is None:
    print("could not load image")
else:
    (h,w)=image.shape[:2]

    center=(w//2,h//2)

    M=cv2.getRotationMatrix2D(center,180,1.0)
    rotated=cv2.warpAffine(image, M, (w,h))

    cv2.imshow("original",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow("Rotated Image",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 