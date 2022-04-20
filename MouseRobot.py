# -*- coding: UTF-8 -*-

from math import cos, pi, sin, radians
import pyautogui
import time

"""
計算【笛卡兒心臟】線點資料
"""
def calcDescartesPosXY(radius, deg):
    deg = radians(deg)
    posX = 1 * radius * (1 * sin(deg) + 0.5 * sin(2 * deg))
    posY = 1 * radius * (1 * cos(deg) + 0.5 * cos(2 * deg))
    return {"X": posX, "Y": posY}


if __name__ == '__main__':

    ww = pyautogui.size().width
    hh = pyautogui.size().height
    centralX = ww/2
    centralY = hh/2

    # 將游標置中
    pyautogui.moveTo(x=centralX, y=centralY, duration=0)

    while True:
        for deg in range(0, 360, step=12):
            pos = calcDescartesPosXY(100, deg)
            print(pos["X"] + centralX, pos["Y"] + centralY)
            pyautogui.moveTo(x=pos["X"]+centralX, y=pos["Y"]+centralY, duration=0) # 移動滑鼠
