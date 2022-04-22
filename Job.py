# -*- coding: UTF-8 -*-

import threading
import time

# 自訂
import globalvar as gl
from MouseRobot import moveMouseHeart

"""
ref. https://www.itread01.com/content/1548038174.html
"""

class Job(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()     # 用於暫停執行緒的標識
        self.__flag.set()       # 設定為True
        self.__running = threading.Event()      # 用於停止執行緒的標識
        self.__running.set()      # 將running設定為True
        gl._init()

    def run(self):
        while self.__running.isSet():
            self.__flag.wait()      # 為True時立即返回, 為False時阻塞直到內部的標識位為True後返回
            # print(time.time())
            gl.set_value('RunFlag', False)
            self.execFunc() # ※ 執行傳遞進來的 function 參數
            # time.sleep(1)

    def pause(self):
        self.__flag.clear()     # 設定為False, 讓執行緒阻塞
        gl.set_value('RunFlag', False)

    def resume(self):
        self.__flag.set()    # 設定為True, 讓執行緒停止阻塞
        gl.set_value('RunFlag', True)

    def stop(self):
        gl.set_value('RunFlag', False)
        self.__flag.set()       # 將執行緒從暫停狀態恢復, 如何已經暫停的話
        self.__running.clear()        # 設定為False

    def setExecFunc(self, execFunc):  # 設定要執行的function reference
        self.execFunc = execFunc


if __name__ == '__main__':
    a = Job()
    a.setExecFunc(moveMouseHeart)
    a.start()
    time.sleep(2)
    a.pause()
    print("call pause")
    a.stop()
    # a.resume()
    # time.sleep(3)
    # a.pause()
    # time.sleep(2)
    # a.stop()
