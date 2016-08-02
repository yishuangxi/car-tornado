# coding=utf8
from base import ModelBase
from tornado.gen import coroutine, Return

class ModelUserBase(ModelBase):
    def __init__(self, *args, **kwargs):
        super(ModelUserBase, self).__init__(*args, **kwargs)

class ModelUser(ModelUserBase):
    @coroutine
    def find_one_by_username_password(self, username, password):
        sql = 'select * from user where username=%s, password=%s'
        res = yield self.get(sql, username, password)
        raise Return(res)

    @coroutine
    def find_one_by_id(self, user_id):
        sql = 'select * from user where id=%s'
        res = yield self.get(sql, user_id)
        raise Return(res)

    @coroutine
    def find_one_by_username(self, username):
        sql = 'select * from user where username=%s'
        res = yield self.get(sql, username)
        raise Return(res)

    @coroutine
    def find_one_by_phone(self, phone):
        sql = 'select * from user where phone=%s'
        res = yield self.get(sql, phone)
        raise Return(res)