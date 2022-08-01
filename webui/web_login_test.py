#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/8 19:22
# Author :小灬天
# QQ:915155536
# File :web_login.py
#  ===========================
from webui.webui_base import WebUi

bowser = WebUi()
bowser.my_visit('http://11.168.3.220:8081/user/login')
bowser.my_send_keys('id', 'account', 'admin')
bowser.my_sleep(1)
bowser.my_send_keys('id', 'password', '123456')
bowser.my_send_keys('id', 'verifyCode', '123456')
bowser.my_click('xpath', '//span[text()="登 录"]')
