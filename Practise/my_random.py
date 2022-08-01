#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/20 15:55
# Author :小灬天
# QQ:915155536
# File :my_random.py
#  ===========================
import random

# print(random.random()) #大于0且小于1之间的小数
# print(random.randint(1,3)) #大于等于1且小于等于3之间的整数
# print(random.choice([1,'哈哈',[1,2,4],(1,2,4)])) #随机取列表中的一个选项
# print(random.sample([1,'哈哈',[1,2,4],(1,2,4)],2)) #随机取列表中的2个选项
#
# item=[1,3,5,7,9]
# random.shuffle(item) #打乱item的顺序,相当于"洗牌"
# print(item)

#生成n位的随机验证码
def make_code(n):
    res=''
    for i in range(n):
        s1=chr(random.randint(65,90))
        s2=str(random.randint(0,9))
        res+=random.choice([s1,s2])
    return res

print(make_code(4))