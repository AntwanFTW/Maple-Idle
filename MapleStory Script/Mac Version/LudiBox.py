# ===============================
# macOS Retina Scaling Fix
# ===============================
import os
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"

import pyautogui
import time
import subprocess
from pyautogui import ImageNotFoundException

# -------------------------------
# Focus BlueStacks (macOS)
# -------------------------------
last_focus = 0
FOCUS_COOLDOWN = 1.5

def focus_bluestacks():
    global last_focus
    now = time.time()

    if now - last_focus < FOCUS_COOLDOWN:
        return

    subprocess.run(
        ["osascript", "-e", 'tell application "BlueStacks" to activate'],
        check=False
    )
    last_focus = now
    time.sleep(0.15)

# -------------------------------
# Image Path
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INTERACT_IMG = os.path.join(BASE_DIR, "interact.png")

# -------------------------------
# Configuration
# -------------------------------
CONFIDENCE = 0.82
USE_GRAYSCALE = True

INTERACT_KEY = "q"
INTERACT_COOLDOWN = 0.25

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = False

last_interact = 0

# -------------------------------
# Startup
# -------------------------------
print("Interact Bot running")
print("Presses Q when interact.png is detected")
print("Stop with Ctrl + C")
time.sleep(2)

# -------------------------------
# Main Loop
# -------------------------------
while True:
    now = time.time()

    if now - last_interact > INTERACT_COOLDOWN:
        try:
            interact_btn = pyautogui.locateOnScreen(
                INTERACT_IMG,
                confidence=CONFIDENCE,
                grayscale=USE_GRAYSCALE
            )
        except ImageNotFoundException:
            interact_btn = None

        if interact_btn:
            print("Interact detected → Q")
            focus_bluestacks()
            pyautogui.press(INTERACT_KEY)
            last_interact = now
            time.sleep(0.5)
            continue

    time.sleep(0.6)
