from AI.ocr.ocr_manager import OCRManager
from AI.ocr.text_reader import read_text
from AI.object_detection.obstacle import is_obstacle
from AI.object_detection.distance import get_distance
from AI.object_detection.priority import get_priority
from AI.voice.voice_manager import VoiceManager
from AI.object_detection.camera import Camera
from AI.object_detection.detector import Detector
from AI.object_detection.direction import get_direction

import cv2

# ==============================
# Initialize Modules
# ==============================

camera = Camera()
detector = Detector()
voice = VoiceManager()
ocr = OCRManager()
last_ocr_text = ""
print("🚀 VisionMate AI Started Successfully!")

frame_count = 0

# ==============================
# Main Loop
# ==============================

while True:

    success, frame = camera.read()
    ocr.update_frame(frame)
    if not success:
        print("❌ Failed to read frame")
        break


    # ==============================
    # Object Detection
    # ==============================

    results = detector.detect(frame)
    annotated_frame = results[0].plot()

    best_priority = -1
    best_message = None

    # ==============================
    # Process Detected Objects
    # ==============================

    for box in results[0].boxes:

        cls = int(box.cls[0])
        object_name = detector.model.names[cls]

        x1, y1, x2, y2 = box.xyxy[0]

        center_x = (x1 + x2) / 2

        direction = get_direction(center_x, frame.shape[1])

        area = (x2 - x1) * (y2 - y1)

        distance = get_distance(area)

        danger = is_obstacle(
            center_x,
            frame.shape[1],
            distance
        )

        priority = get_priority(object_name)

        # Keep only highest priority object
        if priority > best_priority:

            best_priority = priority

            if danger:
                best_message = (
                    f"Warning! {object_name.capitalize()} directly ahead."
                )
            else:
                best_message = (
                    f"Warning. {object_name.capitalize()} "
                    f"{distance} on your {direction.lower()}"
                )

        # Draw Direction
        cv2.putText(
            annotated_frame,
            direction,
            (int(x1), int(y1) - 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    # ==============================
    # Speak Only Once
    # ==============================

    if best_message:
        print(best_message)
        voice.speak(best_message)
    texts = ocr.get_text()

    if texts:
        print("📖 OCR:", texts)
    # ==============================
    # Draw Danger Zone
    # ==============================

    left = int(frame.shape[1] * 0.4)
    right = int(frame.shape[1] * 0.6)

    cv2.rectangle(
        annotated_frame,
        (left, 0),
        (right, frame.shape[0]),
        (0, 0, 255),
        2
    )

    # ==============================
    # Show Frame
    # ==============================
    texts = ocr.get_text()

    if texts:

        current_text = " ".join(texts)

        if current_text != last_ocr_text:

            print("📖 OCR:", current_text)

            voice.speak(current_text)

            last_ocr_text = current_text
    cv2.imshow("VisionMate AI", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ==============================
# Cleanup
# ==============================

camera.release()
cv2.destroyAllWindows()