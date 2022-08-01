#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/20 17:26
# Author :小灬天
# QQ:915155536
# File :my_except.py
#  ===========================
try:
    # 不能确定争取执行的代码
    # 提示用户输入一个数字
    num = int(input("请输入一个数字："))
except Exception as e :
    print("请输入一个正确的数字！",e)
else:
    print('没异常则会执行，有异常则不会执行！')
finally:
    print('无论有没有异常，都会执行')
print("-" * 50)

# 主动抛出异常
ex=Exception('故意抛出异常！')
raise ex