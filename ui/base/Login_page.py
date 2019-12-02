# @Time : 2019/12/2 17:15
# @Author : lisalou
# @File : Login_page.py
# @Software : PyCharm
from ui.base.Base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    url = BasePage.base_url+'/login'
    loginame = (By.CSS_SELECTOR, '[placeholder="手机号/邮箱"]')
    password = (By.CSS_SELECTOR, '[placeholder="密码"]')

    def __init__(self, driver):
        super().__init__(driver=driver, url=self.url)

    def login(self):
        self.open('豆瓣')
        self.send_keys(webElement=self.find_element(*self.USERNAME), keys='xxxxx')
        self.send_keys(webElement=self.find_element(*self.PASSWORD), keys='xxxxx')
        self.find_element(*self.SUBMIT_BTN).click()





