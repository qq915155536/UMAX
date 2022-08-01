#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/29 16:48
# Author :小灬天
# QQ:915155536
# File :version_select.py
#  ===========================
from interface_base.base_session import BaseSession


# 1.查询版本
def version_select(conf):
    session = BaseSession(conf)
    url = session.conf_url + 'base/code/version/control/page'
    data = {'pageNum': 1, 'pageSize': 10}
    res = session.session.get(url=url, data=data)
    # 结果断言
    tag = res.json()['code']
    if tag == 200:
        session.logger.info('查询版本成功！结果如下：')
        session.logger.info(res.json())
    else:
        session.logger.error('查询版本失败！报错如下：')
        session.logger.error(res.json())


if __name__ == '__main__':
    version_select('dev')
