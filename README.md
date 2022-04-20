# Python-MouseRobot
Python-滑鼠機器人-笛卡兒心臟線

# 建立mac虛擬環境
1. Mac可如此連結建立虛擬環境設定: (ref. https://stackoverflow.com/questions/49470367/install-virtualenv-and-virtualenvwrapper-on-macos)
2. 設定好虛擬環境後，Mac可使用 `mkvirtualenv venv01` 建立虛擬環境(會生成在 ~/.virtualenvs 中)
3. 可使用 `workon venv01` 進入虛擬環境，此時 `pip install` 的lib會生成在 ~/.virtualenvs/venv01 下
4. 可直接呼叫 `deactive` 指令離開虛擬環境
5. 設定zsh最右方顯示虛擬環境名稱: (ref. https://blog.csdn.net/Zero_S_Qiu/article/details/104217295)

# 打包成exe (PyInstaller)
|說明|連結|
|:-:|:-:|

# 參考資料
|說明|連結|
|:-:|:-:|
|心臟線方程式|https://baike.baidu.hk/item/%E5%BF%83%E8%87%9F%E7%B7%9A/10323843|
|導出使用的package|pip freeze > ./requirements.txt|
|安裝使用的package|pip install -r ./requirements.txt|
|PyInstaller打包exe|https://medium.com/pyladies-taiwan/python-%E5%B0%87python%E6%89%93%E5%8C%85%E6%88%90exe%E6%AA%94-32a4bacbe351|




