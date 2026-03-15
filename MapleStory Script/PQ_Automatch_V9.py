import pyautogui
import time
import os
import keyboard  # pip install keyboard

# -------------------------------
# Directory
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AUTO_MATCH_IMG = os.path.join(BASE_DIR, "auto_match.png")
ACCEPT_IMG = os.path.join(BASE_DIR, "accept.png")
OK_IMG = os.path.join(BASE_DIR, "ok.png")

# -------------------------------
# Configuration
# -------------------------------
CONFIDENCE = 0.7  # template matching confidence

AUTO_MATCH_KEY = "f8"
ACCEPT_KEY = "f9"
OK_KEY = "f7"

AUTO_MATCH_COOLDOWN = 3  # seconds
ACCEPT_COOLDOWN = 3
OK_COOLDOWN = 2

# Optional screen regions (None = full screen)
AUTO_MATCH_REGION = None
ACCEPT_REGION = None
OK_REGION = None

USE_GRAYSCALE = True  # ignores color differences

pyautogui.PAUSE = 0.1

last_auto_match = 0
last_accept = 0
last_ok = 0

# -------------------------------
# Initialization
# -------------------------------
print("PQ 1.1 Bot running:")
print("Auto Match = F8 | Accept = F9 | OK = F7")
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
            print("Auto Match detected → F8")
            keyboard.send(AUTO_MATCH_KEY)  # ← simulate real keypress
            last_auto_match = now
            time.sleep(0.3)
            continue  # skip Accept & OK
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
            print("Accept detected → F9")
            keyboard.send(ACCEPT_KEY)
            last_accept = now
            time.sleep(0.3)
            continue  # skip OK
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
            print("OK detected → F7")
            keyboard.send(OK_KEY)
            last_ok = now
    except Exception as e:
        print("OK error:", e)

    time.sleep(0.2)
