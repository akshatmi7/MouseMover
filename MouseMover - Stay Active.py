import pyautogui
import time

while True:
    pyautogui.moveRel(100, 0, duration=0.5)  # Move right
    pyautogui.moveRel(-100, 0, duration=0.5) # Move left
    time.sleep(5)  # Wait for 30 seconds
