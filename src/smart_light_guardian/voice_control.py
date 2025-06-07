import threading
import speech_recognition as sr


class VoiceControl(threading.Thread):
    """Threaded voice command listener."""

    def __init__(self, callback):
        super().__init__(daemon=True)
        self.callback = callback
        self.running = True

    def run(self):
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        while self.running:
            with mic as source:
                print("Say a command (lights on/off/status)...")
                audio = recognizer.listen(source, phrase_time_limit=3)
            try:
                text = recognizer.recognize_google(audio).lower()
                print(f"Heard: {text}")
            except sr.UnknownValueError:
                print("Could not understand. Please repeat.")
                continue
            except sr.RequestError:
                print("Speech recognition service unavailable.")
                continue

            if "lights on" in text:
                self.callback("on", "voice command")
            elif "lights off" in text:
                self.callback("off", "voice command")
            elif "light status" in text or "lights status" in text:
                self.callback("status", "voice command")

    def stop(self):
        self.running = False
