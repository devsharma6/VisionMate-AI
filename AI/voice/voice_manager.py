import asyncio
import edge_tts
import threading
import queue
import os
from playsound import playsound


class VoiceManager:

    def __init__(self):

        self.queue = queue.Queue()
        self.last_message = ""

        worker = threading.Thread(
            target=self._worker,
            daemon=True
        )
        worker.start()

    async def _generate_voice(self, text):

        communicate = edge_tts.Communicate(
            text=text,
            voice="en-US-GuyNeural"
        )

        await communicate.save("voice.mp3")

    def _worker(self):

        while True:

            message = self.queue.get()

            try:

                asyncio.run(
                    self._generate_voice(message)
                )

                playsound("voice.mp3")

                if os.path.exists("voice.mp3"):
                    os.remove("voice.mp3")

                self.last_message = message

            except Exception as e:
                print("Voice Error:", e)

            self.queue.task_done()

    def speak(self, message):

        if not message:
            return

        if message == self.last_message:
            return

        if self.queue.empty():
            self.queue.put(message)