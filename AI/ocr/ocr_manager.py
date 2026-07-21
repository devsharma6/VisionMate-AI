import time
import threading
import cv2

from AI.ocr.text_reader import read_text


class OCRManager:

    def __init__(self):

        self.frame = None
        self.texts = []
        self.running = True

        threading.Thread(
            target=self._worker,
            daemon=True
        ).start()

    def update_frame(self, frame):

        self.frame = frame.copy()

    def _worker(self):

        while self.running:

            if self.frame is None:
                continue

            # Smaller image = Faster OCR
            small = cv2.resize(
                self.frame,
                (640, 360)
            )

            try:
                self.texts = read_text(small)

            except Exception:
                pass
        time.sleep(0.5)
    def get_text(self):

        return self.texts