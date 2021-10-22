from pyautogui import *
import pyautogui
import time
import random
import keyboard
import win32api, win32com

while 1:
    if pyautogui.locateOnScreen('follow.png', region=(1150,290,270,700)) != None:
        print(pyautogui.locateOnScreen('follow.png'))
        print("Find It")
        time.sleep(0.1)
    else:
        print("NT")
        time.sleep(0.1)