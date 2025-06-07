# Smart Light Guardian

Smart Light Guardian is a simulation of a voice and sound controlled light system. It demonstrates how accessibility and sustainability can be combined in a simple Python application.

## Features
- **Voice commands** using `speech_recognition` to switch lights on or off.
- **Clap detection** with `sounddevice` for hands‑free control.
- **Auto‑off timer** that turns off the light after five minutes of inactivity.
- **Activity logging** to `log.txt` and a session summary on exit.

## Setup
1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python -m smart_light_guardian.main
   ```

A microphone is required for both voice commands and clap detection.

## Usage
- Say "lights on" or clap loudly to turn on the light.
- Say "lights off" or clap again to turn it off.
- Say "light status" to hear the current state.
- If no commands are detected for five minutes, the system turns the light off automatically.
- When you exit with `Ctrl+C`, a session summary is printed.

All events are logged in `log.txt` for later analysis.
