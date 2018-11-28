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


import time
# print(time.time())    # 得到从1970到现在的秒数  seconds
# print(time.localtime())    # struct_time共九个元素，结构化时间元祖
# print(time.localtime(time.time()))   # 与上面一样
# time_list = time.localtime()
# print(type(time_list))    # <type 'time.struct_time'>
# print(time_list.tm_year)   # 得到年份2018
# print(time.strftime("%Y-%m-%d %H:%M:%S", time_list))     # 将结构化元祖时间转化为格式化字符串时间   2018-11-21 16:46:46
# print(time.strptime("2018-11-21 16:43:26", "%Y-%m-%d %H:%M:%S"))     # 将格式化字符串时间转化为结构化元祖时间
# print(time.mktime(time.strptime("2018-11-21 16:43:26", "%Y-%m-%d %H:%M:%S")))    # 1542789806.0 获取从1970到现在的秒数  seconds
# print(time.ctime(time.time()))    # ctime函数的参数为sec，秒，得到结果为  Wed Nov 21 16:49:17 2018


import datetime
# print(datetime.datetime.now())       # 获取当前时间的时间格式化输出    2018-11-21 16:51:53.214165
# print(datetime.datetime.now() + datetime.timedelta(3))   # 获取三天后的时间   2018-11-24 17:01:09.468866
# print(datetime.datetime.now() + datetime.timedelta(hours=3))   # 获取当前时间的后三个小时   2018-11-21 20:01:09.468885
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))    # 获取当前时间的格式化输出  2018-11-21 17:23:47
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:00:00"))    # 2018-11-21 19:00:00
# t1 = time.localtime()
# t2 = datetime.datetime.now()
# print(time.strftime("%Y-%m-%d %H:%M:%S", t1))     # 2018-11-21 20:26:05
# print(t2.strftime("%Y-%m-%d %H:%M:%S"))    # 2018-11-21 20:26:05


import subprocess
cmd = "free -m"
# p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# stdout, stderr = p.communicate()  # communicate方法返回的是一个tuple类型，stderr是int类型，stdout是str类型
# print(p.returncode)
# print("==========================")
# print(stderr)
# print("==========================")
# print(stdout)
# p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# stdout, stderr = p.communicate()
# print(stdout)
# print(stderr)


# def runcmd(cmd):
#     p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = p.communicate()
#     return stdout, stderr
#
#
# stdout, stderr = runcmd(cmd)
# print(stdout)
class Datetime:
    def __init__(self):
        pass

    @staticmethod     # staticmethod方法与__init__方法的区别：不需要带有self参数
    def get_time_stamp():
        res = datetime.datetime.now().strftime("'%Y-%m-%d %H:%M:%S'")
        return res     # 2018-11-28 15:37:19

    @staticmethod
    def get_time_now():
        res = time.localtime()
        result = time.strftime("'%Y-%m-%d %H:%M:%S'", res)
        return result    # 2018-11-28 15:37:19

    @staticmethod
    def get_time_expect():
        result = datetime.datetime.strptime('2018-11-30 15:00:00', '%Y-%m-%d %H:%M:%S')
        return result    # 2018-11-30 15:00:00


t = Datetime()
print t.get_time_now()
print(t.get_time_stamp())
print(t.get_time_expect())
# params = {}
# params["user"] = "wadeson"
# if not isinstance(params, dict):
#     print('false')
# else:
#     print('OK')
#
# rows = [1, 2, 3, 4]
# custins_list = [l for l in rows]
# print(custins_list)
