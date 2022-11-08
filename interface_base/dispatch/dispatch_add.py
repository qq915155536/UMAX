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
        num = len(flight_info)
        info_log = '航班总数：{0},  航班详情：{1}'.format(num, flight_info)
        session.logger.info(info_log)
        # 提取航班信息id
        flight_ids = jsonpath(info1, '$..id')
    else:
        session.logger.error('获取航班信息失败，报错如下：')
        session.logger.error(res1.json())

    #  2.选择规则,获得规则详情
    rule_type_id = '4a5afc59937172de9870b2cbac5b27e9'  # 浦东极限违规
    # rule_type_id='4a5afc59937172de9870b2cbac5b27e9'  # 浦东轻度违规
    # rule_type_id='4a5afc59937172de9870b2cbac5b27e9'  #测试环境-自动派工
    url2 = session.conf_url + 'rule/' + rule_type_id
    res2 = session.session.get(url=url2)
    rule_info = res2.json()['data']
    if res2.json()['code'] == 200:
        # 新增下一步的规则详情
        allRuleDTOList = [
            {'foodRuleAlertTimeDTO': rule_info['foodRuleAlertTime'],
             'foodRuleConnectionLineDTO': rule_info['foodRuleConnectionLine'],
             'foodRuleEmployeeQualificationDTO': rule_info['foodRuleQualification'],
             'foodRuleFleetShipDTO': rule_info['foodRuleFleetShipVO'],
             'foodRuleJoinTimeDTO': rule_info['foodRuleJoinTime'],
             'foodRuleLoadingTimeDTO': rule_info['foodRuleLoadingTime'],
             'foodRuleMealTimeDTO': rule_info['foodRuleMealTime'],
             'foodRuleRegionTimeDTO': rule_info['foodRuleRegionTime'],
             'foodRuleScheduleTimeDTO': rule_info['foodRuleScheduleTime'],
             'foodRuleTeamDTO': rule_info['foodRuleTeam'],
             'foodRuleTeamTimeDTO': rule_info['foodRuleTeamTime'],
             'foodRuleTimeDTO': rule_info['foodRuleTime'],
             'ruleTypeId': rule_type_id,
             'ruleTypeName': "浦东极限违规"
             }
        ]
        session.logger.info('所选规则的详情为：')
        session.logger.info(allRuleDTOList)
    else:
        session.logger.error('所选规则有误！')
        session.logger.error(res2.json())

    #   3.准备新增派工的入参及url
    url3 = session.conf_url + 'workOrder'
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    data = {
        'allRuleDTOList': allRuleDTOList,
        'flightIds': flight_ids,
        'isInitTask': 0,  # 自动-算法计算
        # 'isInitTask': 1,  # 手动-人工排班
        'orderName': '【测试脚本生成】' + now_time,
        'orderTimeBegin': start_time,
        'orderTimeEnd': end_time,
        'ruleTypeIdList': [rule_type_id]
    }
    res3 = session.session.post(url=url3, json=data)
    info3 = res3.json()
    if info3['code'] == 200:
        order_name = data['orderName']
        session.logger.info(f'派工任务，新增成功,任务名为:{order_name}')
    else:
        session.logger.error('新增失败！')
        session.logger.error(info3)


if __name__ == '__main__':
    # 航班时间段：
    flight_start_time = '2022-11-08 08:00'
    flight_end_time = '2022-11-08 21:00'
    select_flight('dev', flight_start_time, flight_end_time)
