# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 10:31
# @Author  : MARX·CBR
# @File    : windows.py

import sys, os
from pynput.keyboard import Controller, Key, Listener
from myRedisServer import redisServer

rs = redisServer()


class windowsClient:
    def __init__(self):
        self.tmp = ""
        self.keys = ""

    # 监听按压
    def on_press(self, key):
        try:
            print("正在按压:", format(key))
            rs.send_msg_on_press(key.char)
        except AttributeError:
            rs.send_msg_on_press(key)
            print("正在按压:", format(key))
        # self.tmp = self.tmp + "{},".format(key)

    # 监听释放
    def on_release(self, key):
        print("已经释放:", format(key))
        rs.send_msg_on_release(key)
        # if key == Key.esc:
        #     # 停止监听
        #     print("ESC")
        #     # return False
        # if key.char in self.tmp:
        #     self.keys = "{},".format(key) + self.tmp
        #     self.tmp.replace("'{}',".format(key), "")
        # else:
        #     ...
        # if len(self.tmp) == 0:
        #     print(self.keys)
        #     self.keys = ""

    # 开始监听
    def start_listen(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

# TODO : 键鼠同步功能后期看情况进行完善，目前使用synergy
if __name__ == '__main__':
    # 实例化键盘
    # kb = Controller()
    # kb.pressed(Key.cmd)
    # # 使用键盘输入一个字母
    # kb.press('a')
    # kb.release('a')
    #
    # # 使用键盘输入字符串,注意当前键盘调成英文
    # kb.type("中文啊")
    #
    # # 使用Key.xxx输入
    # kb.press(Key.space)

    # 开始监听,按esc退出监听
    windowsClient().start_listen()
