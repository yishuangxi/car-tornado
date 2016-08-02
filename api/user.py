# coding=utf8
from base import ApiBase
from tornado.gen import coroutine, Return
from service.user import ServiceUser


class ApiUserBase(ApiBase):
    def __init__(self, *args, **kwargs):
        super(ApiUserBase, self).__init__(*args, **kwargs)
        self.srv_user = ServiceUser()


class ApiUserLogin(ApiUserBase):
    @coroutine
    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')

        user = self.srv_user.find_one_by_username_password(username, password)
        if user:
            pass
        else:
            pass


class ApiUserDetail(ApiUserBase):
    @coroutine
    def get(self, user_id):
        user = yield self.srv_user.find_one_by_id(user_id)
        self.json_success(data=user)


class ApiUserRegister(ApiUserBase):
    @coroutine
    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        phone = self.get_argument('phone')
        sex = self.get_argument('sex')

        user_id = yield self.srv_user.create(username, password, phone, sex)

        self.json_success(data=user_id)



