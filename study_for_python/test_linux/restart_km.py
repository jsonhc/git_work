# __author__ = 'Administrator'
# coding=utf8


import json
import commands


originJson = "/root/script/python/test_linux/km_original.json"
newJson = "/root/script/python/test_linux/km_hotfix.json"


def modify():
    j = json.load(file(originJson))
    print j['subsets'][0]['addresses'][0]['ip']
    print j['subsets'][1]['addresses'][0]['ip']
    j['subsets'][0]['addresses'][0]['ip'] = '192.168.101.104'
    j['subsets'][1]['addresses'][0]['ip'] = '192.168.101.105'
    s = json.dumps(j)   # 将josn文件倒出来
    print type(s)    # s的数据类型为str
    fp = open(newJson, 'w')
    fp.write(s)
    fp.close()


def start():
    cmd = '/usr/bin/python test_linux.py'
    ret = commands.getoutput(cmd)
    print ret       # 返回命令的执行结果
    print ret.find('OK')    # 检测ret字符串中是否包含OK字符串，如果不包含则返回固定值-1


def stop():
    cmd = "/usr/bin/python test_linux.py"
    status, ret = commands.getstatusoutput(cmd)
    print status   # 命令执行成功返回成功状态码0
    print ret    # 返回命令执行的结果


if __name__ == '__main__':
    # modify()
    start()
    # stop()
