# coding=utf8

from tornado.ioloop import IOLoop
from tornado.web import Application
from config.config_site import config_site
from router.router_all import router_all

if __name__ == '__main__':
    app = Application(router_all, **config_site)
    app.listen(8888)
    print 'serving on http://localhost:8888'
    IOLoop.instance().start()
