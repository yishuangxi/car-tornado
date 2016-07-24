#coding=utf8

from base import BasePage

class LoginPage(BasePage):
    def get(self, *args, **kwargs):
        self.render('web/user/login.html')

class RegisterPage(BasePage):
    def get(self, *args, **kwargs):
        self.render('web/user/register.html')

class EditPage(BasePage):
    def get(self):
        self.render('web/user/edit.html')

class DetailPage(BasePage):
    def get(self, user_id):
        self.render('web/user/detail.html')

