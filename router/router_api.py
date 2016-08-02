#coding=utf8
from api import user

router = [
    (r'/api/user/(\d+)', user.ApiUserDetail),
    (r'/api/user/login', user.ApiUserLogin),
    (r'/api/user/register', user.ApiUserRegister),
]