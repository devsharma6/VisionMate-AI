from ultralytics import YOLO
import cv2
import sys
import os

from AI.object_detection.direction import get_direction

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from AI.voice.voice_manager import VoiceManager

# Initialize Voice Manager
voice_manager = VoiceManager()

# Load YOLOv8 Nano Model
model_path = os.path.join(os.path.dirname(__file__), "../../yolov8n.pt")
model = YOLO(model_path)

# Open Webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not found!")
    exit()

while True:

    success, frame = cap.read()

    if not success:
        break

    # Run YOLO
    results = model(frame)

    # Draw Detection Boxes
    annotated_frame = results[0].plot()

    # Process Every Detected Object
    for box in results[0].boxes:

        cls = int(box.cls[0])
        object_name = model.names[cls]

        x1, y1, x2, y2 = box.xyxy[0]

        center_x = (x1 + x2) / 2

        direction = get_direction(center_x, frame.shape[1])
        voice_manager.speak(f"{object_name} on your {direction}")

        print(f"{object_name} --> {direction}")

        # Display Direction on Screen
        cv2.putText(
            annotated_frame,
            direction,
            (int(x1), int(y1) - 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("VisionMate AI", annotated_frame)

    # Press Q to Quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()