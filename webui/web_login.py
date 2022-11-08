#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/8 19:22
# Author :小灬天
# QQ:915155536
# File :web_login.py
#  ===========================
from webui.webui_base import WebUi


def login():
    browser = WebUi()
    browser.my_visit('http://11.168.3.220:8081/user/login')
    # 输入用户名、密码
    browser.my_send_keys('id', 'account', 'cs004')
    browser.my_send_keys('id', 'password', '123456')
    # 选择航食中心
    browser.my_click('id', 'threeCode')
    browser.my_sleep(0.5)
    browser.my_click('xpath', '//div[text()="浦东中心"]')
    # 输入验证码，点击登录
    browser.my_send_keys('id', 'verifyCode', '123456')
    browser.my_click('xpath', '//span[text()="登 录"]')
    return browser


if __name__ == '__main__':
    my_browser = login()
    # 进入人员岗位页面
    # my_browser.my_click('xpath', '//span[text()="基础信息"]')
