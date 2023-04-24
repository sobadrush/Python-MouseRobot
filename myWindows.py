# -*- coding: UTF-8 -*-

import tkinter as tk
import tkinter.font as tkFont
############################
from math import cos, sin, pi, radians
import pyautogui
import time
import threading

import os, sys

# 自訂
from MouseRobot import moveMouseHeart
from Job import Job

"""
建立Button
"""
def create_button(txt='default'):
    btn = tk.Button(window, text=txt, bg='gray', fg='white', font=('Arial', 13))
    btn['width'] = 50
    btn['height'] = 5


    # 按鈕被按下的背景顏色
    btn['activebackground'] = 'darkgray'

    # 按鈕被按下的文字顏色 ( 前景 )
    btn['activeforeground'] = 'yellow'

    # btn.grid(column=_column, row=_row)
    btn.pack(side="top", padx=10, pady=30)
    return btn

"""
綁定的事件
"""
def doClickEvent(event):
    if btnExec.cget("text") == "執行":
        _text = "暫停"
        th1.resume()
    else:
        _text = "執行"
        th1.pause()
    print(_text)
    btnExec.configure(bg="lightBlue", fg="red", text=_text)

def stopThread(event):
    print("======= stopThread ======")
    th1.pause()
    th1.stop()
    os._exit(status=0) # 0: 無錯誤退出 ; 1: 有錯誤退出

if __name__ == '__main__':
    
    window = tk.Tk()
    window.title('派對孔明(つ´ω`)つ')
    window .geometry(f'300x200') # width x height
    window.eval('tk::PlaceWindow . center')
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", lambda : os._exit(status=0))

    # closebutton = create_button("關閉", 1, 2)
    # closebutton.bind('<Button-1>', stopThread) # 綁定滑鼠click事件, Button-1 → 左鍵

    btnExec = create_button('執行')
    btnExec.focus_force()
    # btnExec['command'] = doClickEvent # 綁定滑鼠click事件
    btnExec.bind('<space>', doClickEvent) # 綁定空白鍵事件

    # 建立一個子執行緒
    th1 = Job()
    th1.setExecFunc(moveMouseHeart) # 設定要給JOB執行的function
    th1.start()

    window.mainloop()