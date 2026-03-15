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
# Image Paths
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INTERACT_IMG = os.path.join(BASE_DIR, "interact.png")
AUTOMATCH_IMG = os.path.join(BASE_DIR, "automatch.png")
ACCEPT_IMG    = os.path.join(BASE_DIR, "accept.png")
LEAVE_IMG     = os.path.join(BASE_DIR, "leave.png")
OK_IMG        = os.path.join(BASE_DIR, "ok.png")   # ✅ ADDED

# -------------------------------
# Configuration
# -------------------------------
CONFIDENCE = 0.82
USE_GRAYSCALE = True

INTERACT_KEY  = "q"
AUTOMATCH_KEY = "9"
ACCEPT_KEY    = "6"
LEAVE_KEY     = "7"
OK_KEY        = "0"     # ✅ ADDED

INTERACT_COOLDOWN  = 0.5
AUTOMATCH_COOLDOWN = 2
ACCEPT_COOLDOWN    = 2
LEAVE_COOLDOWN     = 2
OK_COOLDOWN        = 2  # ✅ ADDED

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = False

last_interact  = 0
last_automatch = 0
last_accept    = 0
last_leave     = 0
last_ok        = 0      # ✅ ADDED

# -------------------------------
# Startup
# -------------------------------
print("Automatch Bot running")
print("Q = Interact | 9 = Automatch | 6 = Accept | 7 = Leave | 0 = OK")
print("Stop with Ctrl + C")
time.sleep(2)

# -------------------------------
# Main Loop (CPU optimized)
# -------------------------------
while True:
    now = time.time()
    action_taken = False

    # ===============================
    # PRIORITY 0: INTERACT (FASTEST)
    # ===============================
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
            action_taken = True

    # ===============================
    # PRIORITY 1: ACCEPT
    # ===============================
    if not action_taken and now - last_accept > ACCEPT_COOLDOWN:
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

    # ===============================
    # PRIORITY 4: OK (LOWEST)
    # ===============================
    if not action_taken and now - last_ok > OK_COOLDOWN:
        try:
            ok_btn = pyautogui.locateOnScreen(
                OK_IMG,
                confidence=CONFIDENCE,
                grayscale=USE_GRAYSCALE
            )
        except ImageNotFoundException:
            ok_btn = None

        if ok_btn:
            print("OK detected → 0")
            focus_bluestacks()
            pyautogui.press(OK_KEY)
            last_ok = now
            action_taken = True

    # -------------------------------
    # CPU-friendly sleep
    # -------------------------------
    if action_taken:
        time.sleep(0.25)
    else:
        time.sleep(0.6)
