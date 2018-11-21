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


# import commands
# cmd = "free -m"
# s, r = commands.getstatusoutput(cmd)    # 执行结果返回的是tuple的类型，一个是命令返回的结果值，一个是int类型的返回码
# s1 = commands.getoutput(cmd)   # 执行结果返回的是字符串，直接返回命令执行结果值
# print(type(s1))
# print(type(commands.getstatusoutput(cmd)))
# print(type(s))
# print(type(r))
# # print(s1)
# # print(s)
# # print(r)


# import sys
# print(sys.argv[0])
# L = sys.path
# for i in L:
#     print(i)


# import time
# print(time.time())    # 得到从1970到现在的秒数  seconds
# print(time.localtime())
# print(time.localtime(time.time()))
# time_list = time.localtime()
# print(type(time_list))    # <type 'time.struct_time'>
# print(time_list.tm_year)   # 得到年份2018
# print(time.strftime("%Y-%m-%d %H:%M:%S", time_list))     # 将结构化元祖时间转化为格式化字符串时间   2018-11-21 16:46:46
# print(time.strptime("2018-11-21 16:43:26", "%Y-%m-%d %H:%M:%S"))     # 将格式化字符串时间转化为结构化元祖时间
# print(time.ctime(time.time()))    # ctime函数的参数为sec，秒，得到结果为  Wed Nov 21 16:49:17 2018


import datetime
print(datetime.datetime.now())       # 获取当前时间的时间格式化输出    2018-11-21 16:51:53.214165
print(datetime.datetime.now() + datetime.timedelta(3))   # 获取三天后的时间   2018-11-24 17:01:09.468866
print(datetime.datetime.now() + datetime.timedelta(hours=3))   # 获取当前时间的后三个小时   2018-11-21 20:01:09.468885
