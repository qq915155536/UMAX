#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/18 14:37
# Author :小灬天
# QQ:915155536
# File :dispatch_add.py
#  ===========================
import time
from jsonpath import jsonpath
from interface_base.base_session import BaseSession


# 1.登录并获取指定时间段内的航班信息
def select_flight(conf, start_time, end_time):
    session = BaseSession(conf)
    # 1)准备接口url、headers
    url1 = session.conf_url + 'workOrder/flight'
    # 2）接口参数
    parm = {
        'beginDateTime': start_time,
        'endDateTime': end_time,
        'timeSegments': 3
    }
    # 3）请求接口,获取航班id
    res1 = session.session.get(url=url1, params=parm)
    # 3）接口返回数据处理（断言）
    info1 = res1.json()
    tag = info1['code']
    flight_ids = None
    if tag == 200:
        session.logger.info('获取航班接口，执行成功！派工任务航班号信息如下：')
        carriers = jsonpath(res1.json(), '$..carrier')
        flight_nums = jsonpath(res1.json(), '$..flightNo')
        flight_info = [i + j for i, j in zip(carriers, flight_nums)]
        session.logger.info(flight_info)
        # 提取航班信息id
        flight_ids = jsonpath(info1, '$..id')
    else:
        session.logger.error('获取航班信息失败，报错如下：')
        session.logger.error(res1.json())

    #   2.准备新增派工的入参及url
    url2 = session.conf_url + 'workOrder'
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    data = {
        'flightIds': flight_ids,
        'orderName': '【测试脚本生成】' + now_time,
        'orderTimeBegin': start_time,
        'orderTimeEnd': end_time,
        'ruleTypeId': '1a7371325efd1e113920df8584f3a429'
    }
    res2 = session.session.post(url=url2, json=data)
    info2 = res2.json()
    if info2['code'] == 200:
        order_name = data['orderName']
        session.logger.info(f'派工任务，新增成功,任务名为:{order_name}')
    else:
        session.logger.error('新增失败！')
        session.logger.error(info2)


if __name__ == '__main__':
    # 航班时间段：
    flight_start_time = '2022-08-01 14:20'
    flight_end_time = '2022-08-01 15:00'
    select_flight('dev', flight_start_time, flight_end_time)
