#!/usr/bin/python3
import getpass

user_list = {}
lock_user = []

# 读取文件中的的账号和密码保存在用户字典中
with open("user_list.txt","r") as f1:
    for i in f1.readlines():
        (user,passwd) = i.strip().split()
        user_list[user] = passwd

# 读取锁用户文件中的user保存在列表中
with open("lock_user.txt","r") as f2:
    for i in f2.readlines():
        user = i.strip()
        lock_user.append(user)


user_get=input("please input user:")
passwd_get=getpass.getpass("please input password:")
T = 0

while T < 2:
    # 当输入的名字存在于锁用户中时，直接退出
    if user_get in lock_user:
        print("your user %s has been locked,please contact administrator" % user_get)
        break
    # 当输入的用户不存在锁用户中：1，账号密码进行判断三次  2，账号不存在
    else:
        if  user_get not in user_list.keys():
            print("user %s is not exist,please register!" % user_get)
            break
        else:
            if passwd_get == user_list[user_get]:
                print("welcome to %s" % user_get)
                break
            else:
                print("your password is wrong,please try again")
                T = T + 1
    user_get=input("please input user:")
    passwd_get=getpass.getpass("please input password:")

else:
    print("your user %s has been locked!" % user_get)
    lock_user.append(user_get)
    with open("lock_user.txt","w") as f_lock:
        for i in lock_user:
            f_lock.write("%s\n" % i)
