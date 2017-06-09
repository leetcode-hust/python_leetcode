#!/usr/bin/python
# -*- coding: utf-8 -*
"""
:author:
    Lou yuting
:create_date:
    2017
:descrition:
    error
"""



import paramiko


hostname="123.206.13.151"
user = "root"
pwd="733733"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, 22, user, pwd)

stdin, stdout, stderr = ssh.exec_command("ls /opt/")
for line in stdout:
    print '... ' , line.strip('\n')
ssh.close()


