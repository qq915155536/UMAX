#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/29 11:46
# Author :小灬天
# QQ:915155536
# File :base_session.py
#  ===========================
import requests
from base_api.log.log_api import my_log


class BaseSession:
    # 初始化登录状态的会话，并集成日志
    def __init__(self, conf):
        self.logger = my_log()
        self.session = requests.session()
        self.conf = conf
        self.conf_url = None
        self.info_dict = {
            'dev': 'http://11.168.3.220:8081/api/',
            'test': 'http://11.168.3.220:8082/api/',
            'conf': None,
            'conf_url': None
        }
        self.login()

    # 登录会话
    def login(self):
        try:
            self.info_dict['conf'] = self.conf
            self.info_dict['conf_url'] = self.info_dict[self.conf]
            self.conf_url = self.info_dict['conf_url']
        except Exception as e:
            self.logger.error(f'亲，输入的环境地址:{self.conf}，有误噢！错误信息{e}')
        # 拼接接口地址
        url = self.info_dict['conf_url'] + 'login'
        # 接口入参：用户名、密码
        data = {
            "account": "cs001",
            "password": "123456",
            "threeCode": "PVG",
            "verifyCode": "456"
        }
        # 基础请求头
        base_headers = {'threeCode': 'PVG'}
        # 请求接口
        res = self.session.post(url=url, json=data, headers=base_headers)
        tag = res.json()['code']
        if tag == 200:
            # 接口返回数据处理，把认证加入会话头部
            base_headers["Authorization"] = res.json()['data']['token']
            self.session.headers.update(base_headers)
            self.logger.info(f'{self.conf}环境登录成功！')
        else:
            self.logger.error('登录失败！')
            self.logger.error(res.json())


if __name__ == '__main__':
    my_session = BaseSession('dev')
    # my_session = BaseSession('test')