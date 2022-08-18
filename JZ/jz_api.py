#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/8/18 16:42
# Author :小灬天
# QQ:915155536
# File :jz_api.py
#  ===========================
import requests
from base_api.log.log_api import my_log


class JzSession:
    # 初始化登录状态的会话，并集成日志
    def __init__(self, conf):
        self.logger = my_log()
        self.session = requests.session()
        self.conf = conf
        self.conf_url = None
        self.info_dict = {
            'dev': 'http://11.168.3.186:89/dsApi/',
            'test': 'http://11.168.3.186:90/dsApi/',
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
        # 基础请求头
        # base_headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
        # 接口返回数据处理，把认证加入会话头部
        # self.session.headers.update(base_headers)
        self.logger.info(f'{self.conf}环境登录成功！')


if __name__ == '__main__':
    my_session = JzSession('dev')
    print(my_session.conf_url)
