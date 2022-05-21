# -*- coding: utf-8 -*-
from base.base import BasePage


class LoginUooc(BasePage):
    login_btn = 'id=loginBtn'
    iframe2 = 'id=layui-layer-iframe2'
    name_input = 'id=account'
    pwd_input = 'id=password'

    def login_uooc(self, name="liukaijing", password="lkjLKJ+2021"):
        self.click(LoginUooc.login_btn)
        self.switch_frame(LoginUooc.iframe2)
        self.input(LoginUooc.name_input, name)
        self.input(LoginUooc.pwd_input, password)
