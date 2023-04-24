# Python-MouseRobot
Python-滑鼠機器人-笛卡兒心臟線

# 建立mac虛擬環境
1. Mac可如此連結建立虛擬環境設定: (ref. https://stackoverflow.com/questions/49470367/install-virtualenv-and-virtualenvwrapper-on-macos)
2. 設定好虛擬環境後，Mac可使用 `mkvirtualenv venv01` 建立虛擬環境(會生成在 ~/.virtualenvs 中)
3. 可使用 `workon venv01` 進入虛擬環境，此時 `pip install` 的lib會生成在 ~/.virtualenvs/venv01 下
4. 可直接呼叫 `deactive` 指令離開虛擬環境
5. 設定zsh最右方顯示虛擬環境名稱: (ref. https://blog.csdn.net/Zero_S_Qiu/article/details/104217295)

# 此專案的 Mac 虛擬環境名稱
1. 名稱：venv_MouseRobot
2. 路徑：/Users/roger/.virtualenvs/venv_MouseRobot

# 打包成exe (PyInstaller)
|說明|連結|
|:-:|:-:|
|【Python】使用 PyInstaller 將 Python打包成 exe 檔|https://reurl.cc/Er7Qdv|
|使用自訂icon(需使用ico圖檔)|https://reurl.cc/Xj6QOg|
|指令|$ pyinstaller --name=PartyKonMing  --icon=.\images\KonMing.ico --clean -F .\MouseRobot.py|
|指令|$ pyinstaller -F 就是 --onefile|

# Python 製作視窗程式
|說明|連結|
|:-:|:-:|
|為應用程式設計圖形化介面，使用Python Tkinter 模組|https://www.rs-online.com/designspark/python-tkinter-cn|
|綁定空白鍵事件|https://stackoverflow.com/questions/15753793/how-to-bind-spacebar-key-to-a-certain-method-in-tkinter-python|

# 參考資料
|說明|連結|
|:-:|:-:|
|心臟線方程式|https://baike.baidu.hk/item/%E5%BF%83%E8%87%9F%E7%B7%9A/10323843|
|導出使用的package|pip freeze > ./requirements.txt|
|安裝使用的package|pip install -r ./requirements.txt|
|PyInstaller打包exe|https://reurl.cc/Er7Qdv|
|建立只有一個元素的元組 tuple|https://shengyu7697.github.io/python-tuple/|
|Python跨檔案共享全域性變數|https://www.gushiciku.cn/pl/gUtK/zh-tw|
|傳遞function ref作為參數|https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/|
|偵測視窗關閉 WM_DELETE_WINDOW |https://reurl.cc/4Qea0V|




