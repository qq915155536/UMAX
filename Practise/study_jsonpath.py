#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/9/30 14:09
# Author :小灬天
# QQ:915155536
# File :study_jsonpath.py
#  ===========================
import jsonpath

data = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}

"""
$ --  根节点 
@ -- 当前节点
. --  子节点
.. -- 所有符合条件的内容
*  -- 表示所有的元素节点
【，】 --表示多选 
？（）表示过滤操作
"""
# jsonpath(json数据，定位表达式)  ,返回的是list
# bicycle = jsonpath.jsonpath(data, '$.store.bicycle')
# print(bicycle)

# 获取所有price的值
# price = jsonpath.jsonpath(data, '$..price')
# print(price)

# 获取所有price>10的所有book
price = jsonpath.jsonpath(data, '$..book[?(@.price>10)]')
print(price)

# 过滤器是用于过滤数组的逻辑表达式，# 可以通过逻辑表达式&&或||组合多个过滤器表达式，
# [?(@.age > 18)]
# [?(@.price < 10 && @.category == ‘fiction’)]
# eg:
#   str2 = jsonpath(info, '$..ganttFlightList[?(@.carNo=="虚拟车辆0"&&@.flightNo=="5143")]')
