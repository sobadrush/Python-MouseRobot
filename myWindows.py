# -*- coding: UTF-8 -*-

import tkinter as tk
############################
from math import cos, sin, pi, radians
import pyautogui
import time
import threading

# 自訂
from MouseRobot import moveMouseHeart
from Job import Job

"""
建立Button
"""
def create_button(txt='default', _column=1, _row=1):
    btn = tk.Button(window, text=txt, bg='gray', fg='white', font=('Arial', 13))
    btn['width'] = 50
    btn['height'] = 5

    # 按鈕被按下的背景顏色
    btn['activebackground'] = 'darkgray'

    # 按鈕被按下的文字顏色 ( 前景 )
    btn['activeforeground'] = 'yellow'

    btn.grid(column=_column, row=_row)
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

if __name__ == '__main__':
    
    window = tk.Tk()
    window.eval('tk::PlaceWindow . center')
    window.resizable(False, False)
    window.title('派對孔明(つ´ω`)つ')

    closebutton = create_button("關閉", 1, 2)
    closebutton.bind('<Button-1>', stopThread) # 綁定滑鼠click事件, Button-1 → 左鍵

    btnExec = create_button('執行')
    btnExec.focus_force()
    # btnExec['command'] = doClickEvent # 綁定滑鼠click事件
    btnExec.bind('<space>', doClickEvent) # 綁定空白鍵事件

    # 建立一個子執行緒
    th1 = Job()
    th1.setExecFunc(moveMouseHeart) # 設定要給JOB執行的function
    th1.start()
    window.mainloop()