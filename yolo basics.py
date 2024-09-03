from ultralytics import YOLO
import cv2

model = YOLO('../Yolo-Weights/yolov7.pt')
results = model("images/crowd.jpg", show=True)
cv2.waitKey(0)
