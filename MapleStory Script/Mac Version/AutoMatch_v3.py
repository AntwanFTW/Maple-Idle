# Updated to focus bluestack #


# ===============================
# macOS Retina Scaling Fix
# ===============================
import os
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"

import pyautogui
import time
import cv2
import subprocess

# -------------------------------
# Focus BlueStacks (macOS)
# -------------------------------
def focus_bluestacks():
    try:
        subprocess.run(
            ["osascript", "-e", 'tell application "BlueStacks" to activate'],
            check=False
        )
        time.sleep(0.15)
    except Exception as e:
        print("Focus error:", e)

# -------------------------------
# Image Paths
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AUTOMATCH_IMG = os.path.join(BASE_DIR, "automatch.png")
ACCEPT_IMG    = os.path.join(BASE_DIR, "accept.png")
LEAVE_IMG     = os.path.join(BASE_DIR, "leave.png")

# -------------------------------
# Configuration
# -------------------------------
CONFIDENCE = 0.8
USE_GRAYSCALE = True

AUTOMATCH_KEY = "9"
ACCEPT_KEY    = "6"
LEAVE_KEY     = "7"

AUTOMATCH_COOLDOWN = 2
ACCEPT_COOLDOWN    = 2
LEAVE_COOLDOWN     = 2

AUTOMATCH_REGION = None
ACCEPT_REGION    = None
LEAVE_REGION     = None

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = False

last_automatch = 0
last_accept    = 0
last_leave     = 0

# -------------------------------
# Initialization
# -------------------------------
print("Automatch Bot running:")
print("9 = Automatch | 6 = Accept | 7 = Leave | 8 = Maple")
time.sleep(2)

# -------------------------------
# Main Loop
# -------------------------------
while True:
    now = time.time()

    # ===============================
    # AUTOMATCH → 9
    # ===============================
    try:
        auto_btn = pyautogui.locateOnScreen(
            AUTOMATCH_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=AUTOMATCH_REGION
        )
        if auto_btn and now - last_automatch > AUTOMATCH_COOLDOWN:
            print("Automatch detected → 9")
            focus_bluestacks()
            pyautogui.press(AUTOMATCH_KEY)
            last_automatch = now
            time.sleep(0.3)
            continue
    except Exception as e:
        print("Automatch error:", e)

    # ===============================
    # ACCEPT → 6
    # ===============================
    try:
        accept_btn = pyautogui.locateOnScreen(
            ACCEPT_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=ACCEPT_REGION
        )
        if accept_btn and now - last_accept > ACCEPT_COOLDOWN:
            print("Accept detected → 6")
            focus_bluestacks()
            pyautogui.press(ACCEPT_KEY)
            last_accept = now
            time.sleep(0.3)
            continue
    except Exception as e:
        print("Accept error:", e)

    # ===============================
    # LEAVE → 7
    # ===============================
    try:
        leave_btn = pyautogui.locateOnScreen(
            LEAVE_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=LEAVE_REGION
        )
        if leave_btn and now - last_leave > LEAVE_COOLDOWN:
            print("Leave detected → 7")
            focus_bluestacks()
            pyautogui.press(LEAVE_KEY)
            last_leave = now
            time.sleep(0.3)
            continue
    except Exception as e:
        print("Leave error:", e)

    time.sleep(0.2)
