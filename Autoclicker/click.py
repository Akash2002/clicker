import pyautogui
import keyboard
import time
import random

def keep_alive():
    WIDTH = pyautogui.size().width
    HEIGHT = pyautogui.size().height
    try:
        while True:
            
            x = random.randint(0, WIDTH)
            y = random.randint(300, HEIGHT - 50)
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.click()
            
            # Wait for 2 minutes
            time.sleep(5)

    except KeyboardInterrupt:
        print("Script interrupted manually.")

if __name__ == "__main__":
    print("Press Ctrl+Shift+S to stop the script.")
    keep_alive()
