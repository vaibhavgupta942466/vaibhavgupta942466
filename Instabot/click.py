from pyautogui import *
import pyautogui
import time
import random
import win32api, win32con
import keyboard

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# color (0, 149, 246)
while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(1150,290,270,700))

    width, height = pic.size

    for x in range(0,width,5):
        for y in range (0,height,5):

            r,g,b = pic.getpixel((x,y))

            if b == 246:
                click(x+1150,y+290)
                time.sleep(1)
                break
