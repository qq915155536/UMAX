#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/8/29 15:25
# Author :小灬天
# QQ:915155536
# File :menu_select.py
#  ===========================
from interface_base.base_session import BaseSession
from jsonpath import jsonpath


# 菜单查询接口
def user_select(conf):
    session = BaseSession(conf)
    # 1)准备接口url
    url = session.conf_url + 'menu'
    # 2）请求接口
    res = session.session.get(url=url)
    # 3）接口返回数据处理（断言）
    tag = res.json()['code']
    if tag == 200:
        session.logger.info('查询用户菜单，执行成功！')
        menu_name = jsonpath(res.json(), '$..name')
        session.logger.info(menu_name)
    else:
        session.logger.error(res.json())


if __name__ == '__main__':
    # 查询指定环境的用户菜单信息
    user_select('dev')
