# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.open("http://www.uooconline.com/")

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
        :param element: 定位元素："id=kw","name=wd",
        :return:
        """
        el = element.sqlt("=", 1)
        by = el[0]
        value = el[1]
        if by == "id":
            locator_element = self.driver.find_element(By.ID, value)
        elif by == "name":
            locator_element = self.driver.find_element(By.NAME, value)
        elif by == "xpath":
            locator_element = self.driver.find_element(By.XPATH, value)
        elif by == "tag_name":
            locator_element = self.driver.find_element(By.TAG_NAME, value)
        elif by == "css" or by == "css_selector":
            locator_element = self.driver.find_element(By.CSS_SELECTOR, value)
        elif by == "link_text":
            locator_element = self.driver.find_element(By.LINK_TEXT, value)
        elif by == "partial_link_text":
            locator_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, value)
        elif by == "class_name":
            locator_element = self.driver.find_element(By.CLASS_NAME, value)
        else:
            locator_element = self.driver.find_element(By.XPATH, value)
        return locator_element

    def click(self, element):
        """
        点击操作
        :param element:
        :return:
        """
        self.locator_element(element).click()

    def input(self, element, value):
        """
        输入文本
        :param element: 定位元素
        :param value: 输入的值
        :return:
        """
        self.locator_element(element).send_keys(value)

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

    def switch_frame(self, element):
        """
        切换框架
        :param element:
        :return:
        """
        if "id" in element or "name" in element:
            self.driver.switch_to.frame(element.sqlt("=", 1)[1])
        else:
            self.driver.switch_to.frame(self.locator_element(element))

    def switch_default(self):
        """
        切换回默认框架
        :return:
        """
        self.driver.switch_to.default_content()
