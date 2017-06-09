#!/usr/bin/python
# -*- coding: utf-8 -*
"""
:author:
    Lou yuting
:create_date:
    2017
:descrition:
    python 的多线程学习代码：
    python 创建多线程有两种方式： 传入target函数； 或则继承 threading.Thread类然后实现run() 方法
"""
import time, threading


def loop():
    """
    新线程执行的代码:
    :return:
    """
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n += 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name


print 'thread %s is running...' % threading.current_thread().name
thread = threading.Thread(target=loop, name='LoopThread')
thread.start()  # 等待cpu的调度
print 'thread %s ended.' % threading.current_thread().name
