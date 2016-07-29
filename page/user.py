# coding=utf8

from base import PageBase


class PageUserLogin(PageBase):
    def get(self, *args, **kwargs):
        self.render('web/user/user_login.html')


class PageUserRegister(PageBase):
    def get(self, *args, **kwargs):
        self.render('web/user/user_register.html')


class PageUserEdit(PageBase):
    def get(self, *args, **kwargs):
        self.render('web/user/user_edit.html')


class PageUserDetail(PageBase):
    def get(self, user_id):
        self.render('web/user/user_detail.html')
