# People Counting System

This project is a **People Counting System** using **YOLOv8** object detection and **OpenCV**. The system detects people entering and exiting a defined area by tracking their movement across predefined entry and exit lines in the video feed. It uses a simple counter to maintain the current number of people within the area, incrementing or decrementing based on their direction of movement.

## Features
- **People Detection**: Detects people in real-time using YOLOv8.
- **Entry/Exit Tracking**: Tracks people’s entry and exit across specified lines.
- **People Counter**: Counts and displays the current number of people inside a designated area.
- **Real-time Visualization**: Displays annotated video feed with entry and exit lines and current count.

## Requirements

Install the required packages using the following command:
```bash
pip install opencv-python numpy ultralytics
```

## Getting Started

1. **Clone this repository**:
   ```bash
   git clone <repo_url>
   ```
   
2. **Run the Script**:
   ```bash
   python people_counter.py
   ```

3. **Customize Entry/Exit Lines**: Adjust the `entry_line_x` and `exit_line_x` variables in the code based on your camera setup to set the entry and exit boundaries.

## Code Overview

### Key Components

- **YOLO Model Loading**: Loads the YOLOv8 model (`yolov8n.pt`) to detect people in the video.
- **Video Feed**: Reads frames from a webcam or video file.
- **Entry and Exit Line Definition**: Sets the `entry_line_x` and `exit_line_x` positions to define the boundaries for entry and exit tracking.
- **Centroid Calculation**: Computes the centroid of each detected bounding box to determine position.
- **Entry/Exit Logic**: Checks if a person has crossed the entry or exit lines by comparing their previous and current centroids.
- **Display**: Annotates the video feed with bounding boxes, entry/exit lines, and current count of people inside the area.

### Functions

- **get_centroid(box)**: Computes the centroid of a bounding box.
- **Main Loop**:
  - Reads frames, runs YOLO inference, and extracts centroids of detected people.
  - Compares current and previous centroids to update the people counter based on line crossings.
  - Annotates and displays the frame with entry/exit lines and people count.

## Customization

- **Camera or Video Input**: Change `cv2.VideoCapture(0)` to `cv2.VideoCapture('<video_file_path>')` to use a video file instead of the webcam.
- **Entry/Exit Line Adjustment**: Modify `entry_line_x` and `exit_line_x` to suit different camera setups or scenarios.
- **Model Customization**: Load a different model checkpoint by changing `'yolov8n.pt'` in `YOLO('yolov8n.pt')`.

## Usage Instructions

1. Start the script.
2. Adjust the entry/exit lines if needed.
3. Monitor the live video feed for real-time people counting.
4. Press `q` to quit the application.

## Dependencies

- `cv2` (OpenCV) for video processing and visualization.
- `numpy` for array operations.
- `ultralytics` for YOLOv8 model support.
