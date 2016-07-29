# coding=utf8
from page import index
from page import user

router = [
    (r'/', index.PageIndex),

    #user
    (r'/login', user.PageUserLogin),
    (r'/register', user.PageUserRegister),
    (r'/user/(\d+)', user.PageUserDetail),
    (r'/user/edit', user.PageUserEdit)
]
