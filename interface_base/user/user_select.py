#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/6 19:29
# Author :小灬天
# QQ:915155536
# File :user_select.py
#  ===========================


from interface_base.base_session import BaseSession
from jsonpath import jsonpath


# 用户查询接口
def user_select(conf):
    session = BaseSession(conf)
    # 1)准备接口url
    url = session.conf_url + 'user'
    # 2）接口参数
    parm = {
        'pageNum': 1,
        'pageSize': 10
    }
    # 3）请求接口
    res = session.session.get(url=url, params=parm)
    # 4）接口返回数据处理（断言）
    tag = res.json()['code']
    if tag == 200:
        session.logger.info('查询用户接口，执行成功！')
        user_name = jsonpath(res.json(), '$..userName')
        session.logger.info(user_name)
    else:
        session.logger.error(res.json())


if __name__ == '__main__':
    # 查询指定环境的用户列表信息
    user_select('dev')
