# -*- coding:utf-8 -*-

import psutil
import requests

from itchat.content import TEXT


class MonitorHandler(object):
    """system monitor handler
    """

    HANDLE_MSGS = (TEXT,)
    DEFAULT_MSG = u'监控指令暂未支持'

    def match(self, msg):
        if msg.text.startswith('/m'):
            return True
        return False

    def handle(self, msg):
        if any(p in msg.text for p in ['cpu', 'c', 'm', 'mem']):
            return self.cpu_mem()
        return self.DEFAULT_MSG

    def cpu_mem(self):
        """return cpu memory usage
        """
        line = ''
        percs = psutil.cpu_percent(interval=0, percpu=True)
        for cpu_num, perc in enumerate(percs):
            line += 'CPU%-2s %5s%%\n' % (cpu_num, perc)
        mem = psutil.virtual_memory()
        line += 'Mem    %5s%% %6s / %s\n' % (
            mem.percent,
            str(int(mem.used / 1024 / 1024)) + 'M',
            str(int(mem.total / 1024 / 1024)) + 'M')
        return line


class TuringHandler(object):
    """ turing handler

    Referer: http://www.tuling123.com/
    """

    HANDLE_MSGS = (TEXT,)
    DEFAULT_MSG = u'图灵机器人走丢啦'

    def __init__(self, key, user_id):
        self.key = key
        self.user_id = user_id

    def match(self, msg):
        return True

    def handle(self, msg):
        url = 'http://www.tuling123.com/openapi/api'
        data = {'key': self.key, 'info': msg.text, 'userid': self.user_id}

        try:
            result = requests.post(url, data=data).json()
        except requests.exceptions.RequestException:
            return self.DEFAULT_MSG
        return result.get('text') or self.DEFAULT_MSG


class XiaodouHandler(object):
    """ xiaodou robot handler

    Referer: http://xiao.douqq.com
    """

    HANDLE_MSGS = (TEXT, )
    DEFAULT_MSG = u'小豆机器人走丢啦'

    KEY = 'http://api.douqq.com/?key=&msg=??'

    def __init__(self, key):
        self.key = key

    def match(self, msg):
        return True

    def handle(self, msg):
        url = 'http://api.douqq.com'
        params = {'key': self.key, 'msg': msg.text}
        try:
            resp = requests.get(url, params=params)
        except requests.exceptions.RequestException:
            return self.DEFAULT_MSG
        return resp.text
