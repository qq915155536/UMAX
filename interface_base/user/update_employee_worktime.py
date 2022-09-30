#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/9/14 15:32
# Author :小灬天
# QQ:915155536
# File :update_employee_worktime.py
#  ===========================
from interface_base.base_session import BaseSession

# 批量调整员工工作时间

# 设置参数
# 员工工号列表
employeeNoList = ["8558",
                  "8597",
                  "2705",
                  "8545",
                  "10522",
                  "10541",
                  "15060",
                  "15125",
                  "16052"]
# 早班
# onWorkTime = "04:00"
# offWorkTime = "11:30"
# 中班
# onWorkTime = "06:00"
# offWorkTime = "16:00"
# 做一休一
# onWorkTime = "06:00"
# offWorkTime = "18:30"
# 过夜
onWorkTime = "18:00"
offWorkTime = "06:30"


#调整时间所处日期段
workDateBegin = "2022-09-16"
workDateEnd = "2022-09-16"
data = {
    "crossNight": True,
    "employeeNoList": employeeNoList,
    "onWorkTime": onWorkTime,
    "offWorkTime": offWorkTime,
    "workDateBegin": workDateBegin,
    "workDateEnd": workDateEnd
}

# 请求接口
session = BaseSession('dev')
url = session.conf_url + 'employeeWorkplan/batch'
res = session.session.put(url=url, json=data)
if res.json()['code'] == 200:
    session.logger.info(res.json())
else:
    session.logger.error(res.json())
