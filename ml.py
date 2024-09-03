import torch
import csv
import cv2
import time
import pandas as pd
from datetime import datetime
from ultralytics import YOLO
import yaml

# Load the YOLOv8 model directly using Ultralytics YOLO
model = YOLO('Yolo-Weights/yolov8l.pt')  # Load local YOLOv8 model

# Define the video source (e.g., a video file or webcam)
video_source = input("Enter the path of the video: ")  # Or use 0 for webcam
csv_sink = input("Enter the path of the CSV: ")  # Or use 0 for webcam

# Open the video source
cap = cv2.VideoCapture(video_source)

# Initialize a list to store the results
results = []

head=['Timestamp (ms)','Cars','Bus','Truck','Three-Wheeler','Two-Wheeler','LCV','Bicycle']
with open(csv_sink, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(head)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference using YOLOv8
    results = model(frame)

    # Extract bounding boxes and labels (adjust this part based on YOLOv8 output format)
    detections = results[0].boxes.data  # Assuming YOLOv8 returns a list of results

    # Filter for vehicle classes (e.g., car, truck, bus)
    vehicle_classes = [0,2]  # Replace with actual class indices for car, truck, bus

    # Use torch operations to filter the tensorq
    vehicle_detections = detections[torch.isin(detections[:, -1], torch.tensor(vehicle_classes))]

    # Count vehicles
    vehicle_count = len(vehicle_detections)

    #Similarly,
    bus_detections = detections[torch.isin(detections[:, -1], torch.tensor([0,5]))]
    bus_count = len(bus_detections)
    truck_detections = detections[torch.isin(detections[:, -1], torch.tensor([0,7]))]
    truck_count = len(truck_detections)
    TW_detections = detections[torch.isin(detections[:, -1], torch.tensor([0,3]))]
    TW_count = len(TW_detections)
    bicycle_detections = detections[torch.isin(detections[:, -1], torch.tensor([0,1]))]
    bicycle_count = len(bicycle_detections)

    #cv2_imshow('Vehicle Detection')
    #if cv2.waitKey(1000) & 0xFF == ord('q'):
        #break

    # Save results to a CSV file
    list = [cap.get(cv2.CAP_PROP_POS_MSEC),vehicle_count,bus_count,truck_count,'Null',TW_count,'Null',bicycle_count]
    with open(csv_sink, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(list)

cap.release()
cv2.destroyAllWindows()