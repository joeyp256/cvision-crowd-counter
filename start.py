import cv2
import numpy as np
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Open the video file or webcam
cap = cv2.VideoCapture(0)  # Use 0 for webcam, or provide a video file path

# Initialize counter
people_inside = 0


# Define entry/exit lines (adjust these values based on your camera setup)
entry_line_x = 200  # Adjust this value based on your frame width
exit_line_x = 400   # Adjust this value based on your frame width
  

def get_centroid(box):
    x1, y1, x2, y2 = box
    return ((x1 + x2) / 2, (y1 + y2) / 2)

# Keep track of centroids in the previous frame
prev_centroids = []

while True:
    # Read a frame from the video
    success, frame = cap.read()
    if not success:
        break
    
    # Run YOLOv8 inference on the frame, only detecting people (class 0)
    results = model(frame, classes=[0])
    
    # Get centroids of detected people in the current frame
    current_centroids = []
    for r in results:
        boxes = r.boxes.xyxy.cpu().numpy()
        for box in boxes:
            current_centroids.append(get_centroid(box))
    
    # Check for entries and exits
    for cent in current_centroids:
        x, _ = cent
        if entry_line_x <= x < exit_line_x:
            # Check if this centroid was to the left of entry_line in the previous frame
            was_outside = any(prev_x < entry_line_x for prev_x, _ in prev_centroids)
            if was_outside:
                people_inside += 1
            was_inside = any(prev_x >= exit_line_x for prev_x, _ in prev_centroids)
            if was_inside:
                people_inside = max(0, people_inside - 1)
    
    # Update previous centroids
    prev_centroids = current_centroids
    
    # Visualize the results on the frame
    annotated_frame = results[0].plot()
    
    # Draw entry and exit lines
    cv2.line(annotated_frame, (entry_line_x, 0), (entry_line_x, frame.shape[0]), (0, 255, 0), 2)
    cv2.line(annotated_frame, (exit_line_x, 0), (exit_line_x, frame.shape[0]), (0, 0, 255), 2)
    
    # Display the count on the frame
    cv2.putText(annotated_frame, f"People inside: {people_inside}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the annotated frame
    cv2.imshow("People Counter", annotated_frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()