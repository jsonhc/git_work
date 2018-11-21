# __author__ = 'Administrator'
# coding=utf8


import os

# print(__file__)
# base_dir = os.path.dirname(__file__)
# print(base_dir)
# print(os.getcwd())
# L = os.listdir(base_dir)
# for i in L:
#     j = os.path.join(base_dir, i)
#     print(j)
#     with open(j, "r") as f:
#         for line in f.readlines():
#             print(line)

# print(__file__)
# with open("/root/script/python/test_linux/test_linux.py", "r") as f:
#     for i in f.readlines():
#         print(i)


import commands
cmd = "free -m"
s, r = commands.getstatusoutput(cmd)    # 执行结果返回的是tuple的类型，一个是命令返回的结果值，一个是int类型的错误码
s1 = commands.getoutput(cmd)   # 执行结果返回的是字符串，直接返回命令执行结果值
print(type(s1))
print(type(commands.getstatusoutput(cmd)))
print(type(s))
print(type(r))
# print(s1)
# print(s)
# print(r)


import sys
print(sys.argv[0])