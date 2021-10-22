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
i = 0
A = [.5,.65,.4,.6,.7,.4,.6,.65,.55,.35,.45]
while keyboard.is_pressed('q') == False:

    a = pyautogui.locateOnScreen('follow.png', region=(1150,290,270,700))

    if a != None:
        print(a[0],a[1])
        print('Follow Found!')
        print(i)
        print(A[i])
        click(a[0]+40,a[1]+30)
        time.sleep(A[i])
        i+=1
        if(i==10):
            i=0
    else:
        print('EveryOne Followed On Current Page')
        print(i)
        print(A[i])
        time.sleep(A[i])
        pyautogui.scroll(-10)
        i+=1
        if(i==10):
            i=0
        
