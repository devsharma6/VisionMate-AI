from AI.object_detection.camera import Camera
from AI.object_detection.detector import Detector

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

    cv2.imshow("VisionMate AI", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()