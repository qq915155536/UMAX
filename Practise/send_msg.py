#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/10/10 10:56
# Author :小灬天
# QQ:915155536
# File :send_msg.py
#  ===========================
import requests

# 消息推送平台： https://www.pushplus.plus/
url = 'https://www.pushplus.plus/api/send'

data = {"token": "1a1652284aba46d596e2151b7f2fb98f",
        "title": "测试-推动消息！",
        "content": "这里是只是测试而已！3333",
        "template": "html",
        "channel": "wechat"}
res = requests.post(url=url, json=data)
print(res.json())

