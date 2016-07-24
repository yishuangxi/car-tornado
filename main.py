# coding=utf8

from tornado.ioloop import IOLoop
from tornado.web import Application
from config.config_site import config_site
from router.all import router

if __name__ == '__main__':
    app = Application(router, **config_site)
    app.listen(8888)
    IOLoop.instance().start()
