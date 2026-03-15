# Updated to use cpu which makes
# it less intensive on Mac
#


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
from pyautogui import ImageNotFoundException

# python3 -m pip install pyautogui
# python3 -m pip install opencv-python


# -------------------------------
# Focus BlueStacks (macOS)
# -------------------------------
last_focus = 0
FOCUS_COOLDOWN = 1.5

def focus_bluestacks(window_name="BlueStacks Air Chobiwan"):
    global last_focus
    now = time.time()

    if now - last_focus < FOCUS_COOLDOWN:
        return

    script = f'''
    tell application "System Events"
        tell process "BlueStacks"
            set frontmost to true
            click (first window whose name contains "{window_name}")
        end tell
    end tell
    '''

    subprocess.run(["osascript", "-e", script], check=False)

    last_focus = now
    time.sleep(0.2)

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

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = False

last_automatch = 0
last_accept    = 0
last_leave     = 0

# -------------------------------
# Startup
# -------------------------------
print("Automatch Bot running")
print("9 = Automatch | 6 = Accept | 7 = Leave")
print("Stop with Ctrl + C")
time.sleep(2)

# -------------------------------
# Main Loop (CPU optimized)
# -------------------------------
while True:
    now = time.time()
    action_taken = False

    # ===============================
    # PRIORITY 1: ACCEPT
    # ===============================
    if now - last_accept > ACCEPT_COOLDOWN:
        try:
            accept_btn = pyautogui.locateOnScreen(
                ACCEPT_IMG,
                confidence=CONFIDENCE,
                grayscale=USE_GRAYSCALE
            )
        except ImageNotFoundException:
            accept_btn = None

        if accept_btn:
            print("Accept detected → 6")
            focus_bluestacks()
            pyautogui.press(ACCEPT_KEY)
            last_accept = now
            action_taken = True

    # ===============================
    # PRIORITY 2: AUTOMATCH
    # ===============================
    if not action_taken and now - last_automatch > AUTOMATCH_COOLDOWN:
        try:
            auto_btn = pyautogui.locateOnScreen(
                AUTOMATCH_IMG,
                confidence=CONFIDENCE,
                grayscale=USE_GRAYSCALE
            )
        except ImageNotFoundException:
            auto_btn = None

        if auto_btn:
            print("Automatch detected → 9")
            focus_bluestacks()
            pyautogui.press(AUTOMATCH_KEY)
            last_automatch = now
            action_taken = True

    # ===============================
    # PRIORITY 3: LEAVE
    # ===============================
    if not action_taken and now - last_leave > LEAVE_COOLDOWN:
        try:
            leave_btn = pyautogui.locateOnScreen(
                LEAVE_IMG,
                confidence=CONFIDENCE,
                grayscale=USE_GRAYSCALE
            )
        except ImageNotFoundException:
            leave_btn = None

        if leave_btn:
            print("Leave detected → 7")
            focus_bluestacks()
            pyautogui.press(LEAVE_KEY)
            last_leave = now
            action_taken = True

    # -------------------------------
    # CPU-friendly sleep
    # -------------------------------
    if action_taken:
        time.sleep(0.35)
    else:
        time.sleep(0.7)
