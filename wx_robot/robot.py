# -*- coding:utf-8 -*-

from itchat.core import Core
from itchat.content import TEXT


class WxRobot(object):
    """ Wechat robot
    """

    def __init__(self, hot_reload=False, default_msg=u'暂未支持'):
        self.hot_reload = hot_reload
        self.wx = Core()
        self.handlers = []
        self.default_msg = default_msg

    def register_handler(self, handler):
        self.handlers.append(handler)

    def dispatch(self):

        @self.wx.msg_register(TEXT)
        def _dispatcher(msg):
            for h in self.handlers:
                if h.match(msg):
                    return h.handle(msg)
            else:
                return self.default_msg

    def run(self):
        self.dispatch()
        self.wx.auto_login(hotReload=self.hot_reload)
        self.wx.run()
