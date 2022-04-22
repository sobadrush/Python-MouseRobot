# -*- coding: UTF-8 -*-

from math import cos, pi, sin, radians
import pyautogui
import time

import globalvar as gl

"""
計算【笛卡兒心臟】線點資料
"""
def calcDescartesPosXY(radius, deg):
    deg = radians(deg)
    posX = 1 * radius * (1 * sin(deg) + 0.5 * sin(2 * deg))
    posY = 1 * radius * (1 * cos(deg) + 0.5 * cos(2 * deg))
    return {"X": posX, "Y": posY}

"""
計算【笛卡兒心臟】線點資料(0~360)
"""
def calcDescartesPoints():
    t = tuple()
    for deg in range(0, 360, 10): # step = 10
        posDict = calcDescartesPosXY(100, deg)
        t += (posDict,) # tuple只能加入tuple → 參考:建立只有一個元素的元組 tuple
    return t

"""
根據計算出的心臟線點資料進行移動滑鼠
"""
def moveMouseHeart():

    global _runFlag

    ww = pyautogui.size().width
    hh = pyautogui.size().height
    centralX = ww/2
    centralY = hh/2

    # 將游標置中
    pyautogui.moveTo(x=centralX, y=centralY, duration=0)

    # 計算一圈心臟線的點資料
    pointsTuple = calcDescartesPoints()

    i = 0
    while i < len(pointsTuple):
        if gl.get_value('RunFlag') == True:
            if i == len(pointsTuple) - 1:
                i = 0
            pos_X = pointsTuple[i].get("X") + centralX
            pos_Y = pointsTuple[i].get("Y") + centralY
            print(f'{{ {pos_X}, {pos_Y} }}')
            pyautogui.moveTo(x=pos_X, y=pos_Y, duration=0.01) # 移動滑鼠
            i += 1


if __name__ == '__main__':
    moveMouseHeart()

