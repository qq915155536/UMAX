#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/6 18:55
# Author :小灬天
# QQ:915155536
# File :log_api.py
#  ===========================
import logging
import colorlog


def my_log():
    logger = logging.getLogger('test_log')
    # 解决日志重复打印问题
    if not logger.handlers:
        # 设置日志级别
        logger.setLevel(logging.INFO)
        # 设置日志格式器
        # 1)普通格式
        # fm='【%(asctime)s】  %(filename)s  【%(levelname)s】  line:%(lineno)d  ——>>%(message)s<<——'
        # fmt=logging.Formatter(fmt=fm)
        # 2)颜色格式
        fm = '%(log_color)s【%(asctime)s】%(filename)s【%(levelname)s】line:%(lineno)d | %(message)s'
        fmt = colorlog.ColoredFormatter(fm)
        # 设置控制台处理器
        sh = logging.StreamHandler()
        # 设置文件处理器
        # fh=logging.FileHandler(r'D:\My_Project\just_test\base_api\log\log_file\test.log',encoding='utf-8')
        # 为处理器设置格式器
        sh.setFormatter(fmt)
        # fh.setFormatter(fmt)
        # 为日志添加处理器
        logger.addHandler(sh)
        # logger.addHandler(fh)
    return logger


if __name__ == '__main__':
    my_logger = my_log()
    my_logger.debug('debug')
    my_logger.info('info')
    my_logger.warning('warning')
    my_logger.error('error')
    my_logger.critical('critical')
