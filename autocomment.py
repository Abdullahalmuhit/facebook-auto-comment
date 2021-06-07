import pyautogui
import time

comments=["hello", "hi", "How Are You"]
time.sleep(5)
for i in range(10):
    pyautogui.typewrite(comments[i%10])
    pyautogui.typewrite("\n")
    time.sleep(2)