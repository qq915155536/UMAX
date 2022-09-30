#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/9/22 16:09
# Author :小灬天
# QQ:915155536
# File :select_employee_worktime.py
#  ===========================
from interface_base.base_session import BaseSession
from jsonpath import jsonpath

# 查询员工工作时间
session = BaseSession('dev')
url = session.conf_url + 'employeeWorkplan'
params = {'workTime': '2022-09-27', 'condition': None}
res = session.session.get(url=url, params=params)
id_list = jsonpath(res.json(), '$..id')
print(len(id_list), id_list)
