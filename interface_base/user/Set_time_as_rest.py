#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/9/14 15:52
# Author :小灬天
# QQ:915155536
# File :Set_time_as_rest.py
#  ===========================
from interface_base.base_session import BaseSession

# 把员工工作时间，置为休息
# 设置参数(工作时间id)
time_id = 'ff37ec90ee41c4bf7673735adb8f5132'

# 请求接口
session = BaseSession('dev')
url = session.conf_url + 'employeeWorkplan/' + time_id
res = session.session.delete(url=url)
if res.json()['code'] == 200:
    session.logger.info(res.json())
else:
    session.logger.error(res.json())
