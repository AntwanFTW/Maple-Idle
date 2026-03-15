# ===============================
# macOS Retina Scaling Fix
# ===============================
import os
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"

import pyautogui
import time
import cv2  # OpenCV backend for PyAutoGUI

# -------------------------------
# Configuration
# -------------------------------
AUTO_MATCH_IMG = "auto_match.png"
ACCEPT_IMG = "accept.png"
OK_IMG = "ok.png"

print("Working dire:", os.getcwd())
print("Files:", os.listdir())

CONFIDENCE = 0.61 # slightly lowerç7 for macOS / BlueStacks

AUTO_MATCH_KEY = "8"
ACCEPT_KEY = "5"
OK_KEY = "7"

AUTO_MATCH_COOLDOWN = 3  # seconds
ACCEPT_COOLDOWN = 3
OK_COOLDOWN = 2

# Optional screen regions (None = full screen)
AUTO_MATCH_REGION = None
ACCEPT_REGION = None
OK_REGION = None

USE_GRAYSCALE = True  # ignores color differences

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = False  # recommended on macOS

last_auto_match = 0
last_accept = 0
last_ok = 0

# Mac Purpose - force PyAutoGUI to use native resolution

pyautogui.FAILSAFE = False 

# -------------------------------
# Initialization
# -------------------------------
print("PQ 1.1 Bot running (macOS Retina-safe):")
print("Auto Match = 8 | Accept = 5 | OK = 7")
time.sleep(2)  # time to focus BlueStacks

# -------------------------------
# Main Loop
# -------------------------------
while True:
    now = time.time()

    # ===============================
    # 1️⃣ Auto Match (HIGHEST PRIORITY)
    # ===============================
    try:
        auto_match = pyautogui.locateOnScreen(
            AUTO_MATCH_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=AUTO_MATCH_REGION
        )
        if auto_match and now - last_auto_match > AUTO_MATCH_COOLDOWN:
            print("Auto Match detected → 8")
            pyautogui.keyDown(AUTO_MATCH_KEY)
            pyautogui.keyUp(AUTO_MATCH_KEY)
            last_auto_match = now
            time.sleep(0.3)
            continue
    except Exception as e:
        print("Auto Match error:", e)

    # ===============================
    # 2️⃣ Accept (MEDIUM PRIORITY)
    # ===============================
    try:
        accept = pyautogui.locateOnScreen(
            ACCEPT_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=ACCEPT_REGION
        )
        if accept and now - last_accept > ACCEPT_COOLDOWN:
            print("Accept detected → 5")
            pyautogui.keyDown(ACCEPT_KEY)
            pyautogui.keyUp(ACCEPT_KEY)
            last_accept = now
            time.sleep(0.3)
            continue
    except Exception as e:
        print("Accept error:", e)

    # ===============================
    # 3️⃣ OK (LOWEST PRIORITY)
    # ===============================
    try:
        ok_button = pyautogui.locateOnScreen(
            OK_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=OK_REGION
        )
        if ok_button and now - last_ok > OK_COOLDOWN:
            print("OK detected → 7")
            pyautogui.keyDown(OK_KEY)
            pyautogui.keyUp(OK_KEY)
            last_ok = now
    except Exception as e:
        print("OK error:", e)

    time.sleep(0.2)

