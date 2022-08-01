#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/28 11:30
# Author :小灬天
# QQ:915155536
# File :food_car_delete.py
#  ===========================
from base_api.db.db_api import DB

my_db = DB('dev')
sql = """
DELETE 
FROM
	food_car 
WHERE
	car_no = '测试'
"""
my_db.execute_sql(sql)
