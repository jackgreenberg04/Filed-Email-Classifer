import threading
import numpy as np
import sounddevice as sd


class ClapDetector(threading.Thread):
    """Detects loud sounds to toggle the light."""

    def __init__(self, callback, threshold=0.5, chunk_duration=0.2):
        super().__init__(daemon=True)
        self.callback = callback
        self.threshold = threshold
        self.chunk_duration = chunk_duration
        self.running = True

    def run(self):
        with sd.InputStream(callback=self._audio_callback):
            while self.running:
                sd.sleep(int(self.chunk_duration * 1000))

    def _audio_callback(self, indata, frames, time, status):
        volume = np.linalg.norm(indata)
        if volume > self.threshold:
            print("Clap detected!")
            self.callback("toggle", "clap")

    def stop(self):
        self.running = False
