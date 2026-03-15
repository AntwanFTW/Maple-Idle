import pyautogui
import time
import cv2  # OpenCV backend for PyAutoGUI

# -------------------------------
# Configuration
# -------------------------------
AUTO_MATCH_IMG = "auto_match.png"
ACCEPT_IMG = "accept.png"

CONFIDENCE = 0.85  # template matching confidence
AUTO_MATCH_KEY = "f8"
ACCEPT_KEY = "f9"

AUTO_MATCH_COOLDOWN = 3  # seconds
ACCEPT_COOLDOWN = 3

# Optional: define screen regions for faster and safer detection
# Example: (left, top, width, height)
# Replace with your BlueStacks window coordinates
# Add in Later. Too lazy
AUTO_MATCH_REGION = None
ACCEPT_REGION = None

USE_GRAYSCALE = True  # ignores color differences

pyautogui.PAUSE = 0.1
last_auto_match = 0
last_accept = 0

# -------------------------------
# Initialization
# -------------------------------
print("PQ 1.0 Bot running: Auto Match = F8, Accept = F9")
time.sleep(2)  # time to focus BlueStacks

# -------------------------------
# Main Loop
# -------------------------------
while True:
    now = time.time()

    # --- Auto Match detection ---
    try:
        auto_match = pyautogui.locateOnScreen(
            AUTO_MATCH_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=AUTO_MATCH_REGION
        )
        if auto_match and now - last_auto_match > AUTO_MATCH_COOLDOWN:
            print("Auto Match detected → F8")
            pyautogui.press(AUTO_MATCH_KEY)
            last_auto_match = now
    except Exception as e:
        print("Unexpected error locating auto_match.png:", e)

    # --- Accept detection ---
    try:
        accept = pyautogui.locateOnScreen(
            ACCEPT_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=ACCEPT_REGION
        )
        if accept and now - last_accept > ACCEPT_COOLDOWN:
            print("Accept detected → F9")
            pyautogui.press(ACCEPT_KEY)
            last_accept = now
    except Exception as e:
        print("Unexpected error locating accept.png:", e)

    # Slight delay to reduce CPU usage
    time.sleep(0.2)
