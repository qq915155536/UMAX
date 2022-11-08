#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/7/8 19:22
# Author :小灬天
# QQ:915155536
# File :web_base.py
#  ===========================
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webui.chrome_options import Options
from time import sleep


class WebUi:
    # 初始化浏览器
    def __init__(self):
        self.browser = webdriver.Chrome(options=Options().options_conf())
        self.browser.implicitly_wait(8)

    # 访问网址
    def my_visit(self, url):
        self.browser.get(url)

    # 定位元素
    def my_location(self, by, value):
        return self.browser.find_element(by, value)

    # 点击元素
    def my_click(self, by, value):
        self.my_location(by, value).click()

    # 输入文本
    def my_send_keys(self, by, value, text):
        self.my_location(by, value).send_keys(text)

    # 清空文本
    def my_clear(self, by, value):
        self.my_location(by, value).clear()

    # 文本断言
    def my_assert_text(self, by, value, expect):
        try:
            real = self.my_location(by, value).text
            assert real == expect, '预期：{0} 与 实际：{1} 不符'.format(expect, real)
        except Exception as e:
            print('断言失败，报错：{}'.format(e))

    # 句柄的切换：status=1,关闭首个句柄；否则不关闭。
    def switch_handle(self, status=1):
        handles = self.browser.window_handles
        if status == 1:
            self.browser.close()
        self.browser.switch_to.window(handles[1])

    # 强制等待
    @staticmethod
    def my_sleep(sec):
        sleep(sec)

    # 显式等待
    def my_force_wait(self, by, value):
        return WebDriverWait(self.browser, 10, 0.5).until(lambda el: self.my_location(by, value), message='元素获取失败')

    # 执行js语句
    def my_js(self, js, obj=None):
        self.browser.execute_script(js, obj)

    # 刷新浏览器
    def my_refresh(self):
        self.browser.refresh()

    # 退出浏览器
    def my_quit(self):
        self.browser.quit()


if __name__ == '__main__':
    browser = WebUi()
    browser.my_visit('http://www.baidu.com')
    browser.my_send_keys('id', 'kw', '测试')
    browser.my_click('id', 'su')
    browser.my_sleep(3)
    browser.my_quit()
