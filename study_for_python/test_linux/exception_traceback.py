# __author__ = 'Administrator'
# coding=utf8


import re
import os


r_path = "/root/script/python/test_linux"
r_head, r_tail = os.path.split(r_path)
print r_head, r_tail
# m = re.split(r',', 'runoob,runoob,runoob.')
# print m
# it = re.finditer(r"\d+", "12a32bc43jf3")
# print type(it)
# for i in it:
#     print i.group()
# pattern = re.compile(r'\d+')  # 匹配数字
# result1 = pattern.findall('runoob 123 google 456')
# result2 = pattern.findall('run88oob123google456', 0, 10)
#
# print(result1)
# print(result2)
# s = "Hello World Wide Web"
# pattern = re.compile(r'([a-z]{1,}) ([a-z]+)', re.I)
# m = pattern.match("Hello World Wide Web")
# print m.groups()
# s = 'A23G4HFD567'
# pattern = re.compile(r'\d+')
# m = pattern.match('one12twothree34four')
# print m
#
# print re.compile(r'\d+').match('one12twothree34four')
# m = re.compile(r'(\d+)').match('one12twothree34four', 3, 10)   # 从'1'的位置开始匹配，正好匹配到12
# print m.start()     # 匹配到的起始位置为3
# print m.end()       # 匹配到的终止位置为5
# print m.span()      # 匹配到的位置（3，5）
# print m.group()     # 匹配到的内容12
# print m.group(1)    # 获取匹配的内容12，匹配的时候加上了括号
# n = re.compile(r'(?P<name>\d+)').match('one12twothree34four', 3, 10)
# print n.group('name')

# def double(matched):
#     value = int(matched.group('name'))
#     return str(value * 2)
#
#
# print re.sub(r'(?P<name>\d+)', double, s)  # 将\d匹配到的保存在分组name中(匹配到的就是数字),然后将匹配到的传入到函数double中进行替换
# print re.search(r'(?P<name>\d+\w\d+)', s, re.M | re.I).group('name')
# print re.search(r'(?P<name>(?<=A)\d+)', s, re.M | re.I).group('name')
# phone = "2004-959-559 # 这是一个国外电话号码"
# num = re.sub(r'#.*$', '', phone)
# print num
#
# num1 = re.sub(r'\D', '', num)     # \D:匹配任意非数字
# print num1
# line = "Cats are smarter than dogs"
# print len(line)
#
# matchobj = re.match(r'dogs', line, re.M | re.I)
# if matchobj:
#     # print "matchobj.group(): ", matchobj.group()
#     print "matchobj.group(): %s" % matchobj.group()
# else:
#     print "not match"
#
# matchobj = re.search(r'dogs', line, re.M | re.I)
# if matchobj:
#     print "matchobj.group(): ", matchobj.group()
# else:
#     print "not match"
# matchObj = re.match(r'(.*) are (.*) .*', line, re.M | re.I)    # 括号是进行的分组，这里有两个括号，表示有两个分组
# print type(matchObj)
# print matchObj.group()
# print matchObj.group(1)   # 得到分组的内容
# print matchObj.groups()   # 将分组的内容使用元祖进行返回
# print matchObj.span()

# print re.search('www', 'www.baidu.com').span()
# print re.search('com', 'www.baidu.com').span()
# print re.search(r'(.*) are (.*) .*', line, re.M | re.I).group()
# print re.search(r'(.*) are (.*) .*', line, re.M | re.I).group(1)
