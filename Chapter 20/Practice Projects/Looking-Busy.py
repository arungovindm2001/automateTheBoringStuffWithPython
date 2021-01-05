import pyautogui
import time
import random

while True:
    random.random()
    a = pyautogui.position()
    randomX=a.x+random.random()
    randomY=a.y+random.random()
    pyautogui.moveTo(randomX,randomY)
    print('Position at ('+str(randomX),str(randomY)+')')
    time.sleep(10)
