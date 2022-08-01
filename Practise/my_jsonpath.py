#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/27 14:00
# Author :小灬天
# QQ:915155536
# File :my_jsonpath.py
#  ===========================
from jsonpath import jsonpath

# 1.json数据
# data = None
data = {'code': 200, 'message': '', 'data': {
    '1200-1500': [{'id': '3520487', 'flightNo': '7399', 'acType': '789', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3520505', 'flightNo': '7333', 'acType': '33L', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3520522', 'flightNo': '7583', 'acType': '773', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3520550', 'flightNo': '6565', 'acType': '320', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3520551', 'flightNo': '7729', 'acType': '33L', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3520562', 'flightNo': '7551', 'acType': '359', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3520569', 'flightNo': '9366', 'acType': '73H', 'carrier': 'FM', 'inOrOut': '进'},
                  {'id': '3520673', 'flightNo': '6967', 'acType': '319', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3520724', 'flightNo': '5142', 'acType': '319', 'carrier': 'MU', 'inOrOut': '进'},
                  {'id': '3520737', 'flightNo': '5184', 'acType': '319', 'carrier': 'MU', 'inOrOut': '进'},
                  {'id': '3520883', 'flightNo': '5264', 'acType': 'ARJ', 'carrier': 'MU', 'inOrOut': '进'},
                  {'id': '3520921', 'flightNo': '5695', 'acType': '32L', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3521162', 'flightNo': '5585', 'acType': '32L', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3521224', 'flightNo': '9133', 'acType': '73H', 'carrier': 'FM', 'inOrOut': '出'},
                  {'id': '3521245', 'flightNo': '9178', 'acType': '73E', 'carrier': 'FM', 'inOrOut': '进'},
                  {'id': '3521249', 'flightNo': '9085', 'acType': '73E', 'carrier': 'FM', 'inOrOut': '出'},
                  {'id': '3521269', 'flightNo': '9189', 'acType': '73L', 'carrier': 'FM', 'inOrOut': '出'},
                  {'id': '3521377', 'flightNo': '5248', 'acType': '32L', 'carrier': 'MU', 'inOrOut': '进'},
                  {'id': '3521538', 'flightNo': '5377', 'acType': '33E', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3521624', 'flightNo': '5600', 'acType': '321', 'carrier': 'MU', 'inOrOut': '进'},
                  {'id': '3521805', 'flightNo': '5231', 'acType': '323', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3521985', 'flightNo': '5602', 'acType': '320', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3522011', 'flightNo': '7107', 'acType': '33L', 'carrier': 'MU', 'inOrOut': '进'}],
    '1500-1600': [{'id': '3520545', 'flightNo': '6563', 'acType': '32L', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3520547', 'flightNo': '7263', 'acType': '773', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3520678', 'flightNo': '9717', 'acType': '737', 'carrier': 'MU', 'inOrOut': '进'},
                  {'id': '3520822', 'flightNo': '5267', 'acType': '319', 'carrier': 'MU', 'inOrOut': '出'},
                  {'id': '3520931', 'flightNo': '5376', 'acType': '32L', 'carrier': 'MU', 'inOrOut': '进'},
                  {'id': '3521067', 'flightNo': '6071', 'acType': '325', 'carrier': 'MU', 'inOrOut': '进'},
                  {'id': '3521295', 'flightNo': '9146', 'acType': '73H', 'carrier': 'FM', 'inOrOut': '进'},
                  {'id': '3521727', 'flightNo': '5430', 'acType': '323', 'carrier': 'MU', 'inOrOut': '进'}]}}

# 2.提取表达式
# str1 = None
str1 = '$..id'

res = jsonpath(data, str1)
print(res)
