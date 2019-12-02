# -*- coding: utf-8 -*-

# @Time : 2019/12/2 13:44
# @Author : lisalou
# @File : Base_page.py
# @Software : PyCharm

"""
 base_page : 页面对象基类
"""
import datetime
import logging
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    base_url = "twww.bitasset.cc:7001"
    def __init__(self,driver):
        self.driver=driver;

    # 等待元素可见
    def wait_eleVisible(self,*loc,timeout=30,poll_frequency=0.5,model=None):
        '''
        :param loc: 元素定位表达式。元组类型，表达方式（元素定位类型，元素定位方法）
        :param timeout: 等待时间
        :param poll_frequency: 频率
        :param model: 等待失败时，截屏需要的功能说明
        :return:
        '''
        logging.info('在{1}等待元素{0}可见'.format(loc,model))
        try:
            start=datetime.datetime.now()
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.invisibility_of_element_located(loc))
            end = datetime.datetime.now()
            logging.info('等待了{}秒'.format((end-start).seconds))
        except:
            logging.exception('等待元素可见失败')
            #截图
            self.save_imgs(model)
            raise

    # 查找一个元素
    def get_Element(self,*loc,model=None):
        logging.info('在{0}：查找{1}元素'.format(model,loc))
        try:
            return self.driver.find_element(*loc)
        except:
            logging.exception('查找元素失败。')
            #截图
            self.save_imgs(model)
            raise

    # text输入操作
    def input_text(self,*loc,text,model=None):
        #查找元素
        ele=self.get_Element(loc,model)
        #输入操作
        logging.info('在{0}：元素{1}中输入文本：{2}'.format(model,loc,text))
        try:
            ele.send_keys(text)
        except:
            logging.exception('输入操作失败')
            #截图
            self.save_imgs(model)
            raise

    # textarea输入操作
    def input_textarea(self,*loc,text,model=None):
        #查找元素
        ele = self.get_Element(loc,model)
        #输入操作
        logging.info('在{0}：元素{1}中用js输入文本：{2}'.format(model,loc,text))
        try:
            js = "var js = document.getElementById('revOpinion');"
            self.driver.execute_script(js,'js.value=text')
        except:
            logging.exception('输入操作失败')
            #截图
            self.save_imgs(model)
            raise

    # 清除操作
    def clear_input_text(self,*loc,model=None):
        #查找元素
        ele = self.get_Element(loc,model)
        #清楚操作
        logging.info('在{0}清除{1}的内容'.format(model,loc))
        try:
            ele.clear()
        except:
            logging.exception('清除操作失败')
            #截图
            self.save_imgs(model)
            raise

    # 点击操作
    def click_element(self,*loc,model=None):
        #查找元素
        ele = self.get_Element(loc,model)
        #点击操作
        logging.info('在{0}点击{1}'.format(model,loc))
        try:
            ele.click()
        except:
            logging.exception('点击操作失败')
            #截图
            self.save_imgs(model)
            raise

    # 获取文本内容
    def get_text(self,*loc,model=None):
        #查找元素
        ele = self.get_Element(loc,model)
        #获取文本内容操作
        logging.info('在{0}：元素{1}中获取文本'.format(model.loc))
        try:
            return ele.text
        except:
            logging.exception('获取文本内容操作失败')
            #截图
            self.save_imgs(model)
            raise

    # 获取元素的属性
    def get_element_attribute(self,*loc,attr_name,model=None):
        #查找元素
        ele = self.get_Element(loc,model)
        #获取元素属性操作
        logging.info('在{0}：元素{1}的属性'.format(model.loc))
        try:
            return ele.get_attribute(attr_name)
        except:
            logging.exception('获取元素的属性内容操作失败')
            #截图
            self.save_imgs(model)
            raise

    # iframe切换
    def switch_iframe(self,frame_refer,timeout=30,poll_frequency=0.5,model=None):
        #frame_refer为index name id webElement
        #等待iframe存在，然后切换进来
        logging.info('iframe切换操作：')
        try:
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.frame_to_be_available_and_switch_to_it(frame_refer))
            time.sleep(0.5)
            logging.info('切换成功')
        except:
            logging.exception('切换失败！！！')
            #截图
            self.save_imgs(model)
            raise

    # 窗口切换
    # 如果切换到新窗口new,如果回到默认的窗口default
    def switch_window(self,name,cur_handles=None):
        pass

    # 截屏
    def save_imgs(self,model=None):
        pass

    # 滑动滚动条
    def sliding(self,*loc,model=None):
        #查找元素
        ele = self.get_Element(loc,model)
        #滑动滚动条
        logging.info('在{0}滑动滚动条，使{1}可见'.format(model,loc))
        try:
            self.driver.execute_script('arguments[0].scrollIntoView(false);',ele)
        except:
            logging.exception('滑动操作失败！！！')
            #截图
            self.save_imgs(model)
            raise

    # 处理select下拉框
    def select(self,loc,text,model=None):
        # 查找元素
        ele = self.get_Element(loc,model)
        # 滑动滚动条
        logging.info('在{0}页面，选择{1}select框'.format(model,loc))
        s = Select(ele)
        try:
            #s.select_by_value(text)
            s.select_by_visible_text(text)
            print(s.options)
        except:
            logging.exception('select选择失败！！！')
            #截图
            self.save_imgs(model)
            raise

