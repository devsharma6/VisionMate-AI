import cv2

class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(0)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        if not self.cap.isOpened():
            raise Exception("Camera not found!")

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()