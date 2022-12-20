import pyautogui
import time

pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')
while True:
    
    pyautogui.press('b')
    time.sleep(2)
    pyautogui.press('b')
    time.sleep(2)
    pyautogui.press('c')
    time.sleep(2)
    pyautogui.press('backspace')
    time.sleep(2)
    pyautogui.press('backspace')
    time.sleep(2)
    pyautogui.press('backspace')
    time.sleep(2)
    
