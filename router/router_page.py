# coding=utf8
from page import index
from page import user

router = [
    (r'/', index.IndexPage),

    #user
    (r'/login', user.LoginPage),
    (r'/register', user.RegisterPage),
    (r'/user/(\d+)', user.DetailPage),
    (r'/user/edit', user.EditPage)
]
