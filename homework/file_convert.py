#!/usr/bin/python3
user_list = {}

with open("user_list.txt","r") as f:
    for i in f.readlines():
        (user,passwd) = i.strip().split()
        #  print(i.strip().split())
        user_list[user] = passwd


print(user_list)
