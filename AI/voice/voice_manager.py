import pyttsx3
import time

class VoiceManager:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)

        self.last_message = ""
        self.last_time = 0
        self.cooldown = 3

    def speak(self, message):

        current_time = time.time()

        # Same message ko repeat mat karo
        if message == self.last_message:
            return

        # Cooldown check
        if current_time - self.last_time < self.cooldown:
            return

        print("🔊", message)

        self.engine.say(message)
        self.engine.runAndWait()

        self.last_message = message
        self.last_time = current_time