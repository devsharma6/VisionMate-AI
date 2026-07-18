from AI.object_detection.distance import get_distance
from AI.object_detection.priority import get_priority
from AI.voice.voice_manager import VoiceManager
from AI.object_detection.camera import Camera
from AI.object_detection.detector import Detector
from AI.object_detection.direction import get_direction

import cv2

camera = Camera()
detector = Detector()
voice = VoiceManager()

print("🚀 VisionMate AI Started Successfully!")

while True:

    success, frame = camera.read()

    if not success:
        print("❌ Failed to read frame")
        break

    results = detector.detect(frame)

    annotated_frame = results[0].plot()

    for box in results[0].boxes:
        best_priority = -1
        best_message = None

        cls = int(box.cls[0])
        object_name = detector.model.names[cls]

        x1, y1, x2, y2 = box.xyxy[0]

        center_x = (x1 + x2) / 2

        direction = get_direction(center_x, frame.shape[1])
        area = (x2 - x1) * (y2 - y1)
        distance = get_distance(area)

        message = f"Warning. {object_name} {distance} on your {direction.lower()}"
        priority = get_priority(object_name)

        if priority > best_priority:
            best_priority = priority
            best_message = (
            f"Warning. {object_name.capitalize()} "
            f"{distance} on your {direction.lower()}"
            )
        print(f"Frame Width: {frame.shape[1]}")
        print(f"Center X: {center_x}")
        print(f"Direction: {direction}")
        print("-" * 30)
        if object_name == "person":
            message = f"Warning. Person on your {direction}"
            print("VOICE MESSAGE:", message)
            voice.speak(message)
        cv2.putText(
            annotated_frame,
            direction,
            (int(x1), int(y1) - 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )
    if best_message:
    # voice.speak(best_message)
        pass
    cv2.imshow("VisionMate AI", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()