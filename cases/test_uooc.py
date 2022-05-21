# -*- coding: utf-8 -*-
from pageobject.login_page import LoginUooc


class TestUooc:
    def test_uooc(self):
        lp = LoginUooc()
        lp.login_uooc()
