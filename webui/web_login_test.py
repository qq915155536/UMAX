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
# 输入用户名、密码
bowser.my_send_keys('id', 'account', 'cs004')
bowser.my_send_keys('id', 'password', '123456')
# 选择航食中心
bowser.my_click('id', 'threeCode')
bowser.my_sleep(1)
bowser.my_click('xpath', '//div[text()="浦东中心"]')
# 输入验证码，点击登录
bowser.my_send_keys('id', 'verifyCode', '123456')
bowser.my_click('xpath', '//span[text()="登 录"]')
