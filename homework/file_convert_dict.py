#!/usr/bin/python3

d = {}

with open("file_convert_dict.txt","r") as f:
    for i in f.readlines():
        (user,passwd) = i.strip().split()
        d[user] = passwd


print(d)
