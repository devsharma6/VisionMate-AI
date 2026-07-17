import asyncio
import edge_tts
import os
from playsound import playsound


class VoiceManager:

    def __init__(self):
        self.last_message = ""

    async def _generate_voice(self, text):
        communicate = edge_tts.Communicate(
            text=text,
            voice="en-US-GuyNeural"
        )

        await communicate.save("voice.mp3")

    def speak(self, message):

        if message == self.last_message:
            return

        print("🔊", message)

        asyncio.run(self._generate_voice(message))

        playsound("voice.mp3")

        self.last_message = message

        if os.path.exists("voice.mp3"):
            os.remove("voice.mp3")