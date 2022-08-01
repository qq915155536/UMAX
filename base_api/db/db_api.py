#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/6 20:05
# Author :小灬天
# QQ:915155536
# File :db_api.py
#  ===========================
from base_api.db.read_ini import read_db_ini
import pymysql


class DB:
    def __init__(self, conf):
        """
        设置数据库环境
        :param conf: 数据库环境
        """
        self.conf = conf

    # sql执行函数
    def execute_sql(self, sql):
        """
        :param sql: 待执行sql语句
        :return: 返回执行结果
        """
        # 获取数据库字典配置
        dict = read_db_ini(self.conf)
        # print('这里是数据库字典配置：', dict)
        # 连接数据库
        try:
            my_db = pymysql.connect(**dict)
        except Exception as e:
            print(f'数据库连接错误：{e}')
        try:
            # 创建游标
            cur = my_db.cursor()
            # 执行sql语句
            cur.execute(sql)
            my_db.commit()
            res = cur.fetchall()
            my_db.close()
            return res
        except Exception as f:
            print(f'sql语句执行错误！{f}')


if __name__ == '__main__':
    sql = 'SELECT company_name FROM food_company WHERE 1=1'
    dev_db = DB('dev')
    print(dev_db.execute_sql(sql))
