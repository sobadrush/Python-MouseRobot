# -*- coding: UTF-8 -*-

from math import cos, pi, sin, radians
import pyautogui
import time

def calcDescartesPosXY(radius, deg):
    deg = radians(deg)
    posX = 3 * radius * (cos(deg) - 0.5 * cos(2 * deg))
    posY = 3 * radius * (sin(deg) - 0.5 * sin(2 * deg))
    return { "X": posX, "Y": posY }

if __name__ == '__main__':

    ww = pyautogui.size().width
    hh = pyautogui.size().height

    # 將游標置中
    pyautogui.moveTo(x=ww/2, y=hh/2, duration=0)

    # while True:
    #     pyautogui.moveTo(x=122, y=224, duration=1.2)
    while True:
        for deg in range(0, 360, 1):
            pos = calcDescartesPosXY(100, deg)
            print(pos["X"] + ww/2, pos["Y"] + hh/2)
            pyautogui.moveTo(x=pos["X"]+ww/2, y=pos["Y"]+hh/2, duration=0)
        
     

