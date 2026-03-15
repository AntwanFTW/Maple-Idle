import pyautogui
import time
import os
import keyboard  # pip install keyboard

# -------------------------------
# Directory
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INTERACT_IMG = os.path.join(BASE_DIR, "interact.png")

# -------------------------------
# Configuration
# -------------------------------
CONFIDENCE = 0.8
INTERACT_KEY = "w"
INTERACT_COOLDOWN = 2  # seconds

INTERACT_REGION = None  # None = full screen
USE_GRAYSCALE = True

pyautogui.PAUSE = 0.1
last_interact = 0

# -------------------------------
# Initialization
# -------------------------------
print("Interact Bot running")
print("Interact → W")
time.sleep(2)  # time to focus game window

# -------------------------------
# Main Loop
# -------------------------------
while True:
    now = time.time()

    try:
        interact = pyautogui.locateOnScreen(
            INTERACT_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=INTERACT_REGION
        )

        if interact and now - last_interact > INTERACT_COOLDOWN:
            print("Interact detected → W")
            keyboard.send(INTERACT_KEY)
            last_interact = now
            time.sleep(0.2)

    except Exception as e:
        print("Interact error:", e)

    time.sleep(0.2)
