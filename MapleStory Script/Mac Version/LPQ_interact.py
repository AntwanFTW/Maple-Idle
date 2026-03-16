

# ===============================
# macOS Retina Scaling Fix
# ===============================
import os
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
os.environ["QT_SCALE_FACTOR"] = "1"

import pyautogui
import time
import cv2
from pyautogui import ImageNotFoundException

# -------------------------------
# Key Inputs
# -------------------------------
AUTOMATCH_KEY = "9"
ACCEPT_KEY = "6"
LEAVE_KEY = "7"
INTERACT_KEY = "q"

# -------------------------------
# Image Paths
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AUTOMATCH_IMG = os.path.join(BASE_DIR, "automatch.png")
ACCEPT_IMG    = os.path.join(BASE_DIR, "accept.png")
LEAVE_IMG     = os.path.join(BASE_DIR, "leave.png")
INTERACT_IMG  = os.path.join(BASE_DIR, "interact.png")

# -------------------------------
# Configuration
# -------------------------------
CONFIDENCE = 0.75
USE_GRAYSCALE = True

AUTOMATCH_COOLDOWN = 2
ACCEPT_COOLDOWN    = 2
LEAVE_COOLDOWN     = 2
INTERACT_COOLDOWN  = 1

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = False

last_automatch = 0
last_accept    = 0
last_leave     = 0
last_interact  = 0

# -------------------------------
# Startup
# -------------------------------
print("Automatch Bot running")
print("9 = Automatch | 6 = Accept | 7 = Leave | Q = Interact")
print("Full screen scan enabled")
print("Stop with Ctrl + C")

time.sleep(2)

# -------------------------------
# Main Loop
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
            pyautogui.press(AUTOMATCH_KEY)
            last_automatch = now
            action_taken = True

    # ===============================
    # PRIORITY 3: INTERACT
    # ===============================
    if not action_taken and now - last_interact > INTERACT_COOLDOWN:
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
            pyautogui.press(INTERACT_KEY)
            last_interact = now
            action_taken = True

    # ===============================
    # PRIORITY 4: LEAVE
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
            pyautogui.press(LEAVE_KEY)
            last_leave = now
            action_taken = True

    # -------------------------------
    # CPU Friendly Sleep
    # -------------------------------
    if action_taken:
        time.sleep(0.35)
    else:
        time.sleep(0.7)












