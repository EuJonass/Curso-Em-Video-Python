import pyautogui
import time

while True:
    time.sleep(1)
    pyautogui.press("win")
    time.sleep(2)
    pyautogui.write("chrome")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.doubleClick(x=630, y=436)
    pyautogui.write("youtube.com")
    pyautogui.press("enter")
