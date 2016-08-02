# coding=utf8
from base import ServiceBase
from model.user import ModelUser
from tornado.gen import coroutine, Return

class ServiceUser(ServiceBase):
    def __init__(self, *args, **kwargs):
        super(ServiceUser, self).__init__()
        self.model_user = ModelUser()

    @coroutine
    def find_one_by_username_password(self, username, password):
        res = self.model_user.find_one_by_username_password()
        raise Return(res)

    @coroutine
    def find_one_by_id(self, user_id):
        res = yield self.model_user.find_one_by_id(user_id=user_id)
        raise Return(res)

    @coroutine
    def create(self, username, password, phone, sex):
        res = yield self.model_user.create(username, password, phone, sex)
        raise Return(res)