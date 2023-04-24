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
import globalvar as gl

"""
建立Button
"""
def create_button(txt='default'):
    btn = tk.Button(window, text=txt, bg='gray', fg='white', font=('Arial', 13))
    btn['width'] = 10
    btn['height'] = 5
    btn['font'] = tkFont.Font(family='Arial', size=20, weight='bold')

    # 按鈕被按下的背景顏色
    btn['activebackground'] = 'darkgray'

    # 按鈕被按下的文字顏色 ( 前景 )
    btn['activeforeground'] = 'yellow'

    # btn.grid(column=_column, row=_row)
    btn.pack(side="left", padx=10, pady=10)
    return btn

"""
綁定的事件
"""
def doClickEvent(event):
    if btnExec.cget("text") == "執行":
        _text = "暫停"
        th1.resume()
        th2.resume()
    else:
        _text = "執行"
        th1.pause()
        th2.pause()
    print(_text)
    btnExec.configure(bg="lightBlue", fg="red", text=_text)

"""
停止Thread
"""
def stopThread(event):
    print("======= stopThread ======")
    th1.pause()
    th1.stop()
    th2.pause()
    th2.stop()
    os._exit(status=0) # 0: 無錯誤退出 ; 1: 有錯誤退出

"""
增加元素進ListBox
"""
def addItemToListBox():
    # myListbox.insert(tk.END, 'apple')
    # myListbox.insert(tk.END, 'banana')
    # myListbox.insert(tk.END, 'orange')
    # myListbox.insert(tk.END, 'lemon')
    # myListbox.insert(tk.END, 'tomato')
    while True:
        if gl.get_value('RunFlag') == True:
            myListbox.insert(0, gl.get_value("POS_XY"))
            time.sleep(0.05)
            
            if myListbox.size() > 10:
                myListbox.delete(10)
                # print(f'確認 size = {myListbox.size()}')
                
        

if __name__ == '__main__':
    
    window = tk.Tk()
    window.title('派對孔明(つ´ω`)つ')
    window .geometry(f'380x200') # width x height
    window.eval('tk::PlaceWindow . center')
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", lambda : os._exit(status=0)) # 偵測視窗關閉

    # closebutton = create_button("關閉", 1, 2)
    # closebutton.bind('<Button-1>', stopThread) # 綁定滑鼠click事件, Button-1 → 左鍵

    btnExec = create_button('執行')
    btnExec.focus_force()
    # btnExec['command'] = doClickEvent # 綁定滑鼠click事件
    btnExec.bind('<space>', doClickEvent) # 綁定空白鍵事件

    # 建立一個子執行緒: 根據心臟線點資料移動
    th1 = Job()
    th1.setExecFunc(moveMouseHeart) # 設定要給JOB執行的function
    th1.start()

    # 建立 ListBox
    scrollbar = tk.Scrollbar(window) # ref. 捲軸：https://www.geeksforgeeks.org/scrollable-listbox-in-python-tkinter/
    scrollbar.pack(side = "right", fill = 'both')
    
    myListbox = tk.Listbox(borderwidth=2, height=15, selectmode="multiple")
    myListbox.pack(side="right", padx=10, pady=10)
    myListbox.config(yscrollcommand= scrollbar.set)
    scrollbar.config(command = myListbox.yview)


    # 建立一個子執行緒: 將點資料加入listbox
    th2 = Job()
    th2.setExecFunc(addItemToListBox) # 設定要給JOB執行的function
    th2.start()

    window.mainloop()