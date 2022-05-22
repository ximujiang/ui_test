# -*- coding: utf-8 -*-
from time import sleep

from base.base import BasePage


class LoginUooc(BasePage):
    login_btn = 'id=loginBtn'
    iframe2 = 'xpath=//*[contains(@id,"layui-layer-iframe")]'
    name_input = 'id=account'
    pwd_input = 'id=password'
    rectBottom = 'id=rectBottom'
    tencent = 'xpath=//*[@site="/oauth/login/qq"]/span'
    ptlogin_iframe = 'id=ptlogin_iframe'
    qq = 'xpath=//*[contains(@id,"nick")]'
    check_bottom = 'xpath=//*[@id="autoUrgeLearnReminder"]/div[2]/button'
    def step_login_uooc(self):
        self.click(LoginUooc.login_btn)
        self.element_wait(LoginUooc.iframe2)
        self.switch_frame(LoginUooc.iframe2)
        self.click(LoginUooc.tencent)
        self.element_wait(LoginUooc.ptlogin_iframe)
        self.switch_frame(LoginUooc.ptlogin_iframe)
        self.click(LoginUooc.qq)
        self.switch_default()
        self.click(LoginUooc.check_bottom)
        sleep(3)
