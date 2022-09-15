#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/9/6 13:48
# Author :小灬天
# QQ:915155536
# File :view_calculation_results.py
#  ===========================
from interface_base.base_session import BaseSession
from jsonpath import jsonpath
from collections import Counter

# 查看计算结果，需传入workOrderId
def view_calculation_results(workOrderId):
    session = BaseSession('dev')
    url = session.conf_url + 'algorithmResult/' + workOrderId
    params = {'workOrderId': workOrderId}
    res = session.session.get(url=url, params=params)
    info = res.json()
    if info['code'] == 200:
        session.logger.info('查询成功，结果如下：')
        #处理返回结果，查询目标数据
        l2=jsonpath(info,'$..flightNo')
        print('原接口航班号：',l2)
        #统计航班号出现次数：
        print(Counter(l2))
        print(len(Counter(l2)))
    else:
        session.logger.error('查询失败！，错误如下：')
        session.logger.error(info)

if __name__ == '__main__':
    work_order_id = '58b2c37d5ae67b6d67e65217c3fde9d7'
    view_calculation_results(work_order_id)
