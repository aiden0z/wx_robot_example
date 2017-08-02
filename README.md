### 介绍

该项目为实验楼课程 [《利用微信API将你的微信变为聊天机器人》](https://www.shiyanlou.com/courses/684) 直播视频的相关代码。在直播中，我们基于 [itchat](https://github.com/littlecodersh/ItChat) 软件包实现了一个简单的微信机器人，接入了 [图灵机器人](http://www.tuling123.com/), [小豆机器人](http://xiao.douqq.com/), 以及简单的系统监控功能。

课程地址 https://www.shiyanlou.com/courses/684

直播视频回放地址 http://www.bilibili.com/video/av12860627/


<br />
<br />
<p align="center"><img src="https://raw.githubusercontent.com/aiden0z/wx_robot_example/master/robot.png"></p>
<p align="center">效果图</p>

## 原理

如果我们能模拟微信登录，能接收到微信消息，就可以针对这些消息进行分析处理并作出相应的响应，这就是微信聊天机器人的基本原理。

简单来说，我可以通过 [itchat](https://github.com/littlecodersh/ItChat) 模拟登录微信账户 A，当账户登录成功后，使用其他的微信账户给 A 账户发送消息，就可以看到聊天机器人的效果了。

该项目实现的微信机器人不仅接入了小豆机器人，还实现了简单的系统监控功能，系统性能数据采集基于包 [psutil](https://github.com/giampaolo/psutil) 实现。

## 运行项目

安装 Python 执行环境后，可以通过 `pip` 命令安装 `virtualenv` 软件包，然后基于该包搭建执行环节。通过以下步骤启动本项目：

```
# 创建工作目录
$ mkdir ~/project
$ cd ~/project
# 克隆本项目
$ git clone https://github.com/aiden0z/wx_robot_example.git wx_robot
$ cd wx_robot
# 安装 virutalenv 软件包，如果已经安装，可以跳过该操作
$ sudo pip install virtualenv
# 创建 virtualenv 环境
$ virtualenv env
# 激活 virtualenv 环境
$ source env/bin/activate
# 安装项目依赖包
$ pip install -r requirements.txt
# 启动机器人
$ python robot.py
```

以上步骤中，以 `#` 开始的行为注释， `$` 开头的行为真正需要执行的命令。其中 `requirements.txt` 包含了本项目所有的依赖包。项目启动成功后，可以看到类似以下的效果：

```
 $ python wx_robot.py
Getting uuid of QR code.
Downloading QR code.
Please scan the QR code to log in.
```

接着扫描二维码登录，并使用微信好友发送消息，就可以看到效果了。

## 反馈

如果你有任何问题可以到 [实验楼讨论区](https://www.shiyanlou.com/questions/) 进行提问，或者在本项目中开 issue。

更多更精彩的课程，可以前往 [实验楼](https://www.shiyanlou.com) 学习。
