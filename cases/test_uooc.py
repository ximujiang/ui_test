# -*- coding: utf-8 -*-
from pageobject.subject_page import Subjects


class TestUooc:
    def test_uooc(self, drivers):
        self.sub = Subjects(drivers)
        self.sub.step_selector_course("操作系统")
        self.sub.step_set_su_du()
