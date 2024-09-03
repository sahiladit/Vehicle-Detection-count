Vehicle Detection and Counting using YOLOv7 and PyTorch

This repository contains a Python project that leverages YOLOv7, a state-of-the-art object detection model, to detect and count various types of vehicles in video streams. The project is built using PyTorch and provides a comprehensive solution for real-time vehicle monitoring, which can be applied in traffic management, surveillance, and other related fields.

Table of Contents
Introduction
Features
Installation
Usage
Output
Customization
Contributing
License
Introduction
This project is designed to detect and count different types of vehicles in video streams using the YOLOv7 model. The output is stored in a CSV file, where each entry corresponds to the number of detected vehicles at specific timestamps.

Features
Real-time vehicle detection and counting using YOLOv7 and PyTorch.
Supports multiple vehicle classes: Cars, Buses, Trucks, Two-Wheelers, Bicycles, etc.
Outputs results in a CSV file with the following columns:
Timestamp (ms)
Cars
Bus
Truck
Three-Wheeler
Two-Wheeler
LCV
Bicycle
Customizable for different datasets and vehicle types.
Installation
To set up the project locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/vehicle-detection-yolov7.git
cd vehicle-detection-yolov7
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Download the YOLOv7 model weights and place them in the Yolo-Weights directory.

Usage
To run the vehicle detection and counting:

Prepare your video source (e.g., a video file or webcam).

Run the script:

bash
Copy code
python detect_vehicles.py
Enter the required inputs:

The path to the video file.
The path to save the CSV output file.
The script will process the video and generate the output CSV file.

Output
The script generates a CSV file with the following structure:

Timestamp (ms)	Cars	Bus	Truck	Three-Wheeler	Two-Wheeler	LCV	Bicycle
0.0	23	3	4	Null	1	Null	1
33.333	22	2	3	Null	0	Null	0
...	...	...	...	...	...	...	...
Each row corresponds to a specific timestamp in the video and shows the count of each vehicle type detected.

Customization
You can customize the following aspects of the project:

Vehicle Classes: Modify the vehicle_classes list in the script to include the indices of the vehicle types you want to detect.
Model: Use a different YOLOv7 model by changing the path in the script.
Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License. See the LICENSE file for details.
