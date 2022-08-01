from selenium.webdriver import ChromeOptions


class Options:
    # 初始化配置对象options
    def __init__(self):
        self.options = ChromeOptions()

    # 加载配置
    def options_conf(self):
        # 添加试验性质的配置项
        # self.options.add_experimental_option()
        # # 添加常规设定
        # self.options.add_argument()
        # 页面加载策略 (1.normal，即等着全部页面加载完毕；2.none,是把html下载完毕；eager，html下载并解析完毕。)
        self.options.page_load_strategy = 'eager'
        # 去掉自动化提示
        self.options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        # 去掉保存密码弹框
        prefs = {}
        prefs['credentials_enable_service'] = False
        prefs['profile.password_manager_enabled'] = False
        self.options.add_experimental_option('prefs', prefs)
        # 窗体最大化
        self.options.add_argument('start-maximized')
        # 指定浏览器位置
        # self.options.add_argument('window-position=500,200')
        # 指定窗口大小
        # self.options.add_argument('window-size=400,400')
        # 无头模式:无界面运行
        # self.options.add_argument('--headless')

        return self.options


if __name__ == '__main__':
    test_options = Options().options_conf()
    from selenium import webdriver

    d = webdriver.Chrome(options=test_options)
    d.get('http://www.baidu.com')
