#!/usr/bin/python
# -*- coding: utf-8 -*
"""
:author:
    Lou yuting
:create_date:
    2017
:descrition:
    该文件执行方式：  python file.py count
"""
import subprocess
import threading
import sys

import requests

# p = subprocess.Popen('ls /', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# print p.stdout.readlines()

DEFAULT_MAX_NUM = 1000


def execute_command(command):
    """
    :param command: 执行命令行
    :return: void
    """
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def print_log(thread_name, i, r):
    """
    :param thread_name 当前执行的线程名
    :param i
    :param r: request 的返回对象response
    :return:
    """
    execute_command("echo '" + "【" + thread_name + "】-" + str(i) + ":" + str(r.status_code) + "' >> /opt/request.log")


def loop(count):
    """
    循环 count 次， 洪水攻击目标url
    """
    for i in range(0, count):
        r = requests.get("http://123.206.13.151")
        # print r.content
        print "【", i, "】 : 【", r.status_code, "】"
        print_log(threading.currentThread().getName(), i, r)
        r.close()


"""
main 函数的入口
"""
print "开始测rgs试Nginx的性能："
args = sys.argv
count = 0
if len(args) == 1:
    print "当前线程测试数量默认是：", str(DEFAULT_MAX_NUM)
    count = DEFAULT_MAX_NUM
else:
    print "当前线程测试数量设置是：", str(args[1])
    count = int(args[1])

# 先清除上次的日志文件
execute_command("rm -rf /opt/request.log")
threading.currentThread().setName("Main-Thread-1")
print "当前线程名：", threading.currentThread().getName()
loop(count)
