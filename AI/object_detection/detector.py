from ultralytics import YOLO
import os

model_path = os.path.join(
    os.path.dirname(__file__),
    "../../models/yolov8n.pt"
)
)

class Detector:

    def __init__(self):
        self.model = YOLO(model_path)

    def detect(self, frame):
        return self.model(frame)