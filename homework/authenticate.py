#!/usr/bin/python3
import json

with open("username.json","r") as f:
     user_dict=json.load(f)

username=user_dict["name"]
passwd=user_dict["password"]

user_get=input("please input user:")
passwd_get=input("please input password:")
T = 0

while T < 2:
    if user_get == username and passwd_get == passwd:
        print("welcome to user:",user_get)
        break
    else:
        print("user %s or password %s is wrong!" % (user_get,passwd_get))
        T = T + 1
    user_get=input("please input user:")
    passwd_get=input("please input password:")

else:
    print("your user %s has been locked!" % user_get)
    with open("lock_user.json","w") as f_lock:
        pass
