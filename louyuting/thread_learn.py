#!/usr/bin/python
# -*- coding: utf-8 -*
"""
:author:
    Lou yuting
:create_date:
    2017
:descrition:
    python 的多线程学习代码：

"""

import time, threading

# 新线程执行的代码:
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n= 0
    while n < 5:
        n = n+1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name


print 'thread %s is running...' % threading.current_thread().name
thread = threading.Thread(target=loop, name='LoopThread')
thread.start()
thread.join()
print 'thread %s ended.' % threading.current_thread().name