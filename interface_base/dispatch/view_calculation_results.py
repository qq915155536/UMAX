#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/10/11 9:36
# Author :小灬天
# QQ:915155536
# File :view_calculation_results.py
#  ===========================
from interface_base.base_session import BaseSession
from jsonpath import jsonpath
import json
from collections import Counter


# 查看计算结果（甘特图），需传入workOrderId
def view_calculation_results(workOrderId):
    session = BaseSession('dev')
    url = session.conf_url + 'algorithmResult/' + workOrderId
    params = {'workOrderId': workOrderId}
    res = session.session.get(url=url, params=params)
    info = res.json()
    if info['code'] == 200:
        session.logger.info('查询成功，结果如下：')
        # 处理返回结果，查询目标数据
        l2 = jsonpath(info, '$..flightNo')
        print('原接口航班号：', l2)

        # 统计航班号出现次数：
        # print(Counter(l2))
        # print(len(Counter(l2))

        # 查找某一车辆的详细信息
        car_no = '虚拟车辆30'
        path_str = '$..[?(@.carNo=="{0}")]'.format(car_no)
        l3 = jsonpath(info, path_str)
        print(l3)
        l3 = json.dumps(l3, ensure_ascii=False)
        print(f'{car_no}的详细信息为：', l3)

    else:
        session.logger.error('查询失败！，错误如下：')
        session.logger.error(info)


if __name__ == '__main__':
    work_order_id = '62ed4194605bc29b83c4e0b7e0759378'
    view_calculation_results(work_order_id)
