import cv2

image = cv2.imread(r"C:\Users\ACER\Downloads\spider.jpg")

if image is not None:
    h, w, c =image.shape
    print(f"Image loaded:\nheight: {h}\nwidth:{w}\nchannels: {c}")
else:
    print("Could not load image")