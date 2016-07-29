# coding=utf8
from page import index
from page import user

router = [
    (r'/', index.PageIndex),

    #user
    (r'/login', user.PageLogin),
    (r'/register', user.PageRegister),
    (r'/user/(\d+)', user.PageDetail),
    (r'/user/edit', user.PageEdit)
]
