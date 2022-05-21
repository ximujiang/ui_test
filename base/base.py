# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    driver = webdriver.Chrome()

    def open(self, url):
        """
        访问url
        :param url: 网页地址
        :return:
        """
        self.driver.get(url)

    def locator_element(self, element):
        """
        定位元素位置
        :param element:
        :return:
        """
        return self.driver.find_element(element)

    def click(self, element):
        """
        点击操作
        :param element:
        :return:
        """
        self.locator_element(element).click()

    def quit(self):
        """
        退出浏览器
        :return:
        """
        self.driver.quit()

    def element_wait(self, element):
        """
        等待元素出现
        :param element:
        :return:
        """
        return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locator_element(element), message="元素查找失败！")

    def switch_frame(self, value, name=None):
        """
        切换框架
        :param value:
        :param name:
        :return:
        """
        if name is None:
            self.driver.switch_to.frame(value)
        else:
            self.driver.switch_to.frame(self.locator_element(element=value))

    def switch_default(self):
        """
        切换回默认框架
        :return:
        """
        self.driver.switch_to.default_content()


