#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/20 15:34
# Author :小灬天
# QQ:915155536
# File :my_time.py
#  ===========================
import time
import datetime


print(time.time()) #时间戳

#获取当前时间
print(time.strftime('%Y-%m-%d  %X'))    ##格式化的时间字符串:'2017-02-15 11:40:53'
print(time.strftime('%Y-%m-%d  %H:%M:%S'))   #格式化的时间字符串:'2017-02-15 11:40:53'
print(time.localtime())  ##本地时区的struct_time

print(datetime.datetime.now())

print(time.strftime('%Y%m%d'))
