import os
import time
import pyautogui
import win32gui
import win32con
import win32api

# -------------------------------
# Directory / Images
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUTO_MATCH_IMG = os.path.join(BASE_DIR, "auto_match.png")
ACCEPT_IMG     = os.path.join(BASE_DIR, "accept.png")
OK_IMG         = os.path.join(BASE_DIR, "ok.png")

# -------------------------------
# Config
# -------------------------------
CONFIDENCE = 0.7
USE_GRAYSCALE = True

AUTO_MATCH_COOLDOWN = 3
ACCEPT_COOLDOWN     = 3
OK_COOLDOWN         = 2

AUTO_MATCH_REGION = None
ACCEPT_REGION     = None
OK_REGION         = None

pyautogui.PAUSE = 0.1

# Keys
AUTO_MATCH_KEY = win32con.VK_F8
ACCEPT_KEY     = win32con.VK_F9
OK_KEY         = win32con.VK_F7

last_auto_match = 0
last_accept     = 0
last_ok         = 0

# -------------------------------
# Find BlueStacks Window
# -------------------------------
def find_bluestacks_window():
    def enum_handler(hwnd, result):
        title = win32gui.GetWindowText(hwnd)
        if "BlueStacks" in title:
            result.append(hwnd)

    windows = []
    win32gui.EnumWindows(enum_handler, windows)
    return windows[0] if windows else None

bst_window = find_bluestacks_window()
if not bst_window:
    print("❌ Could not find BlueStacks window!")
    exit(1)

print("Found BlueStacks window:", bst_window)

# -------------------------------
# Send Key to BlueStacks
# -------------------------------
def send_key(hwnd, vk_code):
    # WM_KEYDOWN
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, vk_code, 0)
    time.sleep(0.05)
    # WM_KEYUP
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, vk_code, 0)

# -------------------------------
# Validate Images
# -------------------------------
missing = False
for p in [AUTO_MATCH_IMG, ACCEPT_IMG, OK_IMG]:
    if not os.path.isfile(p):
        print("❌ Missing image:", p)
        missing = True

if missing:
    print("Fix images and restart.")
    exit(1)

print("All images found.")
time.sleep(2)  # time to focus or start BlueStacks

# -------------------------------
# Main Loop
# -------------------------------
while True:
    now = time.time()

    # Auto Match
    try:
        am = pyautogui.locateOnScreen(
            AUTO_MATCH_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=AUTO_MATCH_REGION
        )
        if am and now - last_auto_match > AUTO_MATCH_COOLDOWN:
            print("Auto Match detected → F8")
            send_key(bst_window, AUTO_MATCH_KEY)
            last_auto_match = now
            time.sleep(0.3)
            continue
    except Exception as e:
        print("Auto Match error:", e)

    # Accept
    try:
        ac = pyautogui.locateOnScreen(
            ACCEPT_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=ACCEPT_REGION
        )
        if ac and now - last_accept > ACCEPT_COOLDOWN:
            print("Accept detected → F9")
            send_key(bst_window, ACCEPT_KEY)
            last_accept = now
            time.sleep(0.3)
            continue
    except Exception as e:
        print("Accept error:", e)

    # OK
    try:
        okb = pyautogui.locateOnScreen(
            OK_IMG,
            confidence=CONFIDENCE,
            grayscale=USE_GRAYSCALE,
            region=OK_REGION
        )
        if okb and now - last_ok > OK_COOLDOWN:
            print("OK detected → F7")
            send_key(bst_window, OK_KEY)
            last_ok = now
    except Exception as e:
        print("OK error:", e)

    time.sleep(0.2)
