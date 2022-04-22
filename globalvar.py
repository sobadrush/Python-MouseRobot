"""
Python跨檔案共享全域性變數
ref. https://www.gushiciku.cn/pl/gUtK/zh-tw
"""

def _init():
    global _global_dict
    _global_dict = {}

def set_value(name, value):
    _global_dict[name] = value

def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue