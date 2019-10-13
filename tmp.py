# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 20:00
# @Author  : MARX·CBR
# @File    : tmp.py
from pynput.keyboard import Controller

from myRedisServer import redisServer
import pyautogui

rs = redisServer()
tmp = []
keys = []
per = rs.get_msg("marx")
# rel = rs.get_msg("cbr")
tt = []
kb = Controller()
while 1:
    msg_p = per.parse_response()[2].decode()

    kb.press(msg_p)
    kb.release(msg_p)

    # if len(tt) == 2:
    #     pyautogui.typewrite(tt)
    #
    #     kb.type(tt)
    #
    #     tt.clear()
    # else
    #     tt.append(msg_p)
    # print(msg_p)
    # tt.clear()
    # msg_r = rel.parse_response()[2].decode()
    # if msg_p == msg_r:
    #     keys.append(msg_p)
    #     if msg_r in tmp:lkj
    #         keys.append(msg_r)kkjhkjjkjjkuf
    #         tmp.remove(msg_r)l
    #     else:
    #         tmp.append(msg_r)
    # else:
    #     tmp.append(msg_p)
    #
    # if len(tmp) == 0:
    #     print(keys)

    # if msg not in tmp:
    #     tmp.append(msg)
    # else:
    #     tmp.remove(msg)
    #     keys.append(msg)
    #     if len(tmp) == 0:
    #         print(keys)
    #         keys.clear()
    #     else:
    #         # print(tmp, keys)
    #         ...

    # print(msg, keys)
