
# Scipt to automate SOLO KPQ v1.1 in MapleStory using image recognition and keyboard simulation
# If images are not recognized properly, adjust CONFIDENCE value (.5-.85)
# May have to screen shot images of icons and replace it in the script folder.
# /Requires pyautogui and keyboard libraries: pip install pyautogui keyboard  
# Python 3.13.2 is being used for development
################################################################################################

# BEFORE you RUN: adjust the size of bluestack window, and then take screenshots of
# Enter, Accept, OK, and Leave buttons and replace the images in the script folder.

################################################################################################
import pyautogui
import time
import os
import keyboard  # pip install keyboard

# -------------------------------
# Directory
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ENTER_IMG  = os.path.join(BASE_DIR, "enter.png")   # Uses Enter instead of Auto Match
ACCEPT_IMG = os.path.join(BASE_DIR, "accept.png")
OK_IMG     = os.path.join(BASE_DIR, "ok.png")
LEAVE_IMG  = os.path.join(BASE_DIR, "leave.png")

# -------------------------------
# Configuration
# -------------------------------
CONFIDENCE = 0.75  # template matching confidence

ENTER_KEY  = "f6"
ACCEPT_KEY = "f9"
OK_KEY     = "f7"
LEAVE_KEY  = "f5"

ENTER_COOLDOWN  = 3
ACCEPT_COOLDOWN = 3
OK_COOLDOWN     = 2
LEAVE_COOLDOWN  = 3  # leave should be slower / safer

# Optional screen regions (None = full screen)
ENTER_REGION  = None
ACCEPT_REGION = None
OK_REGION     = None
LEAVE_REGION  = None

USE_GRAYSCALE = True  # ignores color differences

pyautogui.PAUSE = 0.1

last_ENTER  = 0
last_accept = 0
last_ok     = 0
last_leave  = 0

# -------------------------------
# Initialization
# -------------------------------
print("PQ 1.1 Bot running:")
print("Enter = F6 | Accept = F9 | OK = F7 | Leave = F5")
time.sleep(2)  # time to focus BlueStacks

# -------------------------------
# Main Loop
# -------------------------------
while True:
    now = time.time()

    # ===============================
    #  Enter (HIGHEST PRIORITY)
    # ===============================
    try:
        ENTER = pyautogui.locateOnScreen(
            ENTER_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=ENTER_REGION
        )
        if ENTER and now - last_ENTER > ENTER_COOLDOWN:
            print("Enter detected → F6")
            keyboard.send(ENTER_KEY)
            last_ENTER = now
            time.sleep(0.3)
            continue
    except Exception as e:
        print("Enter error:", e)

    # ===============================
    # Accept (MEDIUM PRIORITY)
    # ===============================
    try:
        accept = pyautogui.locateOnScreen(
            ACCEPT_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=ACCEPT_REGION
        )
        if accept and now - last_accept > ACCEPT_COOLDOWN:
            print("Accept detected → F9")
            keyboard.send(ACCEPT_KEY)
            last_accept = now
            time.sleep(0.3)
            continue
    except Exception as e:
        print("Accept error:", e)

    # ===============================
    # OK (LOW PRIORITY)
    # ===============================
    try:
        ok_button = pyautogui.locateOnScreen(
            OK_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=OK_REGION
        )
        if ok_button and now - last_ok > OK_COOLDOWN:
            print("OK detected → F7")
            keyboard.send(OK_KEY)
            last_ok = now
            time.sleep(0.3)
            continue
    except Exception as e:
        print("OK error:", e)

    # ===============================
    # Leave (LOWEST PRIORITY)
    # ===============================
    try:
        leave_button = pyautogui.locateOnScreen(
            LEAVE_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=LEAVE_REGION
        )
        if leave_button and now - last_leave > LEAVE_COOLDOWN:
            print("Leave detected → F5")
            keyboard.send(LEAVE_KEY)
            last_leave = now
    except Exception as e:
        print("Leave error:", e)

    time.sleep(0.2)
