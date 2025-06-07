from datetime import datetime


class Logger:
    """Simple file logger for light actions."""

    def __init__(self, path="log.txt"):
        self.path = path

    def log(self, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(f"{timestamp}: {message}\n")
