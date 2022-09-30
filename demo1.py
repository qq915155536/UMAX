#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/18 14:37
# Author :小灬天
# QQ:915155536
# File :dispatch_add.py
#  ===========================
from interface_base.base_session import BaseSession

session=BaseSession('dev')
url='ws://11.168.3.235:8081/algorithm/d8e58781be505229e3c87c4159910d04/2'
session.session.get(url=url)
