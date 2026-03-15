import pyautogui
import time

IMAGE = "maple.png"
CONFIDENCE = 0.75   # Mac usually needs lower confidence

print("Watching for image... Press Ctrl+C to stop.")

while True:
    try:
        location = pyautogui.locateOnScreen(IMAGE, confidence=CONFIDENCE)
    except pyautogui.ImageNotFoundException:
        location = None

    if location:
        pyautogui.press('7')
        print("Image found → pressed 7")
        time.sleep(1)  # prevent spamming

    time.sleep(0.2)
