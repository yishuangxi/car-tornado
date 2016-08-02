# coding=utf8
from base import ServiceBase
from model.user import ModelUser
from tornado.gen import coroutine, Return
import re


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




    #####         字段合法性检测       #########
    @coroutine
    def __check_password(self, password):
        valid = self.check_len(password, 1, 10)
        if not valid:
            raise Return((valid, 'password字段长度不合法'))

        valid = self.check_str(password)
        if not valid:
            raise Return((valid, 'password字段内容不合法'))

        raise Return((True, None))

    @coroutine
    def __check_phone(self, phone):
        re_phone = re.compile(r'^[0-9]{11}$')

        if not re_phone.match(phone):
            raise Return((False, 'phone字段内容不合法'))
        user = yield self.model_user.find_one_by_phone(phone)
        if user:
            raise Return((False, "phone字段内容已经存在"))
        else:
            raise Return((True, None))

    @coroutine
    def __check_sex(self, sex):
        if sex not in ['male', 'female']:
            raise Return((False, 'sex字段不合法'))
        else:
            raise Return((True, None))

    @coroutine
    def __check_username(self, username):
        # 优先检测长度
        valid = self.check_len(username, 1, 10)
        if not valid:
            raise Return((valid, 'username字段长度不合法'))

        # 再检测字段内容合法性
        valid = self.check_str(username)
        if not valid:
            raise Return((valid, 'username字段内容不合法' + username))

        # 再检测是否存在数据库中
        user = yield self.model_user.find_one_by_username(username)
        if user:
            raise Return((False, 'username: \'' + username + '\'已经存在'))

        raise Return((True, None))

    @coroutine
    def check_register(self, username, password, phone, sex):
        valid, msg = yield self.__check_username(username)
        if not valid:
            raise Return((valid, msg))

        valid, msg = yield self.__check_password(password)
        if not valid:
            raise Return((valid, msg))

        valid, msg = yield self.__check_phone(phone)
        if not valid:
            raise Return((valid, msg))

        valid, msg = yield self.__check_sex(sex)
        if not valid:
            raise Return((valid, msg))

        raise Return((True, None))
