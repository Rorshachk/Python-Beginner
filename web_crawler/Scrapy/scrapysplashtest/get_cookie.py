from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


class Taobao_Spider:

    def __init__(self, username, password):
        """初始化参数"""
        url = 'https://login.taobao.com/member/login.jhtml'
        self.url = url

        options = webdriver.ChromeOptions()
        # 不加载图片,加快访问速度
        options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2})
        # 设置为开发者模式，避免被识别
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])
        self.browser = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.browser, 10)
        # 初始化用户名
        self.username = username
        # 初始化密码
        self.password = password

    def run(self):
        """登陆接口"""
        self.browser.get(self.url)
        try:
            # 这里设置等待：等待输入框
            login_element = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
            login_element.click()

            sina_login = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))
            sina_login.click()

            weibo_user = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.username > .W_input')))
            weibo_user.send_keys(self.username)

            sina_password = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.password > .W_input')))
            sina_password.send_keys(self.password)

            submit = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.btn_tip > a > span')))
            submit.click()

            taobao_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                          '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))
            # 登陆成功打印提示信息
            print("登陆成功：%s" % taobao_name.text)
            cookies = self.browser.get_cookies()
            with open('in.json', 'w') as f:
                json.dump(cookies, f)

        except Exception:
            self.browser.close()
            print("登陆失败")


if __name__ == "__main__":
    username = input("请输入你的微博用户名:")
    password = input("请输入密码:")

    spider = Taobao_Spider(username, password)
    spider.run()


'''
import requests
from urllib.parse import urlencode


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    # 登录后的cookie
    'cookie': 'thw=cn; t=2a5c07a3b4c1dbb94c07b0b9f2043af9; cna=boerExS9kCwCAXPKmbmQnPil; miid=845071084383715038; hng=CN%7Czh-CN%7CCNY%7C156; tg=0; enc=xCrPUzOlIcKvC8HMX%2Fi0xhrJwRenQmkPHFSSCBDZJieX92Z29qWty8y2GnVsIEkHQ1z91uYjze%2BDoYrRjdlnRw%3D%3D; UM_distinctid=168d0a5cc661f5-0f83e0495d213a-b781636-1fa400-168d0a5cc67ab7; x=e%3D1%26p%3D*%26s%3D0%26c%3D1%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; cookie2=1c8a5f479e03ad03a1300b4523dbd34e; _tb_token_=5d830f8e33e8e; _m_h5_tk=399748255d21443d4c8c5d67d05ca6a3_1555435479015; _m_h5_tk_enc=16f0f0a4c6b9733ef466d726997d7fc2; v=0; unb=3330702905; sg=25a; _l_g_=Ug%3D%3D; cookie1=BxvEgaAehE8yB0hc2t7eQe%2F3stOCBPisIcQfdrdTLcU%3D; tracknick=t_1497968676242_0732; lgc=t_1497968676242_0732; dnk=t_1497968676242_0732; _nk_=t_1497968676242_0732; cookie17=UNN%2BxtrxfuPO5Q%3D%3D; skt=549e4d4dac5facbe; csg=9592379c; uc3=vt3=F8dByEfL9ZReKpMKJIc%3D&id2=UNN%2BxtrxfuPO5Q%3D%3D&nk2=F6k3HMtynvpgmy4rUUdTvF1Va5Q%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTU1NTQyNzY4OA%3D%3D; _cc_=UIHiLt3xSw%3D%3D; mt=ci=11_1&np=; uc1=cookie14=UoTZ4SEI2jjilg%3D%3D&lng=zh_CN&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&existShop=false&cookie21=W5iHLLyFeYZ1WM9hVnmS&tag=8&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&pas=0; JSESSIONID=EEE615F2913262465EF1D8EA202EBF09; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; isg=BA0NWL3nbVnKt87kGiAB2nLOHClHQkKk78I_00-SSaQTRi34FzpRjFvUtJqFnVl0; l=bBjVrPaIvOlyt5JBBOCanurza77OSIRYYuPzaNbMi_5QP6T_9q_OlaNJrF96Vj5RsX8B4R15R8p9-etkZ',
}

params = {
    'q': 'iphone',
    'imgfile': '',
    'commend': 'all',
    'ssid': 's5-e',
    'search_type': 'item',
    'sourceId': 'tb.index',
    'spm': 'a21bo.2017.201856-taobao-item.2',
    'ie': 'utf8',
    'initiative_id': 'tbindexz_20170306',
}

url = 'https://s.taobao.com/search?' + urlencode(params)
s = requests.Session()
response = s.get(url, headers=headers, verify=False).text
print(response)
'''
