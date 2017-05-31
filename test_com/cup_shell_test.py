# -*- coding: utf-8 -*
#  特色示例
# 1. 拥有超时控制的shell执行. 超时shell命令会被kill (SIGTERM)

from com_utils.shell import ShellExec

shell = ShellExec()

ret = shell.run('/bin/ls /opt/', timeout=1)
print "stdout:\n", ret["stdout"]
print "stderr:\n", ret["stderr"]
print "returncode\n:", ret["returncode"]

# 2. 其他类，比如使用rm -rf删除某路径，获取文件MD5等
# cup.shell.md5file(filename) # 计算一个文件的md5值。返回32位长的hex字符串。
#
# cup.shell.kill9_byname(strname) # kill -9 process by name
#
# cup.shell.del_if_exist(path) # 如果文件/目录/symlink存在则删除他们

# 3. 进行远程shell操作 （内部调用了pexpect)

# 具体参照 http://docs.iobusy.com/docs/cup/cup.shell.html#module-cup.shell.expect
# 其中exit_status为本地ssh命令退出码， remote_status为远程的退出码