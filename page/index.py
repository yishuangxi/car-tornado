#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from base import BasePage

class IndexPage(BasePage):
    def get(self):
        self.render('web/index/index.html')
