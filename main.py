from AI.object_detection.camera import Camera
from AI.object_detection.detector import Detector
from AI.object_detection.direction import get_direction

import cv2

camera = Camera()
detector = Detector()

print("🚀 VisionMate AI Started Successfully!")

while True:

    success, frame = camera.read()

    if not success:
        print("❌ Failed to read frame")
        break

    results = detector.detect(frame)

    annotated_frame = results[0].plot()

    for box in results[0].boxes:

        cls = int(box.cls[0])
        object_name = detector.model.names[cls]

        x1, y1, x2, y2 = box.xyxy[0]

        center_x = (x1 + x2) / 2

        direction = get_direction(center_x, frame.shape[1])

        print(f"{object_name} --> {direction}")

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

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()