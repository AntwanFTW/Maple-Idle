import os
import time
import pyautogui
import cv2  # required for confidence matching

# -------------------------------
# Directory Setup
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AUTO_MATCH_IMG = os.path.join(BASE_DIR, "auto_match.png")
ACCEPT_IMG = os.path.join(BASE_DIR, "accept.png")
OK_IMG = os.path.join(BASE_DIR, "ok.png")

# -------------------------------
# Configuration
# -------------------------------
CONFIDENCE = 0.75  # template matching confidence
USE_GRAYSCALE = True  # ignores color differences

AUTO_MATCH_COOLDOWN = 3  # seconds
ACCEPT_COOLDOWN = 3
OK_COOLDOWN = 2

AUTO_MATCH_REGION = None  # None = full screen
ACCEPT_REGION = None
OK_REGION = None

pyautogui.PAUSE = 0.1

# Track last activation times
last_auto_match = 0
last_accept = 0
last_ok = 0

# -------------------------------
# Initialization
# -------------------------------
print("PQ 1.2 Bot running:")
print("Auto Match = click | Accept = click | OK = click")
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
            x, y = pyautogui.center(auto_match)
            print(f"Auto Match detected → clicking at ({x},{y})")
            pyautogui.click(x, y)
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
            x, y = pyautogui.center(accept)
            print(f"Accept detected → clicking at ({x},{y})")
            pyautogui.click(x, y)
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
            x, y = pyautogui.center(ok_button)
            print(f"OK detected → clicking at ({x},{y})")
            pyautogui.click(x, y)
            last_ok = now
    except Exception as e:
        print("OK error:", e)

    time.sleep(0.2)
