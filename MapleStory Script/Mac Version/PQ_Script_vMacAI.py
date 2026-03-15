# ===============================
# macOS Retina Scaling Fix
# ===============================
import os
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"

import pyautogui
import time
import cv2
import random

# -------------------------------7
# Configuration
# -------------------------------
AUTO_MATCH_IMG = "auto_match.png"
ACCEPT_IMG = "accept.png"
OK_IMG = "ok.png"

CONFIDENCE = 0.60
USE_GRAYSCALE = False

AUTO_MATCH_KEY = "8"
OK_KEY = "7"

AUTO_MATCH_COOLDOWN = 3
ACCEPT_COOLDOWN = 2
OK_COOLDOWN = 2

AUTO_MATCH_REGION = None
ACCEPT_REGION = None
OK_REGION = None

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = False

last_auto_match = 0
last_accept = 0
last_ok = 0

# -------------------------------
# Focus BlueStacks (Upper-Left Quadrant)
# -------------------------------
def focus_bluestacks():
    screen_w, screen_h = pyautogui.size()
    pyautogui.click(int(screen_w * 0.25), int(screen_h * 0.25))
    time.sleep(0.05)

# -------------------------------
# Initialization
# -------------------------------
print("PQ 1.1 Bot running (macOS Retina-safe)")
print("Auto Match = 8 | Accept = CLICK | OK = 7")
time.sleep(2)

# -------------------------------
# Main Loop
# -------------------------------
while True:
    now = time.time()

    # ===============================
    # 1️⃣ Auto Match (KEY)
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
            pyautogui.press(AUTO_MATCH_KEY)
            last_auto_match = now
            time.sleep(0.3)
            continue
    except Exception as e:
        print("Auto Match error:", e)

    # ===============================
    # 2️⃣ Accept (CLICK ONLY — FIXED)
    # ===============================
    try:
        accept = pyautogui.locateOnScreen(
            ACCEPT_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=ACCEPT_REGION
        )
        if accept and now - last_accept > ACCEPT_COOLDOWN:
            print("Accept detected → clicking button")

            focus_bluestacks()

            # 🎯 Click center with small random offset
            x, y = pyautogui.center(accept)
            x += random.randint(-5, 5)
            y += random.randint(-5, 5)

            pyautogui.click(x, y)

            last_accept = now
            time.sleep(0.3)
            continue
    except Exception as e:
        print("Accept error:", e)

    # ===============================
    # 3️⃣ OK (KEY)
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
            pyautogui.press(OK_KEY)
            last_ok = now
    except Exception as e:
        print("OK error:", e)

    time.sleep(0.2)
