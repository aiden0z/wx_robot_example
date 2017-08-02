# -*- coding:utf-8 -*-

from wx_robot.handler import MonitorHandler, XiaodouHandler
from wx_robot.robot import WxRobot


if __name__ == '__main__':
    robot = WxRobot(hot_reload=True)

    monitor = MonitorHandler()
    robot.register_handler(monitor)

    xiaodou_key = 'ZDVRRGo2NWR3RGdUVEFlPUE1QXQvPVRlWXhJQUFBPT0'
    xiaodou = XiaodouHandler(xiaodou_key)
    robot.register_handler(xiaodou)

    robot.run()

