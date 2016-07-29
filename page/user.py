# coding=utf8

from base import PageBase


class PageLogin(PageBase):
    def get(self, *args, **kwargs):
        self.render('web/user/login.html')


class PageRegister(PageBase):
    def get(self, *args, **kwargs):
        self.render('web/user/register.html')


class PageEdit(PageBase):
    def get(self, *args, **kwargs):
        self.render('web/user/edit.html')


class PageDetail(PageBase):
    def get(self, user_id):
        self.render('web/user/detail.html')
