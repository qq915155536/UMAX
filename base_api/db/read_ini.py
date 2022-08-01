#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/6 20:01
# Author :小灬天
# QQ:915155536
# File :read_ini.py
#  ===========================
import configparser

def read_db_ini(conf):
    """
    :param conf: 数据库环境
    :return:数据库配置字典:conf_dict
    """
    res=configparser.ConfigParser()
    #读取配置到内存
    #需写绝对路径，若写相对路径，其他地方引用，会报错，找不到配置文件
    res.read(r'D:\My_Project\just_test\base_api\db\db.ini')
    #读取所有配置信息，元组列表
    info=res.items(conf)
    #把元组列表转转为字典
    conf_dict=dict(info)
    return conf_dict

if __name__ == '__main__':
    dev_dict=read_db_ini('dev')
    print(dev_dict)