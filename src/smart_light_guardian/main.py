import time
from threading import Event

from .clap_detection import ClapDetector
from .light_manager import LightManager
from .logger import Logger
from .voice_control import VoiceControl


def main() -> None:
    logger = Logger()
    manager = LightManager(logger)
    stop_event = Event()

    def handle_command(action: str, source: str):
        if action == "on":
            manager.turn_on(method=source)
        elif action == "off":
            manager.turn_off(method=source)
        elif action == "toggle":
            manager.toggle(method=source)
        elif action == "status":
            manager.status()

    voice = VoiceControl(handle_command)
    clap = ClapDetector(handle_command)
    voice.start()
    clap.start()

    print("Smart Light Guardian started. Press Ctrl+C to exit.")
    try:
        while not stop_event.is_set():
            time.sleep(2)
            manager.check_inactivity()
    except KeyboardInterrupt:
        pass
    finally:
        voice.stop()
        clap.stop()
        voice.join(timeout=1)
        clap.join(timeout=1)
        summary = manager.summary()
        print("--- Session Summary ---")
        print(f"Toggle count: {summary['toggles']}")
        print(f"Total time on: {summary['on_time']}")
        print(f"Automatic shutoffs: {summary['auto_offs']}")


if __name__ == "__main__":
    main()
