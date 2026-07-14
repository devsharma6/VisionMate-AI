from ultralytics import YOLO
import cv2

# Load YOLOv8 Nano model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not found!")
    exit()

while True:
    success, frame = cap.read()

    if not success:
        break

    # Run object detection
    results = model(frame)

    # Draw detected objects
    annotated_frame = results[0].plot()

    cv2.imshow("VisionMate AI - Object Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()