#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/8/18 16:51
# Author :小灬天
# QQ:915155536
# File :sx.py
#  ===========================
from JZ.jz_api import JzSession
from jsonpath import jsonpath

session = JzSession('dev')
# 查询属性
url = session.conf_url + 'systemExtendAttr/pageQuery'
param = {
    'moduleFlag': 'F',
    'pageNum': 1,
    'pageSize': 10
}
data = {}
res = session.session.post(url=url, params=param, json=data)
info = res.json()
tag = info['code']
if tag == 200:
    session.logger.info('属性查询成功，结果如下：')
    sx_info = jsonpath(info, '$..name')
    session.logger.info(sx_info)
else:
    session.logger.error('属性查询失败！')
    session.logger.error(info)
