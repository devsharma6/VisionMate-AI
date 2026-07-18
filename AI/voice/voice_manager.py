import asyncio
import edge_tts
import os
import threading
from playsound import playsound


class VoiceManager:

    def __init__(self):
        self.last_message = ""
        self.is_speaking = False

    async def _generate_voice(self, text):
        communicate = edge_tts.Communicate(
            text=text,
            voice="en-US-GuyNeural"
        )

        await communicate.save("voice.mp3")

    def _speak_thread(self, message):

        self.is_speaking = True

        asyncio.run(self._generate_voice(message))

        playsound("voice.mp3")

        if os.path.exists("voice.mp3"):
            os.remove("voice.mp3")

        self.last_message = message
        self.is_speaking = False

    def speak(self, message):

        if self.is_speaking:
            return

        if message == self.last_message:
            return

        print("🔊", message)

        threading.Thread(
            target=self._speak_thread,
            args=(message,),
            daemon=True
        ).start()