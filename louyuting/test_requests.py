#!/usr/bin/python
# -*- coding: utf-8 -*
"""
:author:
    Lou yuting
:create_date:
    2017
:descrition:
    requests 测试代码
"""

import requests

res = requests.get("https://github.com/timeline.json")

print res.encoding
print res.text
print res.content
print res.json()
print "status_code", res.status_code
print "apparent_encoding", res.apparent_encoding
print "cookies", res.cookies
print "headers", res.headers
print "history", res.history
res.close()

