#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from base import PageBase

class PageIndex(PageBase):
    def get(self):
        self.render('web/index/index.html')
