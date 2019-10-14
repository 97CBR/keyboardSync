# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 14:04
# @Author  : MARX·CBR
# @File    : myRedisServer.py

import redis


class redisServer:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 2019
        self.redis_manager = redis.Redis(self.ip, port=self.port, password="*****")
        # print(self.redis_manager.exists("cbr"))

    # 判断车辆是否离开停车场
    def send_msg_on_press(self, name):
        pub = self.redis_manager.publish("marx", name)

    def send_msg_on_release(self, name):
        pub = self.redis_manager.publish("cbr", name)

    def get_msg(self, tunnel):
        sub = self.redis_manager.pubsub()
        sub.subscribe(tunnel)
        sub.parse_response()
        return sub


# obj = redisServer()
# print(obj.send_msg("test"))
