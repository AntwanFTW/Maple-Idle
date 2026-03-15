# ===============================
# macOS Retina Scaling Fix
# ===============================
import os
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"

import pyautogui
import time
import cv2

# -------------------------------
# Image Paths (SAFE on macOS)
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ENTER_IMG  = os.path.join(BASE_DIR, "enter.png")
ACCEPT_IMG = os.path.join(BASE_DIR, "accept.png")
LEAVE_IMG  = os.path.join(BASE_DIR, "leave.png")
MAPLE_IMG  = os.path.join(BASE_DIR, "maple.png")

# -------------------------------
# Configuration
# -------------------------------
CONFIDENCE = 0.78
USE_GRAYSCALE = True

ENTER_KEY  = "5"
ACCEPT_KEY = "6"
LEAVE_KEY  = "7"
MAPLE_KEY  = "8"

ENTER_COOLDOWN  = 2
ACCEPT_COOLDOWN = 2
LEAVE_COOLDOWN  = 2
MAPLE_COOLDOWN  = 2

ENTER_REGION  = None
ACCEPT_REGION = None
LEAVE_REGION  = None
MAPLE_REGION  = None

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = False

last_enter  = 0
last_accept = 0
last_leave  = 0
last_maple  = 0

# -------------------------------
# Initialization
# -------------------------------
print("PQ Bot running:")
print("5 = Enter | 6 = Accept | 7 = Leave | 8 = Maple")
time.sleep(2)  # focus BlueStacks

# -------------------------------
# Main Loop
# -------------------------------
while True:
    now = time.time()

    # ===============================
    # ENTER → 5
    # ===============================
    try:
        enter_btn = pyautogui.locateOnScreen(
            ENTER_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=ENTER_REGION
        )
        if enter_btn and now - last_enter > ENTER_COOLDOWN:
            print("Enter detected → 5")
            pyautogui.press(ENTER_KEY)
            last_enter = now
            time.sleep(0.3)
            continue
    except Exception as e:
        print("Enter error:", e)

    # ===============================
    #  ACCEPT → 6
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
            pyautogui.press(LEAVE_KEY)
            last_leave = now
            time.sleep(0.3)
            continue
    except Exception as e:
        print("Leave error:", e)

    # ===============================
    #  MAPLE → 8
    # ===============================
    try:
        maple_btn = pyautogui.locateOnScreen(
            MAPLE_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=MAPLE_REGION
        )
        if maple_btn and now - last_maple > MAPLE_COOLDOWN:
            print("Maple detected → 8")
            pyautogui.press(MAPLE_KEY)
            last_maple = now
    except Exception as e:
        print("Maple error:", e)

    time.sleep(0.2)
