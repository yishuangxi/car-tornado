# coding=utf8
import re
from tornado.gen import coroutine, Return


class ServiceBase(object):

    def check_len(self, value, min, max):
        if min < len(value) < max:
            return True
        else:
            return False
    def check_str(self, value):
        return True

    def check_digital(self, value):
        pass
