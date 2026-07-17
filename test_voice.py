import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty("rate", 150)

messages = [
    "Person on your left",
    "Person on your center",
    "Person on your right"
]

for msg in messages:
    print(msg)
    engine.stop()
    engine.say(msg)
    engine.runAndWait()
    time.sleep(2)