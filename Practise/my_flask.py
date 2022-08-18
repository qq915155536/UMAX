#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/8/1 19:28
# Author :小灬天
# QQ:915155536
# File :my_flask.py
#  ===========================
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# 例子
# @app.route('/home')
# def login():
#     res1 = '欢迎来到主页：我的Flask！！'
#     return res1

# 登录接口
# @app.route('/home/login', methods=['post', 'get'])
# def login():
#     info = request.get_json()
#     print(type(info), info)
#     user = info['user']
#     pwd = info['pwd']
#     if user == 'admin' and pwd == 123456:
#         return '登录成功！'
#     else:
#         return '登录失败！'

# 登录接口 （返回json）
# @app.route('/home/login', methods=['post', 'get'])
# def login():
#     info = request.get_json()
#     print(type(info), info)
#     user = info['user']
#     pwd = info['pwd']
#     if user == 'admin' and pwd == 123456:
#         return jsonify({"code":200,"msg":"登录成功！"})
#     else:
#         return '登录失败！'

# 登录接口 （返回html）
@app.route('/home/login', methods=['post', 'get'])
def login():
        return render_template('index2.html')


if __name__ == '__main__':
    # app.run('127.0.0.1','5555',debug=True)
    app.run(debug=True)
