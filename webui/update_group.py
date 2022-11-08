#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/10/8 11:19
# Author :小灬天
# QQ:915155536
# File :update_group.py
#  ===========================
from webui.web_login import login

# 登录系统
browser = login()
# 进入人员岗位页面
browser.my_click('xpath', '//span[text()="基础信息"]')
# 人员岗位需通过调用js语句来定位
js = "arguments[0].click()"
obj = browser.my_location('xpath', '//span[text()="人员岗位"]')
browser.my_js(js, obj)
# 定位需要调整的班组
# 定位岗位（车长/航机/司机）
browser.my_click('xpath', '//td[text()="车长"]')
browser.my_sleep(1)
# 定位班组
# A组
# B组
# C组
# D组（做一休一）
# E组（做一休一）
# 过夜班组
browser.my_click('xpath', '//td[text()="A组"]')
browser.my_click('xpath', '//span[text()="调 整"]')
# 搜素添加人员至班组
num_list = [1615, 2103, 6670, 6724, 6851, 8312, 8467, 8489, 8561, 10585]
for num in num_list:
    browser.my_send_keys('xpath', '//input[@placeholder="请输入搜索内容"]', num)
    browser.my_sleep(0.5)
    browser.my_clear('xpath', '//input[@placeholder="请输入搜索内容"]')
    browser.my_click('xpath', '//input[@type="checkbox"]')
    browser.my_sleep(0.5)
    browser.my_click('xpath', '//div[@class="ant-transfer-operation"]/button')
    browser.my_sleep(0.5)
    browser.my_click('xpath', '//span[@class="anticon anticon-close-circle"]')
browser.my_click('xpath', '//span[text()="确 定"]')
browser.my_sleep(1)
browser.my_quit()
