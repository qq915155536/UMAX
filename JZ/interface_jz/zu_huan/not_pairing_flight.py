#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/9/2 10:28
# Author :小灬天
# QQ:915155536
# File :not_pairing_flight.py
#  ===========================
from JZ.jz_api import JzSession
from jsonpath import jsonpath

session = JzSession('dev')

# 查询未组环航班信息
url = session.conf_url + 'prApi/schPairing/queryAircraftFlightGantt'
para = {'moduleFlag': 'F',
        'solutionId': None,
        'startTime': '2022-04-01',
        'endTime': '2022-04-07',
        'filialeCodeList': 'UX',
        'fleetSeriesList': 'A320',
        'sourceRankCode': 'A001'
        }
res = session.session.get(url=url, params=para)
info = res.json()
# if info['code'] == 200:
#     session.logger.info('查询成功！')
#     session.logger.info(info)
# else:
#     session.logger.error('查询失败，报错如下：')
#     session.logger.error(info)

id_list=jsonpath(info,'$..id')
print(len(id_list),id_list)
