import pyautogui
import time
import cv2
import os
import sys

# ----------------------------------
# BASE DIRECTORY (SCRIPT LOCATION)
# ----------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AUTO_MATCH_IMG = os.path.join(BASE_DIR, "auto_match.png")
ACCEPT_IMG = os.path.join(BASE_DIR, "accept.png")
OK_IMG = os.path.join(BASE_DIR, "ok.png")

CONFIDENCE = 0.85

# ----------------------------------
# STARTUP CHECKS (FAIL FAST)
# ----------------------------------
print("PQ 1.1 Bot running:")
print("Auto Match = F8 | Accept = F9 | OK = F7")
print("Script directory:", BASE_DIR)

images = {
    "Auto Match": AUTO_MATCH_IMG,
    "Accept": ACCEPT_IMG,
    "OK": OK_IMG
}

for name, path in images.items():
    if not os.path.exists(path):
        print(f"❌ {name} image missing: {path}")
        sys.exit(1)

print("✅ All image files found\n")

# ----------------------------------
# HELPER FUNCTION
# ----------------------------------
def find_and_press(image_path, key_name):
    try:
        location = pyautogui.locateOnScreen(
            image_path,
            confidence=CONFIDENCE
        )

        if location:
            pyautogui.press(key_name)
            time.sleep(0.2)
            return True

    except Exception as e:
        print(f"{key_name} fatal error:", e)
        sys.exit(1)

    return False


# ----------------------------------
# MAIN LOOP
# ----------------------------------
while True:
    if find_and_press(AUTO_MATCH_IMG, "f8"):
        print("Auto Match pressed")
        time.sleep(1)

    if find_and_press(ACCEPT_IMG, "f9"):
        print("Accept pressed")
        time.sleep(1)

    if find_and_press(OK_IMG, "f7"):
        print("OK pressed")
        time.sleep(1)

    time.sleep(0.3)
