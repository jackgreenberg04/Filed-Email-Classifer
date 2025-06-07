from datetime import datetime, timedelta


class LightManager:
    """Manage light state and auto-off timer."""

    def __init__(self, logger, auto_off_minutes=5):
        self.logger = logger
        self.auto_off = timedelta(minutes=auto_off_minutes)
        self.is_on = False
        self.last_on_time = None
        self.toggle_count = 0
        self.auto_off_count = 0
        self.total_on_time = timedelta(0)

    def turn_on(self, method="manual"):
        if not self.is_on:
            self.is_on = True
            self.last_on_time = datetime.now()
            self.toggle_count += 1
            print(f"Lights turned ON at {self.last_on_time:%H:%M:%S}")
            self.logger.log(f"Light turned ON via {method}")

    def turn_off(self, method="manual"):
        if self.is_on:
            now = datetime.now()
            self.is_on = False
            self.toggle_count += 1
            self.total_on_time += now - self.last_on_time
            self.last_on_time = None
            if method == "auto":
                self.auto_off_count += 1
                print("Inactivity detected — Lights turned OFF to conserve energy.")
                self.logger.log("Light turned OFF automatically due to inactivity")
            else:
                print(f"Lights turned OFF at {now:%H:%M:%S}")
                self.logger.log(f"Light turned OFF via {method}")

    def toggle(self, method="manual"):
        if self.is_on:
            self.turn_off(method)
        else:
            self.turn_on(method)

    def status(self, *_):
        state = "ON" if self.is_on else "OFF"
        print(f"Light status: {state}")

    def check_inactivity(self):
        if self.is_on and datetime.now() - self.last_on_time > self.auto_off:
            self.turn_off(method="auto")

    def summary(self):
        return {
            "toggles": self.toggle_count,
            "on_time": self.total_on_time,
            "auto_offs": self.auto_off_count,
        }
